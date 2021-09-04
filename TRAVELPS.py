# cook your dish here
from sys import stdin
from sys import stdout

for _ in range(int(stdin.readline())):
    n, a, b = map(int, stdin.readline().split())
    s = stdin.readline()
    a_count = s.count('0')
    b_count = s.count('1')
    stdout.write(f'{a_count*a + b_count*b}\n')