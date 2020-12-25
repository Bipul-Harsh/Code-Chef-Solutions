# cook your dish here
for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(lambda x: int(x)%2, input().split()))
    c = a.count(0)
    if k==0 and c==n :
        print("NO")
    elif c>=k:
        print("YES")
    else:
        print("NO")