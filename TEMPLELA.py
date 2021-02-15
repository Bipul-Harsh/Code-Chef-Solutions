for _ in range(int(input())):
    n = int(input())
    h = list(map(int, input().split()))
    if n%2 == 0 or h[0] != 0:
        print('no')
    else:
        for i in range(1, n//2+1):
            if h[i] != h[-i-1] or h[i]-h[i-1]!=1:
                print('no')
                break
        else:
            print('yes')
