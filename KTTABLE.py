for _ in range(int(input())):
  N = int(input())
  A = list(map(int, input().split()))
  B = list(map(int, input().split()))
  time_elapsed = 0
  successful_cooking = 0
  for (i,j) in zip(A,B):
    if(j <= i-time_elapsed):
      successful_cooking += 1
    time_elapsed += i
  print(successful_cooking)