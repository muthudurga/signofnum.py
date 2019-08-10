S=input()
a=[]
y=''
for i in range(len(S)):
    if S[i]!=' ':
        y=y+S[i]
        if len(S)-1==i:
            a.append(y)
    else:
        a.append(y)
        y=''
for i in range(len(a)):
    if a[i]=='and':
        temp=a[i+1]
        a[i+1]=a[i-1]
        a[i-1]=temp
print(*a)
