from math import sqrt
for _ in range(int(input())):
    A,B = map(int,input().split())
    na = int(sqrt(A))
    nb = int((sqrt(1+4*B)-1)/2)
    if(nb>=na):
        print('Bob')
    else:
        print('Limak')