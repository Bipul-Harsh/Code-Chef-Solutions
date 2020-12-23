# cook your dish here
for _ in range(int(input())):
    s = input()
    a = set(s[::2])
    b = set(s[1::2])
    if len(a) == 1 and len(b) == 1 and a != b:
        print('YES')
    else:
        print('NO')