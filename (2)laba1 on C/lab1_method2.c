#include <stdio.h>
#include <math.h> 

typedef struct {
    double term;  
    double sum;    
} ResultStruct;

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

static ResultStruct calc_recursive_return(double x, double x2, int i)
{
    if (i == 1) {
        ResultStruct base = { .term = x, .sum = x };
        return base;
    }

    ResultStruct prev = calc_recursive_return(x, x2, i - 1);

    double new_term = -prev.term * x2 * (2.0 * i - 3.0) / (2.0 * i - 1.0);

    ResultStruct result = { .term = new_term, .sum = prev.sum + new_term };
    return result;
}

double calc_recursive_return_wrapper(double x, int n)
{
    double x2 = x * x;
    ResultStruct res = calc_recursive_return(x, x2, n);
    return res.sum;
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

    double res_cyclic  = calc_cyclic(x, n);
    double res_ret_rec = calc_recursive_return_wrapper(x, n); 
    double res_exact   = atan(x);                             

    printf("\nРезультати для x = %.6f, n = %d членів ряду:\n", x, n);
    printf("  Циклічна функція              : %.15f\n", res_cyclic);
    printf("  Рекурсія на поверненні        : %.15f\n", res_ret_rec);
    printf("  atan(x) з math.h (еталон)     : %.15f\n", res_exact);

    printf("\nПохибки:\n");
    printf("  |циклічна      - atan|  : %.2e\n", fabs(res_cyclic  - res_exact));
    printf("  |рекурс. пов.  - atan|  : %.2e\n", fabs(res_ret_rec - res_exact));

    return 0;
}