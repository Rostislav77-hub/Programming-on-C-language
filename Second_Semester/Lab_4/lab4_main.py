import random, math, tkinter as tk

SEED, N, K1, K2 = 5515, 11, 0.64, 0.70
NODE_R, W, H = 22, 800, 760

def gen(seed, n, k):
    random.seed(seed)
    return [[1 if random.uniform(0,2.0)*k >= 1.0 else 0 for _ in range(n)] for _ in range(n)]

def undir(A, n):
    B = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if A[i][j] or A[j][i]: B[i][j] = B[j][i] = 1
    return B

def out_deg(A, n): return [sum(A[i]) for i in range(n)]
def in_deg(A, n):  return [sum(A[r][j] for r in range(n)) for j in range(n)]
def deg(A, n):     return [sum(A[i]) for i in range(n)]

def matmul(A, B, n):
    C = [[0]*n for _ in range(n)]
    for i in range(n):
        for k in range(n):
            if not A[i][k]: continue
            for j in range(n): C[i][j] += A[i][k]*B[k][j]
    return C

def paths2(A, n):
    A2 = matmul(A, A, n)
    p = [(i+1,m+1,j+1) for i in range(n) for j in range(n) if A2[i][j]
         for m in range(n) if A[i][m] and A[m][j]]
    return A2, p

def paths3(A, A2, n):
    A3 = matmul(A2, A, n)
    p = [(i+1,m1+1,m2+1,j+1) for i in range(n) for j in range(n) if A3[i][j]
         for m1 in range(n) if A[i][m1]
         for m2 in range(n) if A[m1][m2] and A[m2][j]]
    return A3, p

def warshall(A, n):
    R = [r[:] for r in A]
    for i in range(n): R[i][i] = 1
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if R[i][k] and R[k][j]: R[i][j] = 1
    return R

def strong_mat(R, n):
    return [[1 if R[i][j] and R[j][i] else 0 for j in range(n)] for i in range(n)]

def find_sccs(T, n):
    vis, sccs = [False]*n, []
    for i in range(n):
        if not vis[i]:
            c = [j for j in range(n) if T[i][j]]
            sccs.append([v+1 for v in c])
            for v in c: vis[v] = True
    return sccs

def condensation(A, sccs, n):
    m = len(sccs)
    cid = {v-1:idx for idx,c in enumerate(sccs) for v in c}
    C = [[0]*m for _ in range(m)]
    for i in range(n):
        for j in range(n):
            if A[i][j] and cid[i]!=cid[j]: C[cid[i]][cid[j]] = 1
    return C

def pmat(label, M):
    print(f"\n{label}")
    for r in M: print(" ".join(map(str,r)))

def print_all(A1, Au, A2, R, T, sccs, C, p2, p3, n):
    print("\n=== ЗАВДАННЯ 1 (k=0.64) ===")
    pmat("Adir:", A1); pmat("Aundir:", Au)
    d = deg(Au, n); do = out_deg(A1,n); di = in_deg(A1,n)
    print("\nСтепені ненапрямленого:", d)
    print("Напівстепені напрямленого:")

    for i in range(n): print(f"  в{i+1}: out={do[i]} in={di[i]}")
    print("Регулярний:", len(set(d))==1, f"(ступінь={d[0]})" if len(set(d))==1 else "")
    print("Ізольовані:", [i+1 for i,v in enumerate(d) if v==0] or "немає")
    print("Висячі:",     [i+1 for i,v in enumerate(d) if v==1] or "немає")
    print("\n=== ЗАВДАННЯ 2 (k=0.70) ===")
    pmat("Adir_2:", A2)
    do2=out_deg(A2,n); di2=in_deg(A2,n)
    print("Напівстепені:")

    for i in range(n): print(f"  в{i+1}: out={do2[i]} in={di2[i]}")
    print(f"\nШляхи довжини 2 ({len(p2)} шт.):")

    for p in p2: print("  "+" → ".join(map(str,p)))
    print(f"\nШляхи довжини 3 ({len(p3)} шт.):")

    for p in p3: print("  "+" → ".join(map(str,p)))
    pmat("Матриця досяжності R:", R)
    pmat("Матриця сильної зв'язності T:", T)
    print("\nКСС:")

    for i,c in enumerate(sccs): print(f"  КСС {i+1}: {c}")
    pmat("Граф конденсації C:", C)

def tri_layout(n, cx, cy, r):
    a0 = -math.pi/2
    vx = [cx+r*math.cos(a0+2*math.pi*k/3) for k in range(3)]
    vy = [cy+r*math.sin(a0+2*math.pi*k/3) for k in range(3)]
    pts = []
    for i in range(n):
        t=i/n; s=t*3; e=int(s); f=s-e; ne=(e+1)%3
        pts.append((vx[e]+(vx[ne]-vx[e])*f, vy[e]+(vy[ne]-vy[e])*f))
    return pts

def circle_layout(n, cx, cy, r):
    return [(cx+r*math.cos(-math.pi/2+2*math.pi*i/n),
             cy+r*math.sin(-math.pi/2+2*math.pi*i/n)) for i in range(n)]

def ctrl(x1,y1,x2,y2,off):
    dx,dy=x2-x1,y2-y1; d=math.hypot(dx,dy)
    if d<1e-6: return x1,y1
    return (x1+x2)/2-dy/d*off, (y1+y2)/2+dx/d*off

def edgept(bx,by,cx,cy,r):
    dx,dy=cx-bx,cy-by; d=math.hypot(dx,dy)
    if d<1e-6: return cx,cy
    return cx-dx/d*r, cy-dy/d*r

def arc_arrow(cv,x1,y1,x2,y2,off,col="black"):
    bx,by=ctrl(x1,y1,x2,y2,off)
    sx,sy=edgept(bx,by,x1,y1,NODE_R); ex,ey=edgept(bx,by,x2,y2,NODE_R)
    cv.create_line(sx,sy,bx,by,ex,ey,smooth=True,arrow=tk.LAST,arrowshape=(12,16,4),fill=col,width=1.5)

def arc_edge(cv,x1,y1,x2,y2,off):
    bx,by=ctrl(x1,y1,x2,y2,off)
    cv.create_line(x1,y1,bx,by,x2,y2,smooth=True,fill="gray30",width=1.5)

def loop(cv,x,y,directed=True):
    lx,ly=x,y-NODE_R
    cv.create_line(lx,ly,lx-24,ly-46,lx,ly-72,lx+24,ly-46,lx,ly,
                   smooth=True,arrow=tk.LAST if directed else tk.NONE,
                   arrowshape=(10,14,4),fill="black",width=1.5)

def node(cv,x,y,lbl,fill="lightblue"):
    cv.create_oval(x-NODE_R,y-NODE_R,x+NODE_R,y+NODE_R,fill=fill,outline="black",width=2)
    cv.create_text(x,y,text=str(lbl),font=("Arial",10,"bold"))

def draw_dir(cv,coords,A,title,nc="lightblue"):
    cv.delete("all"); n=len(coords)
    cv.create_text(W//2,22,text=title,font=("Arial",13,"bold"),fill="#1a237e")
    for i in range(n):
        for j in range(n):
            if not A[i][j]: continue
            x1,y1=coords[i]; x2,y2=coords[j]
            if i==j: loop(cv,x1,y1); continue
            arc_arrow(cv,x1,y1,x2,y2,38 if A[j][i] else 14)
    for i,(x,y) in enumerate(coords): node(cv,x,y,i+1,fill=nc)

def draw_undir(cv,coords,A,title):
    cv.delete("all"); n=len(coords)
    cv.create_text(W//2,22,text=title,font=("Arial",13,"bold"),fill="#1a237e")
    for i in range(n):
        for j in range(i+1,n):
            if A[i][j]: arc_edge(cv,*coords[i],*coords[j],14)
    for i,(x,y) in enumerate(coords): node(cv,x,y,i+1,fill="lightyellow")

def draw_cond(cv,sccs,C,title):
    cv.delete("all"); m=len(sccs)
    cv.create_text(W//2,22,text=title,font=("Arial",13,"bold"),fill="#1a237e")
    coords=circle_layout(m,W//2,H//2+10,max(90,min(260,m*38)))
    for i in range(m):
        for j in range(m):
            if C[i][j]: arc_arrow(cv,*coords[i],*coords[j],38 if C[j][i] else 14,col="#0d47a1")
    for i,(x,y) in enumerate(coords):
        r=max(34,24+len(sccs[i])*5)
        cv.create_oval(x-r,y-r,x+r,y+r,fill="#c8e6c9",outline="#2e7d32",width=2)
        cv.create_text(x,y,text=f"КСС {i+1}\n{{{', '.join(map(str,sccs[i]))}}}",
                       font=("Arial",8,"bold"),justify=tk.CENTER)

def main():
    A1=gen(SEED,N,K1); Au=undir(A1,N)
    A2=gen(SEED,N,K2); A2s,p2=paths2(A2,N); _,p3=paths3(A2,A2s,N)
    R=warshall(A2,N); T=strong_mat(R,N); sccs=find_sccs(T,N); C=condensation(A2,sccs,N)

    print_all(A1,Au,A2,R,T,sccs,C,p2,p3,N)

    root=tk.Tk(); root.title("ЛР 4 — Варіант 5515"); root.resizable(False,False)
    cv=tk.Canvas(root,width=W,height=H,bg="white"); cv.pack(padx=10,pady=(10,0))
    coords=tri_layout(N,W//2,H//2+20,295)

    steps=[
        ("Крок 1/4 — Напрямлений граф 1 (k=0.64)",  lambda: draw_dir(cv,coords,A1,"Напрямлений граф 1 (k=0.64)")),
        ("Крок 2/4 — Ненапрямлений граф 1",          lambda: draw_undir(cv,coords,Au,"Ненапрямлений граф 1")),
        ("Крок 3/4 — Напрямлений граф 2 (k=0.70)",   lambda: draw_dir(cv,coords,A2,"Напрямлений граф 2 (k=0.70)",nc="#e8eaf6")),
        ("Крок 4/4 — Граф конденсації",               lambda: draw_cond(cv,sccs,C,"Граф конденсації")),
    ]

    idx=[0]; lbl=tk.StringVar(value=steps[0][0])
    bot=tk.Frame(root); bot.pack(fill=tk.X,padx=10,pady=6)
    tk.Label(bot,textvariable=lbl,font=("Arial",11),fg="#1a237e").pack(side=tk.LEFT,padx=8)

    def nxt():
        idx[0]=(idx[0]+1)%len(steps); lbl.set(steps[idx[0]][0]); steps[idx[0]][1]()

    tk.Button(bot,text="▶  Наступний крок",font=("Arial",11,"bold"),
              bg="#1565c0",fg="white",relief=tk.FLAT,padx=18,pady=6,command=nxt).pack(side=tk.RIGHT,padx=8)

    steps[0][1](); root.mainloop()

if __name__=="__main__": main()