k = int(input())
rooms = sorted(map(int,input().split(" ")))
for i in range(1,len(rooms)):
  if(i != len(rooms)-1):
    if(rooms[i-1] != rooms[i] and rooms[i] != rooms[i+1]):
      print(rooms[i])
      break
  else:
    print(rooms[i])