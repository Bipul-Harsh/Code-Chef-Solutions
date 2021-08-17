# cook your dish here
from sys import stdin
from sys import stdout

for _ in range(int(stdin.readline())):
    _ = stdin.readline()
    s = sorted(map(int, stdin.readline().split()))
    ans = []
    for ind, val in enumerate(s[:-1]):
        ans.append(s[ind+1]-val)
    print(f'{min(ans)}\n')
