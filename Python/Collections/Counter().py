from collections import Counter
x = int(input())
sizes = list(map(int,input().split(" ")))
sizes_dict = Counter(sizes)
n = int(input())
s = 0
p = 0
money = 0
for _ in range(n):
  s,p = map(int,input().split(" "))
  if(s in sizes_dict.keys() and sizes_dict[s] != 0):
    money += p
    sizes_dict[s] -= 1
print(money)