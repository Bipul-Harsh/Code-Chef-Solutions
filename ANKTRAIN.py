# cook your dish here
for _ in range(int(input())):
    n = int(input())-1
    partner_birth = {0:[4,'LB'], 1:[4,'MB'], 2:[4,'UB'], 3:[-2,'LB'], 4:[-2,'MB'], 5:[-2,'UB'], 6:[2,'SU'], 7:[0,'SL']}
    print(str(n+partner_birth[n%8][0])+partner_birth[n%8][1])