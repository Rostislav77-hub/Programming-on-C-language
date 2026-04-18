import random
import math
import tkinter as tk

def generate_matrices(seed, n, k):
    random.seed(seed)
    
    A_dir = []
    for _ in range(n):
        row = []
        for _ in range(n):
            val = random.uniform(0, 2.0) * k
            row.append(1 if val >= 1.0 else 0)
        A_dir.append(row)
        
    A_undir = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if A_dir[i][j] == 1 or A_dir[j][i] == 1:
                A_undir[i][j] = 1
                A_undir[j][i] = 1
                
    return A_dir, A_undir

def print_matrix(name, matrix):
    print(f"--- Матриця суміжності {name} ---")
    for row in matrix:
        print(" ".join(str(x) for x in row))
    print()

def get_triangle_coords(n, width, height, padding):
    coords = []
    v1 = (width / 2, padding)                  
    v2 = (width - padding, height - padding)   
    v3 = (padding, height - padding)           
    
    for i in range(n):
        t = i / n
        if t < 1/3: 
            f = t * 3
            x = v1[0] + (v2[0] - v1[0]) * f
            y = v1[1] + (v2[1] - v1[1]) * f
        elif t < 2/3: 
            f = (t - 1/3) * 3
            x = v2[0] + (v3[0] - v2[0]) * f
            y = v2[1] + (v3[1] - v2[1]) * f
        else: 
            f = (t - 2/3) * 3
            x = v3[0] + (v1[0] - v3[0]) * f
            y = v3[1] + (v1[1] - v3[1]) * f
        coords.append((x, y))
    return coords

def draw_graph(canvas, coords, matrix, is_directed):
    canvas.delete("all")
    n = len(coords)
    node_r = 20 
    
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                x1, y1 = coords[i]
                x2, y2 = coords[j]
                
                if i == j:
                    canvas.create_oval(x1 - node_r - 20, y1 - node_r - 20, 
                                       x1 - node_r + 10, y1 - node_r + 10, outline="black")
                    continue
                
                is_mutual = is_directed and matrix[j][i] == 1
                
                mx, my = (x1 + x2) / 2, (y1 + y2) / 2
                dx, dy = x2 - x1, y2 - y1
                dist = math.hypot(dx, dy)
                if dist == 0: continue
                
                nx, ny = -dy / dist, dx / dist
                
                offset = 40
                if is_mutual:
                    offset = 40 if i > j else -40 
                elif not is_directed:
                    offset = 30 
                cx, cy = mx + nx * offset, my + ny * offset
                
                d_end = math.hypot(cx - x2, cy - y2)
                if d_end > node_r:
                    end_x = x2 + (cx - x2) / d_end * node_r
                    end_y = y2 + (cy - y2) / d_end * node_r
                else:
                    end_x, end_y = x2, y2

                arrow_opts = tk.LAST if is_directed else tk.NONE
                
                canvas.create_line(x1, y1, cx, cy, end_x, end_y, 
                                   smooth=True, arrow=arrow_opts, arrowshape=(15, 20, 5))

    for i, (x, y) in enumerate(coords):
        canvas.create_oval(x - node_r, y - node_r, x + node_r, y + node_r, fill="white", outline="black", width=2)
        canvas.create_text(x, y, text=str(i + 1), font=("Arial", 12, "bold"))

def main():
    SEED = 5515
    N = 11
    K = 0.705

    A_dir, A_undir = generate_matrices(SEED, N, K)
    print_matrix("Напрямленого графа (Adir)", A_dir)
    print_matrix("Ненапрямленого графа (Aundir)", A_undir)

    root = tk.Tk()
    root.title(f"Графи (Варіант {SEED}) - n={N}, Трикутник")
    
    canvas = tk.Canvas(root, width=800, height=800, bg="white")
    canvas.pack(padx=10, pady=10)
    
    coords = get_triangle_coords(N, 800, 800, 50)
    
    btn_frame = tk.Frame(root)
    btn_frame.pack(pady=5)
    
    tk.Button(btn_frame, text="Напрямлений граф", font=("Arial", 12),
              command=lambda: draw_graph(canvas, coords, A_dir, True)).pack(side=tk.LEFT, padx=10)
    
    tk.Button(btn_frame, text="Ненапрямлений граф", font=("Arial", 12),
              command=lambda: draw_graph(canvas, coords, A_undir, False)).pack(side=tk.LEFT, padx=10)
    
    draw_graph(canvas, coords, A_dir, True)
    
    root.mainloop()

if __name__ == "__main__":
    main()