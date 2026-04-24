import random
import math
import tkinter as tk
from collections import deque

SEED, N, K = 5515, 11, 0.815
CW, CH, PAD, NR = 800, 650, 60, 20

# ── 1. ГЕНЕРАЦІЯ МАТРИЦІ ТА КООРДИНАТ ──────────────────────────────────────
def gen_adj(seed, n, k):
    random.seed(seed)
    return [[1 if random.uniform(0, 2.0) * k >= 1.0 else 0 for _ in range(n)] for _ in range(n)]

def tri_coords(n, w, h, p):
    v = [(w/2, p), (w-p, h-p), (p, h-p)]
    pts = []
    for i in range(n):
        t = i / n
        if t < 1/3:   a, b, f = v[0], v[1], t * 3
        elif t < 2/3: a, b, f = v[1], v[2], (t - 1/3) * 3
        else:         a, b, f = v[2], v[0], (t - 2/3) * 3
        pts.append((a[0] + (b[0]-a[0])*f, a[1] + (b[1]-a[1])*f))
    return pts

# ── 2. АЛГОРИТМИ ОБХОДУ (Для консольного виводу) ───────────────────────────
def run_bfs(A):
    n = len(A)
    vis = [False]*n
    T = [[0]*n for _ in range(n)]
    order = []
    for s in range(n):
        # Починаємо лише з невідвіданої вершини, з якої є хоча б один вихід
        if not vis[s] and sum(A[s]) > 0:
            q = deque([s])
            vis[s] = True
            while q:
                v = q.popleft()
                order.append(v + 1)
                for u in range(n):
                    if A[v][u] and not vis[u]:
                        vis[u] = True
                        T[v][u] = 1
                        q.append(u)
    return T, order

def run_dfs(A):
    n = len(A)
    vis = [False]*n
    T = [[0]*n for _ in range(n)]
    order = []
    for s in range(n):
        if not vis[s] and sum(A[s]) > 0:
            vis[s] = True
            order.append(s + 1)
            stk = [(s, 0)]
            while stk:
                v, ni = stk[-1]
                found = False
                for u in range(ni, n):
                    if A[v][u] and not vis[u]:
                        stk[-1] = (v, u + 1)
                        vis[u] = True
                        T[v][u] = 1
                        order.append(u + 1)
                        stk.append((u, 0))
                        found = True
                        break
                if not found:
                    stk.pop()
    return T, order

# ── 3. ГЕНЕРАТОРИ ДЛЯ ПОКРОКОВОГО GUI ──────────────────────────────────────
def bfs_gen(A):
    n = len(A)
    vis = [False]*n
    col = ['white']*n
    te = set()
    for s in range(n):
        if not vis[s] and sum(A[s]) > 0:
            q = deque([s])
            vis[s] = True
            col[s] = 'yellow' # Вершина в черзі
            yield col[:], set(te)
            while q:
                v = q.popleft()
                col[v] = 'green' # Вершина повністю оброблена
                yield col[:], set(te)
                for u in range(n):
                    if A[v][u] and not vis[u]:
                        vis[u] = True
                        col[u] = 'yellow'
                        te.add((v, u)) # ребро до дерева обходу
                        yield col[:], set(te)
                        q.append(u)

def dfs_gen(A):
    n = len(A)
    vis = [False]*n
    col = ['white']*n
    te = set()
    for s in range(n):
        if not vis[s] and sum(A[s]) > 0:
            vis[s] = True
            col[s] = 'yellow' # Вершина в стеку
            stk = [(s, 0)]
            yield col[:], set(te)
            while stk:
                v, ni = stk[-1]
                found = False
                for u in range(ni, n):
                    if A[v][u] and not vis[u]:
                        stk[-1] = (v, u + 1)
                        vis[u] = True
                        col[u] = 'yellow'
                        te.add((v, u))
                        stk.append((u, 0))
                        yield col[:], set(te)
                        found = True
                        break
                if not found:
                    stk.pop()
                    col[v] = 'green' 
                    yield col[:], set(te)

# ── 4. ВІЗУАЛІЗАЦІЯ (Малювання графа) ──────────────────────────────────────
def draw_edge(canvas, A, i, j, coords, fill, width):
    x1, y1 = coords[i]; x2, y2 = coords[j]
    mx, my = (x1+x2)/2, (y1+y2)/2
    dx, dy = x2-x1, y2-y1
    dist = math.hypot(dx, dy)
    if dist == 0: return
    nx, ny = -dy/dist, dx/dist
    off = (40 if i > j else -40) if A[j][i] else 20
    cx, cy = mx + nx*off, my + ny*off
    d = math.hypot(cx-x2, cy-y2)
    ex, ey = (x2 + (cx-x2)/d*NR, y2 + (cy-y2)/d*NR) if d > NR else (x2, y2)
    canvas.create_line(x1, y1, cx, cy, ex, ey, smooth=True,
                       arrow=tk.LAST, arrowshape=(12, 16, 4),
                       fill=fill, width=width)

def redraw(canvas, A, coords, col, te):
    canvas.delete("all")
    n = len(A)
    nc = {'white': 'white', 'yellow': '#FFF59D', 'green': '#81C784'}
    
    # 1. звичайні сірі ребра (які не увійшли в дерево)
    for i in range(n):
        for j in range(n):
            if A[i][j] and i != j and (i, j) not in te:
                draw_edge(canvas, A, i, j, coords, '#E0E0E0', 1)
                
    # 2. товсті червоні ребра (Дерево обходу)
    for i, j in te:
        draw_edge(canvas, A, i, j, coords, '#D32F2F', 3)
        
    # 3. вершини
    for i, (x, y) in enumerate(coords):
        canvas.create_oval(x-NR, y-NR, x+NR, y+NR, fill=nc[col[i]], outline='#424242', width=2)
        canvas.create_text(x, y, text=str(i+1), font=('Arial', 11, 'bold'))

# ── 5. ГОЛОВНА ЛОГІКА ТА ІНТЕРФЕЙС ─────────────────────────────────────────
def main():
    A = gen_adj(SEED, N, K)
    coords = tri_coords(N, CW, CH, PAD)
    
    # Розрахунки для консолі
    Tb, ob = run_bfs(A)
    Td, od = run_dfs(A)

    print(f"=== ЛАБОРАТОРНА РОБОТА №5 (Вар {SEED}, k={K}) ===")
    print("\nПочаткова матриця суміжності Adir:")
    for r in A: print(" ".join(map(str, r)))
    
    print("\n--- BFS (Пошук вшир) ---")
    print("Матриця суміжності дерева обходу BFS:")
    for r in Tb: print(" ".join(map(str, r)))
    print("Порядок обходу (нова нумерація):", " -> ".join(map(str, ob)))

    print("\n--- DFS (Пошук вглиб) ---")
    print("Матриця суміжності дерева обходу DFS:")
    for r in Td: print(" ".join(map(str, r)))
    print("Порядок обходу (нова нумерація):", " -> ".join(map(str, od)))

    # GUI Setup
    root = tk.Tk()
    root.title(f"ЛР5: Обхід графа (BFS/DFS) - Вар {SEED}")
    root.geometry("800x800")
    root.resizable(False, False)

    canvas = tk.Canvas(root, width=CW, height=CH, bg='white')
    canvas.pack(pady=10)

    # Global State
    current_gen = None
    current_state = [['white']*N, set()]
    
    lbl_status = tk.Label(root, text="Оберіть алгоритм для старту", font=('Arial', 14, 'bold'), fg='#1565C0')
    lbl_status.pack(pady=5)

    def start_algo(algo_type):
        nonlocal current_gen, current_state
        current_state = [['white']*N, set()]
        current_gen = bfs_gen(A) if algo_type == 'BFS' else dfs_gen(A)
        lbl_status.config(text=f"Поточний режим: {algo_type} (Очікування першого кроку)")
        redraw(canvas, A, coords, current_state[0], current_state[1])

    def do_step():
        nonlocal current_state
        if current_gen is None: return
        try:
            current_state[0], current_state[1] = next(current_gen)
            redraw(canvas, A, coords, current_state[0], current_state[1])
            lbl_status.config(text=f"Режим: {lbl_status.cget('text').split()[2]} (В процесі...)")
        except StopIteration:
            lbl_status.config(text=f"{lbl_status.cget('text').split()[1]} {lbl_status.cget('text').split()[2]} - ЗАВЕРШЕНО ✅")

    # Buttons
    btn_frame = tk.Frame(root)
    btn_frame.pack(pady=10)

    tk.Button(btn_frame, text="🔄 Почати BFS (Вшир)", font=('Arial', 11), width=20, command=lambda: start_algo('BFS')).grid(row=0, column=0, padx=10)
    tk.Button(btn_frame, text="🔄 Почати DFS (Вглиб)", font=('Arial', 11), width=20, command=lambda: start_algo('DFS')).grid(row=0, column=1, padx=10)
    
    tk.Button(root, text="▶ НАСТУПНИЙ КРОК", font=('Arial', 14, 'bold'), bg='#4CAF50', fg='white', width=30, pady=10, command=do_step).pack(pady=10)

    # Initial Draw
    redraw(canvas, A, coords, current_state[0], current_state[1])
    root.mainloop()

if __name__ == "__main__":
    main()