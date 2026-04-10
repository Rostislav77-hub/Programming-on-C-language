#include <stdio.h>

int main() {
    int x, y;

    printf("Enter integer value x: ");
    scanf("%d", &x);

    if (x > -10) {
        if (x <= -5) {
            // First region: (-10, -5]
            y = x * 3 - 6;
            printf("y = %d\n", y);
        } else {
            if (x > 5) {
                if (x <= 15) {
                    // Second region: (5, 15]
                    y = x * 3 - 6;
                    printf("y = %d\n", y);
                } else {
                    if (x >= 25) {
                        // Third region: [25, ∞)
                        y = 3 * x + 2;
                        printf("y = %d\n", y);
                    } else {
                        printf("Function is undefined for x = %d\n", x);
                    }
                }
            } 
            else {
                printf("Function is undefined for x = %d\n", x);
            }
        }
    } else {
        printf("Function is undefined for x = %d\n", x);
    }

    return 0;
}