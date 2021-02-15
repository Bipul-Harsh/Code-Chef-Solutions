import string
for _ in range(int(input())):
    n, k = map(int, input().split())
    s = input()
    lower_count = len(list(filter(lambda x: x in string.ascii_lowercase, s)))
    upper_count = n - lower_count
    if lower_count > k and upper_count <= k:
        print("chef")
    elif upper_count > k and lower_count <= k:
        print("brother")
    elif lower_count > k:
        print('none')
    else:
        print('both')
