# cook your dish here
for _ in range(int(input())):
    _ = input()
    a = sorted(map(int, input().split()))
    b = sorted(map(int, input().split()))
    asum = sum(a[:-1])
    bsum = sum(b[:-1])
    if asum<bsum:
        print('Alice')
    elif asum>bsum:
        print('Bob')
    else:
        print("Draw")