import random
import math
import tkinter as tk
import heapq

SEED, N, K = 5515, 11, 0.915
CW, CH, PAD, NR = 800, 700, 70, 20

def build_matrices(seed, n, k):
    random.seed(seed)
    # 1. Adir
    Adir = [[1 if random.uniform(0, 2.0) * k >= 1.0 else 0 for _ in range(n)] for _ in range(n)]

    # 2. Aundir
    Aundir = [[1 if Adir[i][j] or Adir[j][i] else 0 for j in range(n)] for i in range(n)]

    # 3. Матриця B 
    random.seed(seed)
    B = [[random.uniform(0, 2.0) for _ in range(n)] for _ in range(n)]

    # 4. Матриці C, D, H, Tr, Wt, W
    C = [[math.ceil(B[i][j] * 100 * Aundir[i][j]) for j in range(n)] for i in range(n)]
    D = [[1 if C[i][j] > 0 else 0 for j in range(n)] for i in range(n)]
    H = [[1 if D[i][j] != D[j][i] else 0 for j in range(n)] for i in range(n)]
    Tr = [[1 if i < j else 0 for j in range(n)] for i in range(n)]
    Wt = [[(D[i][j] + H[i][j] * Tr[i][j]) * C[i][j] for j in range(n)] for i in range(n)]
    
    # Фінальна симетрична матриця ваг W
    W = [[Wt[i][j] if Wt[i][j] > 0 else Wt[j][i] for j in range(n)] for i in range(n)]
    
    return Aundir, W

# ── Крок 2. Алгоритм Пріма 
def prim_gen(W, n):
    start_node = 0
    for i in range(n):
        if any(W[i][j] > 0 for j in range(n)):
            start_node = i
            break

    vis = {start_node}
    mst = []
    heap = [(W[start_node][u], start_node, u) for u in range(n) if W[start_node][u] > 0]
    heapq.heapify(heap)
    
    yield frozenset(vis), [], None  

    while heap and len(mst) < n - 1:
        w, u, v = heapq.heappop(heap)
        if v in vis:
            continue
            
        vis.add(v)
        mst.append((u, v, w))
        
        for x in range(n):
            if W[v][x] > 0 and x not in vis:
                heapq.heappush(heap, (W[v][x], v, x))
                
        yield frozenset(vis), list(mst), (u, v, w)

# ── Координати вершин 
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

# ── Перемалювання Графа 
def redraw(canvas, Aundir, W, coords, vis, mst_set):
    canvas.delete("all")
    n = len(coords)

    for i in range(n):
        for j in range(i + 1, n):
            if not Aundir[i][j]:
                continue
            x1, y1 = coords[i]
            x2, y2 = coords[j]
            in_mst = (i, j) in mst_set or (j, i) in mst_set
            
            canvas.create_line(x1, y1, x2, y2,
                               fill='#D32F2F' if in_mst else '#E0E0E0',
                               width=4 if in_mst else 1)

            mx, my = (x1+x2)/2, (y1+y2)/2
            dx, dy = x2-x1, y2-y1
            d = math.hypot(dx, dy)
            ox, oy = (-dy/d * 12, dx/d * 12) if d > 0 else (0, -12)
            
            canvas.create_rectangle(mx + ox - 10, my + oy - 7, mx + ox + 10, my + oy + 7, fill="white", outline="white")
            canvas.create_text(mx + ox, my + oy, text=str(W[i][j]), font=('Arial', 9, 'bold'), fill='#1565C0')

    for i, (x, y) in enumerate(coords):
        canvas.create_oval(x-NR, y-NR, x+NR, y+NR,
                           fill='#81C784' if i in vis else 'white',
                           outline='#333333', width=2)
        canvas.create_text(x, y, text=str(i+1), font=('Arial', 12, 'bold'))

# ── ГОЛОВНА ФУНКЦІЯ 
def main():
    Aundir, W = build_matrices(SEED, N, K)
    coords = tri_coords(N, CW, CH, PAD)

    print(f"=== ЛАБОРАТОРНА РОБОТА №6 (Вар {SEED}, k={K}) ===")
    print("\nМатриця суміжності Aundir:")
    for r in Aundir: print(" ".join(map(str, r)))

    print("\nМатриця ваг W:")
    for r in W: print(" ".join(f"{x:3d}" for x in r))

    gen_full = prim_gen(W, N)
    final_mst = []
    for _, mst_f, _ in gen_full:
        final_mst = mst_f
        
    total = sum(e[2] for e in final_mst)
    print("\nРебра мінімального кістяка (MST):")
    for u, v, w in final_mst:
        print(f"  Вершина {u+1:2d} <---> Вершина {v+1:2d}  (вага: {w})")
    print(f"\n>>> СУМА ВАГ МІНІМАЛЬНОГО КІСТЯКА: {total} <<<")

    # --- Графічний інтерфейс ---
    root = tk.Tk()
    root.title(f"ЛР6: Мінімальний кістяк (Алгоритм Пріма) - Вар {SEED}")
    root.geometry("800x850")
    root.resizable(False, False)

    canvas = tk.Canvas(root, width=CW, height=CH, bg='white')
    canvas.pack(pady=10)

    info = tk.StringVar(value="Натисніть кнопку, щоб почати алгоритм Пріма")
    tk.Label(root, textvariable=info, font=('Arial', 12, 'bold'), fg='#333333').pack(pady=5)

    gen = prim_gen(W, N)
    redraw(canvas, Aundir, W, coords, set(), set())

    def step():
        try:
            vis, mst, edge = next(gen)
            mst_set = {(min(u, v), max(u, v)) for u, v, _ in mst}
            redraw(canvas, Aundir, W, coords, vis, mst_set)
            
            cur_weight = sum(e[2] for e in mst)
            
            if edge is None:
                info.set("Початкова вершина додана. Очікування вибору першого ребра...")
            elif len(mst) == N - 1:
                info.set(f"✅ MST побудовано! Загальна сума ваг: {cur_weight}")
                btn.config(state='disabled', bg='#9E9E9E')
            else:
                info.set(f"Додано ребро ({edge[0]+1} - {edge[1]+1}) з вагою {edge[2]}  |  Поточна сума: {cur_weight}")
        except StopIteration:
            pass

    btn = tk.Button(root, text="▶ НАСТУПНИЙ КРОК АЛГОРИТМУ", font=('Arial', 14, 'bold'), 
                    bg='#FF9800', fg='white', activebackground='#F57C00', width=30, pady=8, command=step)
    btn.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()