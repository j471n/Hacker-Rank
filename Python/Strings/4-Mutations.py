#programmer : jatin Sharma

#funcion that takes the string, index, character and replace it
def mutate_string(string, position, character):
      l = list(string)              #creating string to list
      l[position] = character       #changing the character
      string = "".join(l)           #again joining the list to string
      return string                 #in the last returning the string

if __name__ == '__main__':
      s = input()
      index, char = input().split()
      s_new = mutate_string(s, int(index), char)
      print(s_new)