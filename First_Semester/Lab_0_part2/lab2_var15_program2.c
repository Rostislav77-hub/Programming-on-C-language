#include <stdio.h>

int main() {
    int x, y, isDefined = 0;

    printf("Enter integer value x: ");
    scanf("%d", &x);

    if ((x > -10 && x <= -5) || (x > 5 && x <= 15)) {
        y = 3 * x - 6;
        isDefined = 1;
    } else if (x == -10 || x == 5) {
        y = x;
        isDefined = 1;
    } else if (x >= 25) {
        y = 3 * x + 2; 
        isDefined = 1;
    }

    if (isDefined) {
        printf("y = %d\n", y);
    } else {
        printf("Function is undefined for x = %d\n", x);
    }

    return 0;
}