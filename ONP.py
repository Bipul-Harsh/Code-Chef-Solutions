for _ in range(int(input())):
    stack = []
    ans = ""
    for value in input():
        if(value.isalpha()):
            ans += value
        elif(value == '('):
            stack.append(value)
        elif(value == ')'):
            check = stack.pop()
            while(check != '('):
                ans += check
                check = stack.pop()
        else:
            stack.append(value)
    print(ans)