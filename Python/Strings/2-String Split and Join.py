#Programmer : Jatin Sharma

def split_and_join(line):

      hyphen = line.split(" ")      #splliting the word with " "
      return "-".join(hyphen)       # adding "-" instead of " "

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)