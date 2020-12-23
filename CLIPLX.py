# cook your dish here
for _ in range(int(input())):
    x, y = map(int, input().split())
    if x <= y:
        print(0)
    else:
        print(x-y)