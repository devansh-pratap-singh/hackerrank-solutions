e = input()
set_e = set(input().split(" "))
f = input()
set_f = set(input().split(" "))
common = set_e.intersection(set_f)
print(len(common))