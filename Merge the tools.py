s = input()
k = int(input())
n = len(s)
ss_list = [(s[i:i+k]) for i in range(0, len(s), k)]

for substring in ss_list:
    u_str = ''
    for char in substring:
        if char not in u_str:
            u_str += char
    print(u_str)
