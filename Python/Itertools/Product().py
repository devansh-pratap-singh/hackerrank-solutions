from itertools import product
A = list(map(int,input().split(" ")))
B = list(map(int,input().split(" ")))
C = product(A,B)
for _ in C:
  print(_, end = " ")