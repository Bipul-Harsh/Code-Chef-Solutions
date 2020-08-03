for _ in range(int(input())):
    (hardness, carbon, tensile) = map(float, input().split())
    checks = [50,0.7,5600]
    res = 0
    res += 1 if hardness > checks[0] else 0
    res += 2 if carbon < checks[1] else 0
    res += 4 if tensile > checks[2] else 0
    if(res == 7):
        print(10)
    elif(res == 3):
        print(9)
    elif(res == 6):
        print(8)
    elif(res == 5):
        print(7)
    elif(res == 1 or res == 2 or res == 4):
        print(6)
    else:
        print(5)
