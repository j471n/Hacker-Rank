# Enter your code here. Read input from STDIN. Print output to STDOUT

t = int(input())

for i in range(t):
    try:
        n, m = map(int, input().split())
        print(n // m)
    except ZeroDivisionError as e:
        print("Error Code:", e)
    except ValueError as e:
        print("Error Code:", e)
        
        
