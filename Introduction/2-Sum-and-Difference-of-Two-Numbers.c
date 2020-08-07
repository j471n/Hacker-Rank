#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main()
{
	int n1, n2;
    float f1, f2;

     scanf("%d %d", &n1, &n2);
     scanf("%f %f", &f1, &f2);

     printf("%d %d\n", n1+n2, n1-n2);
     // .lf is using to print the digits after .(decimal) e.g. 2.1 if ther was .2f then outpul will be like 2.09 
     printf("%.1f %.1f", f1+f2, f1-f2);
    
    return 0;
}
