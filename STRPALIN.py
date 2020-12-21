# cook your dish here
for _ in range(int(input())):
    a = set(input())
    b = set(input())
    c = a.intersection(b)
    if(len(c)>0):
        print('Yes')
    else:
        print('No')