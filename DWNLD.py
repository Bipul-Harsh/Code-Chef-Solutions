for _ in range(int(input())):
    n, k = map(int, input().split())
    cost = 0
    for _ in range(n):
        t, d = map(int, input().split())
        if(t<=k):
            k -= t
        else:
            cost += (t-k)*d
            k = 0
    print(cost)