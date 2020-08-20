chef_score = 0
rick_score = 0
for _ in range(int(input())):
    Pc, Pr = map(int, input().split())
    digit = (Pc // 9) + (1 if(Pc % 9 > 0) else 0)
    digit2 = (Pr // 9) + (1 if(Pr % 9 > 0) else 0)
    if(digit == digit2):
        print(1,digit2)
    elif(digit < digit2):
        print(0,digit)
    else:
        print(1,digit2)