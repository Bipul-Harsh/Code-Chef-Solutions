# cook your dish here
a = int(input())
b = int(input())
c = int(input())
d = b**2 - 4*a*c
if d > 0:
    print( (-b + d**0.5)/(2*a) )
    print( (-b - d**0.5)/(2*a) )
elif d==0:
    root = (-b + d**0.5)/(2*a)
    print(root,root, sep='\n')
