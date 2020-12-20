for _ in range(int(input())):
    c,d,l=map(int,input().split())
    if l%4==0:
        x=c+d-l//4
        if x >= 0 and x <= min(c, 2 * d):
            print("yes")
        else:
            print("no")
    else:
        print("no")