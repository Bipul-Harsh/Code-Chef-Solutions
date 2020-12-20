# cook your dish here
for _ in range(int(input())):
    n = int(input())
    ans = 0
    while(n != 0):
        ans+=1
        n -= int(n**.5)**2
    print(ans)