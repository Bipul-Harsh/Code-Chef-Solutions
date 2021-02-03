# cook your dish here
for _ in range(int(input())):
    s = input()
    s = s.strip('0')
    if '0' in s or len(s)==0:
        print('NO')
    else:
        print('YES')
