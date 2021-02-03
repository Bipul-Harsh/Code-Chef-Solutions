def oper(x):
    ans = x[0]*20 - x[1]*10
    if ans < 0:
        return 0
    else:
        return ans
for _ in range(int(input())):
    n = input()
    A = map(int, input().split())
    B = map(int, input().split())
    c = map(oper, zip(A, B))
    print(max(c))
