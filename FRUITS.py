for _ in range(int(input())):
    (n,m,k) = map(int, input().split())
    diff = max(n-m,m-n)
    if(diff>k):
        print(diff-k)
    else:
        extra_diff = k-diff
        print(extra_diff%2)