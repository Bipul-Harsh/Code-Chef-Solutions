# cook your dish here
import numpy as np
for _ in range(int(input())):
    n, k = map(int, input().split())
    kn = n-k
    ans = np.arange(1, n+1)
    ind = 0
    if(kn <= k):
        while(kn > 0):
            ans[ind] = -ans[ind]
            ind += 2
            kn -= 1
    else:
        ans = -ans
        while(k > 0):
            ans[ind] = -ans[ind]
            ind += 2
            k -= 1
    print(*ans)