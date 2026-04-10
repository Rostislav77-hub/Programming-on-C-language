#include <stdio.h>
#include <math.h>

int main() {
    int n;
    printf("Enter n: ");
    scanf("%d", &n);

    double S = 0.0;           
    double sin_val;           
    double product = 1.0;    
    long long operations = 0; 
    long long sin_calls = 0;  

    for (int i = 1; i <= n; i++) {
        sin_val = sin(i);
        sin_calls++;

        
        product *= sin_val;
        operations += 2; 

        double numerator = sin_val + 2.0;
        double denominator = i + product;

        S += numerator / denominator;

        
        operations += 6; 
    }

    printf("S = %.7lf\n", S);
    printf("Number of arithmetic operations: %lld\n", operations);
    printf("Number of sin() calls: %lld\n", sin_calls);

    return 0;
}