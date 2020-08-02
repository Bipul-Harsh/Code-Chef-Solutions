def sum(d,n,l_iter=0,sumr=0):
    if(d==1):
        for i in range(l_iter+1,n+1):
            sumr += i
            l_iter +=1
        return(sumr)
    else:
        for i in range(l_iter+1,n+1):
            sumr += i
            l_iter += 1
        n = sumr
        return sum(d-1,n,l_iter,sumr)
T = int(input())
for i in range(T):
    (d,n) = map(int,input().split())
    print(sum(d,n))