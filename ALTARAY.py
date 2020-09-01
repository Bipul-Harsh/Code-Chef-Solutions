for _ in range(int(input())):
  N = int(input())
  A = list(map(int,input().split()))
  alt_length = [1]*len(A)
  for i in range(len(A)-2,-1,-1):
    if(A[i]*A[i+1] < 0):
      alt_length[i] += alt_length[i+1]
  print(*alt_length)