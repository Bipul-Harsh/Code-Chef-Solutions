S = set(input())
for _ in range(int(input())):
    W = set(input())
    W.difference_update(S)
    if(len(W) >0):
        print('Yes')
    else:
        print("No")