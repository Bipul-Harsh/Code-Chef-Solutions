for _ in range(int(input())):
  N = int(input())
  no_pair = []
  for _ in range(N):
    doll_type = int(input())
    if(doll_type not in no_pair):
      no_pair.append(doll_type)
    else:
      no_pair.remove(doll_type)
  print(*no_pair)
