N=int(input())
S=[]
n=[]
y=0
for i in range(N):
    S.append(input())
a=['a','e','i','o','u','A','E','I','O','U']
if len(S)==1:
    print(*S)
else:
    for i in range(len(S)):
        b=S[i]
        for x in range(len(b)):
            if b[x] in a:
                y=y+1
        n.append(y)
        y=0
    i=0
    while(i>=0):
        if n!=[]:
            z=max(n)
            if n[i]==z:
                print(S[i])
                S.remove(S[i])
                n.remove(n[i])
                i=0
            else:
                i=i+1            
        else:
            break

