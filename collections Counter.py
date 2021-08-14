x = int(input())
shoe_sizes = list(map(int, input().split()))
ss_counter = {ss:shoe_sizes.count(ss) for ss in shoe_sizes}
n = int(input())

earnings = 0
for cust in range(n):
    size, price = map(int, input().split())
    if size in ss_counter.keys():
        if ss_counter[size] > 0:
            earnings += price
            ss_counter[size] -= 1
    
print(earnings)