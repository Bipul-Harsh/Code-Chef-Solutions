for i in range(int(input())):
    inp = input()
    str_len = len(inp)
    first_half = inp[0:str_len//2]
    second_half = inp[str_len//2:] if (str_len%2==0) else inp[(str_len//2)+1:]
    setA = set(first_half)
    setA = setA.union(set(second_half))
    result1 = dict()
    result2 = dict()
    for i in setA:
        result1[i] = first_half.count(i)
        result2[i] = second_half.count(i)
    if(result1 == result2 ):
        print("YES")
    else:
        print("NO")