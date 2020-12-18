# cook your dish here
for _ in range(int(input())):
    n = int(input())
    s = list(input())
    print(n - max(s.count('R'), s.count('G'), s.count('B')))