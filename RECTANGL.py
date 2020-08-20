for _ in range(int(input())):
    sides = sorted(list(map(int,input().split())))
    
    if sides[0] == sides[1] and sides[2] == sides[3]:
        print('YES')
    else:
        print('NO')