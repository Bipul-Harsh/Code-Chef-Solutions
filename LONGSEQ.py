for _ in range(int(input())):
    n=input()
    count0,count1=0,0
    for ch in n:
        if(ch=="0"):
            count0+=1
        else:
            count1+=1
    if(count0==1 or count1==1):
        print("Yes")
    else:
        print("No")