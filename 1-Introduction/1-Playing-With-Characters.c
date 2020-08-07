#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() 
{

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 

    char ch, s[10], sen[30];
    //getting input from the user
    scanf("%c", &ch); 
    scanf("%s", s);
    // it is because from privious input it takes /n new line character so erase it we          have do do like that
    scanf("\n");
    scanf("%[^\n]%*c", sen); 
    //printing the staments
    printf("%c\n", ch); 
    printf("%s\n", s);
    puts(sen);
    return 0;
}
