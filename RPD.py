# cook your dish here
def sum_digit(val1, val2):
    return sum( map( int, str(val1*val2) ) )

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for ind, val1 in enumerate(a[:-1]):
        for val2 in a[ind+1:]:
            val3 = sum_digit(val1, val2)
            if(ans < val3):
                ans = val3
    print(ans)