for _ in range(int(input())):
    n = int(input())
    C = list(map(int, input().split()))
    if(n == 1):
        print(C[0])
    else:
        C.sort()
        a = C[:-1]
        a.reverse()
        b = [C[-1]]
        diff = abs(sum(a) - sum(b))
        while( abs(sum(b,a[-1]) - sum(a[:-1])) < diff ):
            b.append(a.pop())
            diff = abs(sum(a) - sum(b))
        print(max(sum(a), sum(b)))