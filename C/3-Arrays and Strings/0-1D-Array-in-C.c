#include <stdio.h>

int main() {

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int n,sum=0;
    scanf("%d\n", &n);
    int array[n];
    

    for (int i = 0; i <n; i++)
    {
        //taking input in array and adding into sum
        scanf("%d", &array[i]);
        sum += array[i];
    }

    printf("%d", sum);

    return 0;
}