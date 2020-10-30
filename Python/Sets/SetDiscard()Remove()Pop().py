n = int(input())
s = set(map(int, input().split()))
c = int(input())
for i in range(c):
  com = input().split()
  if(com[0] == "remove"):
    s.remove(int(com[1]))
  elif(com[0] == "discard"):
    s.discard(int(com[1]))
  else:
    s.pop()
print(sum(list(s)))