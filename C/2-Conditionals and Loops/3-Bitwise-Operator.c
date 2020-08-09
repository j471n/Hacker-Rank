#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
//Complete the following function.


void calculate_the_maximum(int n, int k) {
  //Write your code here.
  int a,b;
    int maxAND =0;
    int maxOR =0;
    int maxXOR =0;

    for (a=1;a<n;a++)
    {
        for (b=n;b>a;b--)
        {   
            //cheking that a&b should always less than k and it should alwasys greater thatn variable
            if ((a&b)<k && (a&b)>maxAND) {
                maxAND = a&b;
            }
            if ((a|b)<k && (a|b)>maxOR) {
                maxOR = a|b;
            }
            if ((a^b)<k && (a^b)>maxXOR) {
                maxXOR = a^b;
            }
        }
    }

    printf("%d\n", maxAND);
    printf("%d\n", maxOR);
    printf("%d\n", maxXOR);

}

int main() {
    int n, k;
  
    scanf("%d %d", &n, &k);
    calculate_the_maximum(n, k);
 
    return 0;
}
