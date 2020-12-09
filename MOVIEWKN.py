for _ in range(int(input())):
    n = input()
    L = list(map(int, input().split()))
    R = list(map(int, input().split()))
    res=[]
    for ind, LRval in enumerate(zip(L, R)):
        res.append([LRval[0],LRval[1],ind+1])
    res=sorted(res,key=lambda x:(x[0]*x[1],x[1],100-x[2]),reverse=True)
    print(res[0][2])