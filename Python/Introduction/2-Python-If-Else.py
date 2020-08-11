#taking number as input
n = int(input().strip())

#conditions
if n%2!=0 or n%2==0 and n in  range(6,21):
    print("Weird")
if n % 2 == 0 and n in range(2, 6) or n % 2 == 0 and n > 20:
    print("Not Weird")
