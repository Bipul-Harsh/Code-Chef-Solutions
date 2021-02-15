for _ in range(int(input())):
    x = sorted(map(int,input().split()))
    if sum(x[:2]) == x[2]:
        print('yes')
    else:
        print('no')
