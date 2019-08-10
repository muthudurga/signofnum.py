S=input()
a=[]
for i in range(len(S)):
    if S[i].islower():
        a.append(S[i].upper())
    else:
        a.append(S[i].lower())
z=''
for i in range(len(a)):
    z=z+a[i]
print(z)
