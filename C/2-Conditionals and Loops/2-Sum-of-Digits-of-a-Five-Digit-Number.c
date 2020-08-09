#include <stdio.h>


int main() {
	
    int n, sum=0, rem;
    scanf("%d", &n);
    //Complete the code to calculate the sum of the five digits on n.

    while (n!=0)
    {
      rem= n%10;  //dividing by to get remender
      sum += rem;   // adding remender into sum
      n =n/10;      //actual dividing
    }

    printf("%d", sum);
    
    return 0;
}