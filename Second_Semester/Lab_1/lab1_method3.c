#include <stdio.h>
#include <math.h>

double calc_cyclic(double x, int n)
{
    double x2 = x * x;
    double term = x;
    double sum = x;

    for (int i = 1; i < n; i++) {
        term = -term * x2 * (2.0 * i - 1.0) / (2.0 * i + 1.0);
        sum += term;
    }

    return sum;
}

static double calc_recursive_mixed(double x2, double term, int i, int n)
{
    if (i == n) {
        return term;
    }

    double next_term = -term * x2 * (2.0 * i - 1.0) / (2.0 * i + 1.0);
    double sum_from_next = calc_recursive_mixed(x2, next_term, i + 1, n);

    return term + sum_from_next;
}

double calc_recursive_mixed_wrapper(double x, int n)
{
    double x2 = x * x;
    return calc_recursive_mixed(x2, x, 1, n);
}

int main(void)
{
    double x;
    int n;

    printf("Введіть x (умова: |x| < 1): ");
    if (scanf("%lf", &x) != 1) {
        fprintf(stderr, "Помилка: неправильний формат вводу.\n");
        return 1;
    }
    if (fabs(x) >= 1.0) {
        fprintf(stderr, "Помилка: |x| має бути строго менше 1.\n");
        return 1;
    }

    printf("Введіть n (кількість членів ряду, n >= 1): ");
    if (scanf("%d", &n) != 1 || n < 1) {
        fprintf(stderr, "Помилка: n має бути цілим числом >= 1.\n");
        return 1;
    }

    double res_cyclic = calc_cyclic(x, n);
    double res_mixed  = calc_recursive_mixed_wrapper(x, n);
    double res_exact  = atan(x);

    printf("\nРезультати для x = %.6f, n = %d членів ряду:\n", x, n);
    printf("  Циклічна функція              : %.15f\n", res_cyclic);
    printf("  Змішана рекурсія              : %.15f\n", res_mixed);
    printf("  atan(x) з math.h (еталон)     : %.15f\n", res_exact);

    printf("\nПохибки:\n");
    printf("  |циклічна      - atan|  : %.2e\n", fabs(res_cyclic - res_exact));
    printf("  |змішана рекур - atan|  : %.2e\n", fabs(res_mixed  - res_exact));

    return 0;
}