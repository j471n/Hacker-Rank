#!/bin/python3

#definition : Recursion is a common mathematical and programming concept. It means that a function calls itself

# Complete the factorial function below.
def factorial(n):
    if(n == 1):
       return 1
    else:
        return n * factorial(n-1)   #here the funtion is calling itself
       

if __name__ == '__main__':

    n = int(input())
    #calling fucntion and storing return value in result variable
    result = factorial(n)
    print(result)       #printing result
