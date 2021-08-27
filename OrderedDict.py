from collections import OrderedDict
n = int(input())

od = OrderedDict()
for _ in range(n):
    item, price = input().rsplit(' ', 1)       
    # Learning point above - using "rsplit()"
    # Has 2 arguments: delimiter and the number of times to split from the end
    price = int(price)
    if item in od.keys():
        od[item] += price
    else:
        od[item] = price

for k, v in od.items():
    print(k, v)