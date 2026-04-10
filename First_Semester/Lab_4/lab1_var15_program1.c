#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define ROWS 8
#define COLS 8

void fillAndSort(double arr[ROWS][COLS]) {
    for (int i = 0; i < ROWS; i++) {
        for (int j = 0; j < COLS; j++) {
            arr[i][j] = (double)(rand() % 20 + 1); 
        }
    }

    for (int i = 0; i < ROWS - 1; i++) {
        for (int k = 0; k < ROWS - i - 1; k++) {
            if (arr[k][0] > arr[k + 1][0]) {
                double temp = arr[k][0];
                arr[k][0] = arr[k + 1][0];
                arr[k + 1][0] = temp;
            }
        }
    }

    for (int i = 0; i < COLS - 1; i++) {
        for (int k = 0; k < COLS - i - 1; k++) {
            if (arr[ROWS - 1][k] > arr[ROWS - 1][k + 1]) {
                double temp = arr[ROWS - 1][k];
                arr[ROWS - 1][k] = arr[ROWS - 1][k + 1];
                arr[ROWS - 1][k + 1] = temp;
            }
        }
    }
}

int searchCol(double arr[ROWS][COLS], double target) {
    int left = 0, right = ROWS - 1;
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (arr[mid][0] == target) return mid;
        if (arr[mid][0] < target) left = mid + 1;
        else right = mid - 1;
    }
    return -1;
}

int searchRow(double arr[ROWS][COLS], double target) {
    int left = 0, right = COLS - 1;
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (arr[ROWS - 1][mid] == target) return mid;
        if (arr[ROWS - 1][mid] < target) left = mid + 1;
        else right = mid - 1;
    }
    return -1;
}

int main() {
    srand(time(NULL));
    double matrix[ROWS][COLS];
    double target;

    fillAndSort(matrix);

    printf("Generated matrix:\n      ");
    for(int j=0; j<COLS; j++) printf("Col%d ", j);
    printf("\n");

    for (int i = 0; i < ROWS; i++) {
        printf("Row%d: ", i);
        for (int j = 0; j < COLS; j++) {
            printf("%4.0lf ", matrix[i][j]);
        }
        printf("\n");
    }

    while(1) {
        printf("\nEnter number to search X: ");
        if(scanf("%lf", &target) != 1) break;

        printf("Searching for.... %.0lf...\n", target);
        int found = 0;

        int r = searchCol(matrix, target);
        if (r != -1) {
            printf("Found in Column 0, Row %d\n", r);
            found++;
        }

        int c = searchRow(matrix, target);
        if (c != -1) {
            if (!(c == 0 && r == ROWS - 1)) {
                printf("Found in Column %d, Row %d\n", c, ROWS - 1);
                found++;
            }
        }

        if (found == 0) printf("Not found in First Column or Last Row.\n");
        else printf("Done. Total found: %d\n", found);
    }

    return 0;
}