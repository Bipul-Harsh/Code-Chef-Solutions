vowel = ['a', 'e', 'i', 'o', 'u']
for _ in range(int(input())):
    n = int(input())
    s = input()
    ind = 0
    ans = 0
    while ind < n-1:
        if s[ind] not in vowel and s[ind+1] in vowel:
            ind += 1
            ans += 1
        ind += 1
    print(ans)