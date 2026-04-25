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

---
