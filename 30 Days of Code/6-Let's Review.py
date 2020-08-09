#initializing test_cases
test_cases = int(input())

#looping
for i in range(0, test_cases):
          
    #taking string input
    str = input()

    #this loop is for chekcing the number is even if it is then it will print only even character
    for j in range(0, len(str)):
        if j % 2 == 0:
            print(str[j],end = "")  #in the end we use end="" because python default use \n which we don't want

    print(" ", end='')  # it is for to add space between even and odd character

    for k in range(0, len(str)):
        if k%2!=0:
            print(str[k], end="")

    print("")   #it is just another input from new line (it is related to line 8 str)