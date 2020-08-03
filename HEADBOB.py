for _ in range(int(input())):
    input()
    lst = set(input())
    if('I' in lst):
        print("INDIAN")
    elif('Y' in lst):
        print("NOT INDIAN")
    else:
        print("NOT SURE")