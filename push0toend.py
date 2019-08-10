N=int(input())
x=[int(x) for x in input().split()]
a=[]
if len(x)==N:
    y=0
    for i in range(len(x)):
        if x[i]!=0:
            a.append(x[i])
        else:
            y=y+1
    for i in range(y):
            a.append(0)
    print(*a)
