for _ in range(int(input())):
    inp = input()
    str_len = len(inp)
    first_half = sorted(inp[0:str_len//2])
    second_half = sorted(inp[str_len//2:] if (str_len%2==0) else inp[(str_len//2)+1:])
    if(first_half == second_half):
        print("YES")
    else:
        print("NO")