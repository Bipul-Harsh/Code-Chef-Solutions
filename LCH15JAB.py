for _ in range(int(input())):
  s = list(input())
  s = [s.count(i) for i in set(s)]
  s_max = max(s)
  s.remove(s_max)
  if(sum(s) == s_max):
    print('YES')
  else:
    print('NO')
