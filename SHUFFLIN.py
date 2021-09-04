# cook your dish here
from sys import stdin
from sys import stdout

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    e = n//2
    o = n - e
    a = map(int, stdin.readline().split())
    e_n = len(list(filter(lambda x: x%2==0, a)))
    o_n = n - e_n
    stdout.write(f'{min(o, e_n) + min(e, o_n)}\n')