#Programmer : Jatin Sharma

#fucntion definition
def count_substring(string, sub_string):
    
    #checking if sting < sub-string then it is immposible to have sub_string in string
    if len(string) < len(sub_string): 

        return 0
    else:

        c = 0       #variable which count how much tome sub_string appear
        for i in range(len(string) - len(sub_string)+1):
            if string[i :i+len(sub_string)] == sub_string:
                c += 1
        return c


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)