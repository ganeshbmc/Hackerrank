for i in range(1,int(input())):
    # print(i*sum([pow(10, k) for k in range(i)]))
    print(i*sum(map(lambda x: 10**x, range(i))))