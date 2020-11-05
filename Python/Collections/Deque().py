from collections import deque
n = int(input())
d = deque()
for _ in range(n):
  com = input().split()
  if(com[0] == "append"):
    d.append(com[1])
  elif(com[0] == "pop"):
    d.pop()
  elif(com[0] == "popleft"):
    d.popleft()
  else:
    d.appendleft(com[1])
print(" ".join(d))