def split_and_join(line):
  new = line.split(" ")
  return "-".join(new)

if __name__ == '__main__':
  line = input()
  result = split_and_join(line)
  print(result)