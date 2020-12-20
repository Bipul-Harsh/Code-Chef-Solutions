# cook your dish here
for _ in range(int(input())):
    n, b, m = map(int, input().split())
    time = 0
    while(n):
        qn = (n+1)//2
        time += qn*m + b
        n -= qn
        m <<= 1
    print(time - b)