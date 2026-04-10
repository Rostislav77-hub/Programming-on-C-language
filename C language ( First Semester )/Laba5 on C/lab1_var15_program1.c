#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define N 8

void printMatrix(int arr[N][N], const char* title) {
    printf("%s\n", title);
    printf("      ");
    for (int j = 0; j < N; j++) printf("Col%d ", j);
    printf("\n");

    for (int i = 0; i < N; i++) {
        printf("Row%d: ", i);
        for (int j = 0; j < N; j++) {
            if (j == N - 1 - i) {
                 printf("[%2d] ", arr[i][j]); 
            } else {
                 printf(" %2d  ", arr[i][j]);
            }
        }
        printf("\n");
    }
    printf("\n");
}

void sortSecondaryDiagonal(int arr[N][N]) {
    for (int i = 1; i < N; i++) {
        int key = arr[i][N - 1 - i];
        int j = i - 1;

        while (j >= 0 && arr[j][N - 1 - j] > key) {
            arr[j + 1][N - 1 - (j + 1)] = arr[j][N - 1 - j];
            j = j - 1;
        }
        arr[j + 1][N - 1 - (j + 1)] = key;
    }
}

void runTestRandom() {
    int matrix[N][N];
    for (int i = 0; i < N; i++) 
        for (int j = 0; j < N; j++) 
            matrix[i][j] = rand() % 50; 

    printf("=== TEST 1: RANDOM ELEMENTS ===\n");
    printMatrix(matrix, "Before Sorting:");
    sortSecondaryDiagonal(matrix);
    printMatrix(matrix, "After Sorting:");
    printf("----------------------------------------------------\n\n");
}

void runTestReverse() {
    int matrix[N][N];
    for (int i = 0; i < N; i++) 
        for (int j = 0; j < N; j++) 
            matrix[i][j] = 0; 

    int val = 80;
    for (int i = 0; i < N; i++) {
        matrix[i][N - 1 - i] = val;
        val -= 10;
    }

    printf("=== TEST 2: REVERSE ORDER (Worst Case) ===\n");
    printMatrix(matrix, "Before Sorting (Descending):");
    sortSecondaryDiagonal(matrix);
    printMatrix(matrix, "After Sorting (Ascending):");
    printf("----------------------------------------------------\n\n");
}

void runTestSorted() {
    int matrix[N][N];
    for (int i = 0; i < N; i++) 
        for (int j = 0; j < N; j++) 
            matrix[i][j] = 0; 

    int val = 10;
    for (int i = 0; i < N; i++) {
        matrix[i][N - 1 - i] = val;
        val += 10;
    }

    printf("=== TEST 3: ALREADY SORTED (Best Case) ===\n");
    printMatrix(matrix, "Before Sorting:");
    sortSecondaryDiagonal(matrix);
    printMatrix(matrix, "After Sorting (Should be same):");
    printf("----------------------------------------------------\n\n");
}

int main() {
    srand(time(NULL));
    
    runTestRandom();
    runTestReverse();
    runTestSorted();

    return 0;
}