for _ in range(int(input())):
    h,p = map(int, input().split())
    ans = 1 if(p*2 > h) else 0
    print(ans)