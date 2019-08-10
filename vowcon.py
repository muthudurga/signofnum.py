S=input()
c=['a','e','i','o','u']
a=[]
b=[]
x=''
y=''
for i in range(len(S)):
    if S[i] in c:
        a.append(S[i])
    else:
        b.append(S[i])
for i in range(len(a)):
    x=x+a[i]
for i in range(len(b)):
    y=y+b[i]
print(x+y)
        
