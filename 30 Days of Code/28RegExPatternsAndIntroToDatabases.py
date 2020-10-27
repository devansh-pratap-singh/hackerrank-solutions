import re
A = []
N = int(input())
for i in range(N):
    data = str(input()).split(" ")
    name = data[0]
    email = data[1]
    if re.search(".+@gmail\.com$", email):
        A.append(name)
A.sort()
for name in A:
    print(name)