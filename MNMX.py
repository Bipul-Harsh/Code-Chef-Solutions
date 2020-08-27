for _ in range(int(input())):
    n = int(input())
    A = map(int, input().split())
    print(min(A)*(n-1))