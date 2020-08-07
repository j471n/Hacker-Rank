#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n;
    scanf("%d", &n);  //taking int to create an array

    int arr[n];       //creating an arrya of size n


    //this is the loop of getting array by user
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &arr[i]);
    }

    //prining the same array in reverse this loop is in the reverse diection 
    /* for example n = 4 so arrya[4] but in the given loop int j = 4-1=3,   means arrya has 3 elements*/
    for (int i = n-1; i >=0; i--){
        printf("%d ", arr[i]);
    }

    return 0;
}