for _ in range(int(input().split())):
  n,k = map(int,input().split())
  initial_status = list(map(int, input().split()))
  map(lambda x: x+k, initial_status)
  ans = list(filter(lambda x: x%7 == 0), initial_status)
  print(len(ans))
