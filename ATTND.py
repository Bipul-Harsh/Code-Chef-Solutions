# cook your dish here
for _ in range(int(input())):
    f_names = []
    l_names = []
    for _ in range(int(input())):
        name = input().split()
        f_names.append(name[0])
        l_names.append(name[1])
    for ind, name in enumerate(f_names):
        if f_names.count(name) > 1:
            print(name+' '+l_names[ind])
        else:
            print(name)