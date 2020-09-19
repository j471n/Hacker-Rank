# Programmer : Jatin Sharma

from collections import OrderedDict

n = int(input())
ordered_dict = OrderedDict()

for i in range(n):
    item_name, space, net_price = input().rpartition(' ')
    ordered_dict[item_name] = ordered_dict.get(item_name, 0) + int(net_price)


for i in ordered_dict:
    print(i, ordered_dict[i])
