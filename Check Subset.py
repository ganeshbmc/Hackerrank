t = int(input())
for i in range(t):
    na = int(input())
    a = set(map(int, input().split()))
    nb = int(input())
    b = set(map(int, input().split()))
    print((a-b) == set())
