for _ in range(int(input())):
  n,k = map(int,input().split())
  N = input().split()
  K = []
  for i in range(k):
    K += input().split()[1:]
  for i in N:
    if(i in K):
      print("YES")
    else:
      print('NO')
  print('')
  