# cook your dish here
t = int(input())
while t > 0:
    n = int(input())
    arr = list(map(int, input().split()[:n]))
    arr.sort()
    print(arr[0] + arr[1])
    t -= 1
