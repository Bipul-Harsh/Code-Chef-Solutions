for _ in range(int(input())):
    n, b = map(int, input().split())
    ans = max(*[[int(i.split()[0])*int(i.split()[1]) if int(i.split()[2])<=b else 0 for i in [input()]] for i in range(n)])
    ans = int(*ans) if type(ans) is list else ans
    print(ans if ans > 0 else "no tablet")