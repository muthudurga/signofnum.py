x,y=input().split()
a=[]
a.append(x)
a.append(y)
b=['R','P']
c=['P','R']
e=['R','S']
f=['R','S']
g=['P','S']
h=['S','P']
if a==b or a==c:
    print('P')
elif a==e or a==f:
    print('R')
elif a==g or a==h:
    print('S')
else:
    print('D')
