#programmer : Jatin Sharma

#taking input 
n = int(input())
integer_list = map(int, input().split())  # adding numbers to the integer_list

#creating a tupple and adding interger_list element to the tupple
t = tuple(integer_list)

#printing the hash value of the tuple
print(hash(t))