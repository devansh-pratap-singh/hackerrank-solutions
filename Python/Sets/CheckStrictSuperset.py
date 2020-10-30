set_A = set(input().split(" "))
nos = int(input())
flag = True
for _ in range(nos):
  sub = set(input().split(" "))
  if(sub < set_A):
    flag = True
  else:
    flag = False
    break
print(flag)