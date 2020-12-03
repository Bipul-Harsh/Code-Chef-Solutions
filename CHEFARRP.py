# cook your dish here
import numpy as np
for _ in range(int(input())):
    _ = input()
    A = list(map(int, input().split()))
    A = np.array(A)
    ans=arrlen=len(A)
    for i in range(2,arrlen+1):
        for j in range(arrlen-i+1):
            if(A[j:j+i].sum()==A[j:j+i].prod()):
                ans += 1
    print(ans)
