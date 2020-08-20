for _ in range(int(input())):
    n,k = map(int, input().split())
    P = list(filter(lambda x: k%x == 0, [int(i) for i in input().split()]))
    P_u = list(map(lambda x: k//x, P))
    if(len(P_u) > 0):
        print(P[P_u.index(min(P_u))])
    else:
        print(-1)