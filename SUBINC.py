# cook your dish here
for _ in range(int(input())):
    _ = int(input())
    A = list(map(int, input().split()))
    ans = 0
    t_sum = 0
    n = 0
    a = 0
    for i in A:
        if(i >= a):
            n += 1
            t_sum += n
        else:
            ans += t_sum
            n = 1
            t_sum = 1
        a = i
    ans += t_sum
    print(ans)