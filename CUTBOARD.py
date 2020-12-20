# cook your dish here
for _ in range(int(input())):
    n, m = map(int, input().split())
    if(m == 1 or n == 1):
        print(0)
    else:
        print((m-1)*(n-1))