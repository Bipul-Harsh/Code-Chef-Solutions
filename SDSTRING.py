# cook your dish here
for _ in range(int(input())):
    s = input()
    l = len(s)
    if l%2 == 1 or s.count('1') == l or s.count('0') == l:
        print(-1)
    else:
        z = min(s.count('0'), s.count('1'))
        print(l//2 - z)