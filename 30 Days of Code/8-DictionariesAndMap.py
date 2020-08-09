n = int(input())
#creating phonebook dictinary
phonebook = dict()

for i in range(n):
    entry = input().split(" ")
    #getting name, which is entry[0] and phonenumber which is entry [1]
    phonebook[entry[0]] = phonebook.get(entry[0], entry[1])

while 1:
    try:
        #taking name to print the result if it exist
        name = input()
        if name in phonebook:
            print(str(name) + "=" + str(phonebook[name]))
        else:
            print("Not found")
    except:
        break
