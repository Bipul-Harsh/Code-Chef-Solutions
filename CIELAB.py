# cook your dish here
from sys import stdin, stdout

a, b = map(int, stdin.readline().split())
a = abs(a-b)
if a%10 == 9:
    a -= 1
else:
    a += 1

stdout.write(f'{a}\n')
