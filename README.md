# 🚀 First Semester (Programming Basics in C)

This repository contains the foundational programming labs from the First Semester, covering basic algorithms, control structures, loops, dynamic programming, and matrix operations implemented strictly in **C**.

---

## 📌 Completed works:

### 🔷 [Lab_0] Branching Algorithms & Boolean Logic

Exploring conditional statements and boolean algebra. The task involves evaluating a piecewise continuous function $y(x)$ based on specific domain conditions (Variant 15). The solution is implemented using two distinct approaches to compare syntax and execution.

🛠 **Tech Stack & Highlights:**
* **Control Flow Mastery:** Designed a deeply nested `if-else` tree to map mathematical intervals strictly using singular comparison operators.
* **Boolean Optimization:** Refactored the nested logic into a flattened, readable structure using logical operators (`&&`, `||`).
* **State Management:** Implemented a state flag (`isDefined`) to decouple the mathematical computation logic from the output/rendering phase.
* **Edge Case Handling:** Robustly managing undefined mathematical domains and providing clear user feedback.

* 📁 **Structure:** `First_Semester/Lab_0/` (solution source code).
* ▶️ **Running tests:** `cd First_Semester/Lab_0 && gcc main.c -o main && ./main`

<br>

### 🔷 [Lab_1] Test Environment & Series Approximation

Introductory task used to verify the working environment, compiler setup, and basic syntax execution. Beyond simple setup, this lab includes a fundamental algorithmic implementation: calculating a power series approximation using a `for` loop.

🛠 **Tech Stack & Highlights:**
* **Algorithmic Efficiency:** Calculates the sum of the first $n$ terms of a mathematical series. The logic optimizes the computation by iteratively updating the numerator (`numerator *= step_x`) rather than recalculating powers from scratch on every iteration.
* **Floating-point Arithmetic:** Safe handling of `double` precision variables for fractional accumulation.

* 📁 **Structure:** `First_Semester/Lab_1/` (solution source code).
* ▶️ **Running tests:** `cd First_Semester/Lab_1 && gcc main.c -o main && ./main`

<br>

### 🔷 [Lab_2] Nested Loops and Dynamic Programming

Studying cyclic control structures, nested loops, and the dynamic programming method. The objective is to compute a mathematical sequence (Variant 15) featuring a sum and a nested product:

$$S = \sum_{i=1}^{n} \frac{\sin(i) + 2}{i + \prod_{j=1}^{i} \sin(j)}$$

🛠 **Tech Stack & Highlights:**
* **Algorithmic Optimization (Memoization):** Successfully reduced time complexity from $O(n^2)$ to $O(n)$ by caching the cumulative product state (`product *= sin_val`) instead of recalculating it iteratively.
* **Empirical Profiling:** Designed custom performance counters (`operations`, `sin_calls`) to track mathematical workload and empirically prove the exact efficiency gains of the optimized algorithm.
* **Precision Arithmetic:** Handled floating-point accumulation safely while utilizing standard C math libraries (`<math.h>`).

* 📁 **Structure:** `First_Semester/Lab_2/` (solution source code).
* ▶️ **Running tests:** `cd First_Semester/Lab_2 && gcc main.c -lm -o main && ./main`

<br>

### 🔷 [Lab_3] 2D Array Traversal & Terminal Animation

Exploring methods for navigating and manipulating two-dimensional arrays (matrices). This lab emphasizes visual algorithm execution using console screen coordinates, simulating a matrix environment. The core task involves implementing a dual-traversal zig-zag pattern (Variant 15).

🛠 **Tech Stack & Highlights:**
* **Console UI & ANSI Escape Codes:** Engineered a custom `gotoxy` equivalent using ANSI escape sequences (`\033[%d;%dH`) for raw cursor manipulation without external libraries like `ncurses`.
* **Real-time Animation:** Utilized `usleep()` and explicit buffer flushing (`fflush(stdout)`) to render a smooth, frame-by-frame animation of the traversal process directly in the terminal.
* **UX Enhancements:** Implemented cursor hiding (`\033[?25l`) and terminal clearing for a clean canvas, alongside text color inversion (`\033[7m`) to visually highlight the "active" leading step of the traversal.
* **Dual-Pointer Logic:** Designed a synchronized loop structure where two independent "pointers" (top and bottom rows) traverse the grid simultaneously in a zig-zag snake pattern until they converge.

* 📁 **Structure:** `First_Semester/Lab_3/` (solution source code).
* ▶️ **Running tests:** `cd First_Semester/Lab_3 && gcc main.c -o main && ./main`

<br>

### 🔷 [Lab_4] Binary Search Algorithms in Matrices

Exploring search algorithms, specifically the implementation of Binary Search within two-dimensional arrays. The objective is to efficiently locate a specific real number $X$ within a dynamically generated matrix $A[m][n]$. Based on Variant 15, the task focuses on applying Binary Search exclusively to the **last row** and the **first column**.

🛠 **Tech Stack & Highlights:**
* **Data Preconditioning:** Implemented targeted sorting algorithms (Bubble Sort) to independently arrange the first column and last row, establishing the mandatory sorted preconditions for binary search.
* **Dimensional Binary Search ($O(\log n)$):** Engineered two distinct binary search functions to traverse memory both vertically (`searchCol`) and horizontally (`searchRow`) within the 2D array structure.
* **Edge Case Resolution:** Developed logic to handle intersection overlaps (e.g., the bottom-left corner) to prevent duplicate coordinate reporting during the search.
* **Interactive CLI:** Built a continuous execution loop allowing the user to perform multiple searches on the generated matrix without restarting the application.

* 📁 **Structure:** `First_Semester/Lab_4/` (solution source code).
* ▶️ **Running tests:** `cd First_Semester/Lab_4 && gcc main.c -o main && ./main`

<br>

### 🔷 [Lab_5] In-Place Sorting Algorithms in 2D Arrays

Deep dive into sorting algorithms applied directly within two-dimensional arrays. A core constraint of this lab is performing the sort strictly "in-place", meaning no auxiliary arrays or additional data structures can be allocated. The objective (Variant 15) is to extract and sort the elements located exclusively on the **secondary diagonal** (anti-diagonal) of a square matrix using the **Insertion Sort** algorithm.

🛠 **Tech Stack & Highlights:**
* **Advanced Index Math:** Adapted the standard 1D Insertion Sort algorithm to operate directly across the cross-section of a 2D matrix (`arr[i][N - 1 - i]`), achieving true $O(1)$ auxiliary space complexity.
* **Algorithmic Rigor (Edge Testing):** Engineered a comprehensive test suite to validate algorithmic stability across $O(n)$ Best Case (already sorted), $O(n^2)$ Worst Case (reverse sorted), and Average Case (randomly distributed) scenarios.
* **Console Visualization:** Developed a custom matrix rendering function that structurally formats the grid and visually highlights `[ ]` the targeted anti-diagonal elements for clear debugging and demonstration.

* 📁 **Structure:** `First_Semester/Lab_5/` (solution source code).
* ▶️ **Running tests:** `cd First_Semester/Lab_5 && gcc main.c -o main && ./main`

---
*End of First Semester.*

# 🚀 Second Semester (Advanced Data Structures & Graph Theory)

This repository contains the advanced programming labs from the Second Semester. The curriculum demonstrates a deliberate progression: starting with low-level memory management and recursion in **C**, and transitioning to high-level graph theory algorithms and GUI development in **Python**.

---

## 📌 Completed works:

### 🔷 [Lab_1] Recursive Algorithms & Error Analysis (C)

Exploration of recursive function execution using the call stack. The objective is to compute the Taylor series expansion for the mathematical function $\arctan(x)$ (Variant 15).

🛠 **Tech Stack & Highlights:**
* **Recursion Mechanics:** Implemented three distinct recursive paradigms: calculation strictly on the descent (tail recursion), strictly on the return, and a hybrid approach (descent/return splitting).
* **Mathematical Precision:** Computed approximations and mapped the computational error against a dynamically generated baseline.
* **Memory Constraints:** Strictly controlled variable scope and wrapper functions to prevent stack overflow and memory leaks during deep recursive calls.

* 📁 **Structure:** `Second_Semester/Lab_1/`

<br>

### 🔷 [Lab_2] Dynamic Data Structures: Linked Lists (C)

Advanced manipulation of dynamic memory via Linked Lists. The task (Variant 15) requires reordering a sequence of real numbers into an alternating "accordion" pattern: $a_1, a_n, a_2, a_{n-1}...$

🛠 **Tech Stack & Highlights:**
* **Pointer Arithmetic & Manipulation:** Handled node rewiring and list traversal without relying on a pre-calculated `length` variable, forcing dynamic runtime evaluation.
* **Memory Safety:** Strictly utilized `malloc` and `free` to prevent memory leaks while rearranging the data structure entirely *in-place*.
* **Algorithm Complexity:** Achieved the reordering logic under strict constraints, minimizing read/write operations compared to standard array manipulation.

* 📁 **Structure:** `Second_Semester/Lab_2/`

<br>

### 🔷 [Lab_3] Graph Generation & GUI Visualization (Python)

Transitioning to Python and GUI development to represent discrete mathematics visually. The lab focuses on generating Directed and Undirected graphs based on a deterministic seed and rendering them from scratch.

🛠 **Tech Stack & Highlights:**
* **Algorithmic Graph Generation:** Designed a custom adjacency matrix generator applying specific algebraic thresholds ($k$-filters) based on randomized matrices.
* **Raw GUI Rendering:** Built a visualizer using standard GUI libraries (`tkinter`) without relying on specialized graph frameworks like `networkx`.
* **Geometry Math:** Implemented trigonometric positioning to dynamically arrange nodes in specific geometric patterns and utilized Bezier curves to render overlapping directed edges cleanly.

* 📁 **Structure:** `Second_Semester/Lab_3/`

<br>

### 🔷 [Lab_4] Graph Characteristics, Reachability & Condensation (Python)

Deep algorithmic analysis of graph structures. The objective is to compute fundamental properties, find specific paths, and simplify complex cyclic graphs into their Condensation Graphs.

🛠 **Tech Stack & Highlights:**
* **Matrix Operations:** Utilized matrix multiplication ($A^2, A^3$) to programmatically discover all exact paths of length 2 and 3.
* **Transitive Closure:** Implemented algorithms to calculate the reachability matrix and identify Strongly Connected Components (SCCs).
* **Graph Condensation:** Engineered logic to collapse calculated SCCs into super-nodes and generate/visualize the resulting acyclic Condensation Graph.

* 📁 **Structure:** `Second_Semester/Lab_4/`

<br>

### 🔷 [Lab_5] Graph Traversal Algorithms: BFS & DFS (Python)

Implementation of fundamental search algorithms with interactive real-time visualization. The task involves executing Breadth-First Search (BFS) and Depth-First Search (DFS) on a generated directed graph.

🛠 **Tech Stack & Highlights:**
* **Interactive Stepping (Generators):** Utilized Python `yield` generators to decouple the traversal logic from the UI, allowing the user to step through the BFS/DFS execution frame-by-frame via button clicks.
* **Real-time State Representation:** Dynamically updated node colors and edge highlights in the GUI to reflect vertex states (unvisited, discovered, fully explored).
* **Spanning Tree Extraction:** Simultaneously built and rendered the traversal spanning tree (DFS/BFS tree) parallel to the original graph during execution.

* 📁 **Structure:** `Second_Semester/Lab_5/`

<br>

### 🔷 [Lab_6] Minimum Spanning Tree: Prim's Algorithm (Python)

Finding the optimal subgraph configuration using greedy algorithms. This lab focuses on generating a complex weighted undirected graph and computing its Minimum Spanning Tree (MST).

🛠 **Tech Stack & Highlights:**
* **Complex Data Transformation:** Engineered a multi-step algebraic derivation to construct a symmetric weight matrix $W$ from initial randomized boolean arrays and triangular matrices.
* **Dynamic Adjacency Lists:** Transformed the generated matrices into dynamic linked structures (adjacency lists) for optimized algorithmic processing.
* **Prim's Algorithm & Priority Queues:** Implemented Prim's greedy algorithm to find the MST, leveraging Python's `heapq` for highly efficient $O(E \log V)$ minimum weight edge selection.
* **Weighted UI Rendering:** Enhanced the GUI to clearly render edge weights and visually trace the step-by-step growth of the spanning tree across the network.

* 📁 **Structure:** `Second_Semester/Lab_6/`

---
*End of Second Semester. 2025-2026@*
