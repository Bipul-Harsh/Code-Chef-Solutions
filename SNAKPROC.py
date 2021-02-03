# cook your dish here
for _ in range(int(input())):
    l = input()
    s = list(input())
    s = list(filter(lambda x: x != '.', s))
    if 'T' in s[::2] or 'H' in s[1::2] or len(s)%2 != 0:
        print('Invalid')
    else:
        print('Valid')