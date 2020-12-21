# cook your dish here
for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    l=sorted(l,reverse=True)
    lst=[]
    while len(lst)<2 and len(l)>1:
        if l[0]==l[1]:
            lst.append(l[0])
            l.pop(0)
            l.pop(0)
        else:
            l.pop(0)
    if len(lst)>=2:
        print(lst[0]*lst[1])
    else:
        print(-1)