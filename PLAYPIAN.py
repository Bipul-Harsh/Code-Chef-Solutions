for _ in range(int(input())):
    log = input()
    for ind, val in enumerate(log[::2]):
        if val == log[2*ind+1]:
            print('no')
            break
    else:
        print('yes')