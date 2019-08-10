N=int(input())
x=[int(x) for x in input().split()]
if len(x)==N:
    for i in range(N):
        if x[i]==max(x):
            a=i
        elif x[i]==min(x):
            b=i
    print(a-b)
