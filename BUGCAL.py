for _ in range(int(input())):
    a, b = map(int, input().split())
    ans = temp = 0
    digit = 1
    while a or b:
        temp = (a%10 + b%10)%10
        ans += temp*digit
        digit *= 10
        a //= 10
        b //= 10
    print(ans)
