from itertools import permutations
S = input().split(" ")
for _ in sorted(permutations(S[0], int(S[1]))):
  print(''.join(_))