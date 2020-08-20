for _ in range(int(input())):
    s = input(); p = input()
    ans = [i*(s.count(i)-p.count(i)) for i in set(s)]
    ans.append(p)
    print(''.join(sorted(ans)))