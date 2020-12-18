# cook your dish here
for _ in range(int(input())):
    _ = input()
    a = list(map(int, input().split()))
    _ = input()
    b = list(map(int, input().split()))
    c = 1
    for i in range(1,len(b)):
        if b[i] not in a:
            c=0
            break
        elif a.index(b[i-1]) > a.index(b[i]):
            c = 0
            break
    print("Yes" if c==1 else 'No')