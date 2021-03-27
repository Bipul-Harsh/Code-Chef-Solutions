# cook your dish here
for _ in range(int(input())):
    a, y, x = map(int, input().split())
    if y-a > 0:
        print(a*x+1)
    else:
        print(y*x)
