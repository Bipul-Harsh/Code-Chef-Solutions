from math import sqrt
for _ in range(int(input())):
    t_range=int(input())
    locations = list()
    for _ in range(3):
        locations.append([int(i) for i in input().split()])
    ans = 0
    for i in range(2,-1,-1):
        dist = sqrt(((locations[i][0]-locations[i-1][0])**2) + ((locations[i][1]-locations[i-1][1])**2))
        if(dist <= t_range):
            ans += 1
            if(ans == 2): 
                print('yes')
                break
    if(ans<2):
        print('no')