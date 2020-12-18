# cook your dish here
from math import ceil
d1,v1, d2, v2, p = map(int, input().split())
if(d1 == d2):
    print(d1 + ceil(p/(v1+v2)) - 1)
elif(d1 < d2):
    a = (d2 - d1)*v1
    b = p - a
    print((d1-1) + (d2-d1 if(a<p) else ceil(p/v1)) + (ceil(b/(v1+v2)) if(a<p) else 0))
else:
    a = (d1 - d2)*v2
    b = p - a
    print((d2-1) + (d1-d2 if(a<p) else ceil(p/v2)) + (ceil(b/(v1+v2)) if(a<p) else 0))