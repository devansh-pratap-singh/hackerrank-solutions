T = int(input())
for _ in range(T):
    E = ""
    O = ""
    S = input()
    for i in range(len(S)):
        if(i%2 == 0):
            E+=S[i]
        else:
            O+=S[i]
    print(E+" "+O)