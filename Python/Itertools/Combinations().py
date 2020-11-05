from itertools import combinations
S = input().split(" ")
for i in range(1, int(S[1]) + 1):
  for j in combinations(sorted(S[0]), i):
    print(''.join(j))