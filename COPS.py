for _ in range(int(input())):
    (m,x,y) = map(int,input().split())
    houses = [int(i) for i in input().split()]
    houses.sort()
    print("house: ",houses)
    right_approach = 0
    house_available = 0
    for i in houses:
        left_approach = i - (x*y)
        print("i: ", i)
        print('left_approach: ',left_approach)
        print('right_aproach: ', right_approach)
        if(left_approach > right_approach):
            house_available += (left_approach - right_approach) - 1
        right_approach = i + (x*y)
        print('right_approach: ',right_approach)
        print('house_available: ',house_available)
    if(right_approach < 100):
        house_available += 100 - right_approach
    print('house available: ',house_available)