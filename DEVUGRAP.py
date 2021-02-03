# cook your dish here
def proc(val):
    c_val = val%k
    if val < k:
        return  k-c_val
    else:
        return min(c_val, k-c_val)
    return ans
for _ in range(int(input())):
    n, k = map(int, input().split())
    buckets = map(int, input().split())
    ans = sum(map(proc, buckets))
    print(ans)
