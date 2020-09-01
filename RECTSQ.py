import math
for _ in range(int(input())):
  N,M = map(int,input().split())
  fullArea = N*M
  plotSide = math.gcd(N,M)
  plotArea = plotSide*plotSide
  plotNo = fullArea//plotArea
  print(plotNo)