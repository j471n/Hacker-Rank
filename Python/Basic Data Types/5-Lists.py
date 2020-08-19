#programmer : Jatin Sharma



list = []   #creatung a empty list
num = int(input())   # taking a input to make a loop run
for i in range(num):

    choice = input().split()      # it is a variable which takes what user want to input

    if choice[0] == "insert":

        #inserting the numbers in the list if user choose this
        list.insert(int(choice[1]), int(choice[2]))

    elif choice[0] == "append":

        #appending the list if the user choose this
        list.append(int(choice[1]))

    elif choice[0] == "remove":

        #removing elements from the list
        list.remove(int(choice[1]))

    elif choice[0] == "print":  #printing the list

        print(list)

    elif choice[0] == "reverse":   #reversing the list

        list.reverse()

    elif choice[0] == "sort":      #sorting the list

        list.sort()

    elif choice[0] == "pop":        #removing the last element of the list

        list.pop()
