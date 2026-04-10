#include <stdio.h>

int main() {
    double x;
    int n;

    printf("Enter x (|x| < 1): ");
    scanf("%lf", &x);
    printf("Enter n: ");
    scanf("%d", &n);

    double y = 0.0;
    double numerator = -x * x * x;
    double step_x = -x * x;

    for (int i = 1; i <= n; i++) {
        y += numerator / (2 * i + 1);
        numerator *= step_x;
    }

    printf("Result: %.10lf\n", y);

    getchar();
    getchar();

    return 0;
}