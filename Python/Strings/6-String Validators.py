#programmer : Jatin Sharma

string = input()

# initializing boolean variable with false value
alnum = False
alpha = False
digit = False
lowerCase = False
upperCase = False

# loop for checking that any character of the string is alnum,aplha,digit,lower,upper
# if YES the change the value of their respective variable to TURE
for i in string:
    if not alnum and i.isalnum():
        alnum = True
    if not alpha and i.isalpha():
        alpha = True
    if not digit and i.isdigit():
        digit = True
    if not lowerCase and i.islower():
        lowerCase = True
    if not upperCase and i.isupper():
        upperCase = True

# Printing all the boolean values
print(alnum)
print(alpha)
print(digit)
print(lowerCase)
print(upperCase)
