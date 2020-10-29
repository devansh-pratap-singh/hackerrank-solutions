def swap_case(s):
  n = ""
  for _ in s:
    if(_.isupper()):
      n += _.lower()
    else:
      n+= _.upper()
  return n

if __name__ == '__main__':
  s = input()
  result = swap_case(s)
  print(result)