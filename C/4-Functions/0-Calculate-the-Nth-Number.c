#include <stdio.h>
#include <stdlib.h>
//Complete the following function.

int find_nth_term(int n, int a, int b, int c) {
    //Write your code here.

    int s=a+b+c;
    //checking  that if n is 1 then return 1
    if (n==1) {
        return 1;
    }
    else
    {
          //this is recursion here we are callin again and again untill n became 1, so it can return 1
          return (n-1+ find_nth_term(n-1, s, c, b));
    }

}

int main() {
    int n, a, b, c;

    scanf("%d %d %d %d", &n, &a, &b, &c);
    int ans = find_nth_term(n, a, b, c);

    printf("%d", ans);
    return 0;
}