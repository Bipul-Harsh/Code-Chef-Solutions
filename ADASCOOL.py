# cook your dish here
for _ in range(int(input())):
    n, m = map(int, input().split())
    if n%2 == 0 or m%2 == 0:
        print("YES")
    else:
        print("NO")