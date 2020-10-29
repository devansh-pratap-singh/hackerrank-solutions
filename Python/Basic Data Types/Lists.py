N = int(input())
lst = []
for _ in range(N):
  in_str = input()
  cmd_lst = in_str.split(" ")
  if(cmd_lst[0] == 'insert'):
    lst.insert(int(cmd_lst[1]),int(cmd_lst[2]))
  if(cmd_lst[0] == 'print'):
    print(lst)
  if(cmd_lst[0] == 'remove'):
    lst.remove(int(cmd_lst[1]))
  if(cmd_lst[0] == 'append'):
    lst.append(int(cmd_lst[1]))
  if(cmd_lst[0] == 'sort'):
    lst.sort()
  if(cmd_lst[0] == 'pop'):
    lst.pop()
  if(cmd_lst[0] == 'reverse'):
    lst.reverse()