#Programmer : Jatin Sharma

S = input().strip()

try:
    int(S)
    print(S)

except(ValueError):
    print("Bad String")
