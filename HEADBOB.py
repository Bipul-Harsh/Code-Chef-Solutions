T = int(input())
while(T):
    n = int(input())
    lst = set(input())
    if(len(lst) == 3):
        print("NOT SURE")
    else: 
        if('Y' in lst):
            print("NOT INDIAN")
        else: 
            print("INDIAN")
    T -= 1