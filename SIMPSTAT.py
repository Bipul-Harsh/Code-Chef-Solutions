# cook your dish here
for _ in range(int(input())):
    n, k = map(int, input().split())
    a = sorted(map(int, input().split()))
    ans = a[k:n-k]
    print('{:.6f}'.format(sum(ans)/len(ans)))