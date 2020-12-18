# cook your dish here
import math
for _ in range(int(input())):
    n, d = map(int, input().split())
    a = list(map(int, input().split()))
    b = len(list(filter(lambda x: x>=80 or x<=9, a)))
    c = len(a) - b
    print(math.ceil(b/d)+math.ceil(c/d))