#Programmer : Jatin Sharma

N, M = map(int, input().split())

#printing upper pattern
for i in range(1, N, 2): 
    print((i * ".|.").center(M, "-"))

#printing center welcome patern
print("welcome".upper().center(M, "-"))

#printing lower pattern
for i in range(N-2, -1, -2): 
    print((i * ".|.").center(M, "-"))
