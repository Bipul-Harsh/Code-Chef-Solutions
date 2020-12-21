# cook your dish here
for _ in range(int(input())):
    x, y, K, N = map(int, input().split())
    if x == y:
        print('Yes')
    else:
        a = max(x,y)
        b = min(x,y)
        c = (a-(x+y)/2)%K
        if(c != 0):
            print('No')
        else:
            print("Yes")