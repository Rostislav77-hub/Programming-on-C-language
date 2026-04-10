#include <stdio.h>
#include <math.h> 

double calc_cyclic(double x, int n)
{
    double x2   = x * x; 
    double term = x;       
    double sum  = x;      

    for (int i = 1; i < n; i++) {
        term = -term * x2 * (2.0 * i - 1.0) / (2.0 * i + 1.0);
        sum += term;
    }

    return sum;
}

static double calc_recursive_helper(double x2, double term,
                                    double sum, int i, int n)
{
    if (i >= n)
        return sum;
    
    double next_term = -term * x2 * (2.0 * i - 1.0) / (2.0 * i + 1.0);
    double next_sum  = sum + next_term;

    return calc_recursive_helper(x2, next_term, next_sum, i + 1, n);
}

double calc_recursive(double x, int n)
{
    double x2  = x * x; 
    double f1  = x;                                                 
    return calc_recursive_helper(x2, f1, f1, 1, n);
}

int main(void)
{
    double x;
    int    n;

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

    double res_cyclic    = calc_cyclic(x, n);
    double res_recursive = calc_recursive(x, n);
    double res_exact     = atan(x);          

    printf("\nРезультати для x = %.6f, n = %d членів ряду:\n", x, n);
    printf("  Циклічна функція : %.15f\n", res_cyclic);
    printf("  Рекурсивна функція : %.15f\n", res_recursive);
    printf("  atan(x) з math.h   : %.15f\n", res_exact);

    printf("\nПохибки:\n");
    printf("  |циклічна - atan|    : %.2e\n", fabs(res_cyclic    - res_exact));
    printf("  |рекурсивна - atan|  : %.2e\n", fabs(res_recursive - res_exact));

    return 0;
}