# cook your dish here
for _ in range(int(input())):
    a, b = map(int, input().split())
    ea = a//2
    eb = b//2
    print((a-ea)*(b-eb) + (ea*eb))