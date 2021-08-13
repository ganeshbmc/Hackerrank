a = set(map(int, input().split()))
n = int(input())
a_is_super = True
for i in range(n):
    b = set(map(int, input().split()))
    if (len(a) <= len(b)) or (b-a != set()):
        a_is_super = False
print(a_is_super)
