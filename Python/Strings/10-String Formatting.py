#Ptogrammer : Jatin Sharma

def print_formatted(number):

    #variable for space which'll have lenght of binary number of prompted number
    space = len(bin(n)) - 2
    for i in range(1, number + 1):
        print("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(
            i, width=space))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)