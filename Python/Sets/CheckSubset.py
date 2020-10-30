t = int(input())
for _ in range(t):
  noe_A = int(input())
  set_A = set(input().split(" "))
  noe_B = int(input())
  set_B = set(input().split(" "))
  print(set_A <= set_B)