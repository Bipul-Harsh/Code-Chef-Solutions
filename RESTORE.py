for _ in range(int(input())):
    N = int(input())
    B = list(map(int, input()))
    B.reverse()
    a = 2
    ans = [0]*N
    for ind, val in enumerate(B):
        if(N-ind == val):
            ans[ind] = a
            a+=1
        else:
            ans[ind] = ans[N-val]
    ans.reverse()
    print(ans)
