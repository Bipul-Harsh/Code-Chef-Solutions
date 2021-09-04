# cook your dish here
from sys import stdout
from sys import stdin

for _ in range(int(stdin.readline())):
    a,b,c,d,e = map(int, stdin.readline().split())
    if (a+b <= d and c <= e) or (a+c <= d and b <= e) or (b+c <= d and a <= e):
        stdout.write("yes\n")
    else:
        stdout.write("no\n")