list = []
num = int(input())

for index in range(num):
      name = input()
      score = float(input())
      list.append([name, score])

sh = sorted(set([x[1] for x in list]))
for n in sorted(x[0] for x in list if x[1] == sh[1]):
      print(n)
