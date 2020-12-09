for _ in range(int(input())):
    N,K = map(int, input().split())
    S = input().split('X')
    for i in S:
        i = i.strip('_:')
        print(i)