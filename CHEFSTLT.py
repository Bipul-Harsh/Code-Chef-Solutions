for _ in range(int(input())):
    min_diff = 0;max_diff = 0
    S1 = input()
    S2 = input()[0:len(S1)]
    if(S1 == S2):
        max_diff = S1.count('?')
        min_diff = 0
        print(min_diff, max_diff)
        continue
    for x,y in zip(S1,S2):
        if x == "?" or y == "?":
            max_diff+=1
        elif x != y :
            min_diff += 1
            max_diff += 1
    print(min_diff,max_diff) 