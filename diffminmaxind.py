N=int(input())
x=[int(x) for x in input().split()]
if len(x)==N:
    for i in range(N):
        if x[i]==max(x):
            a=i
            break
    for i in range(N):
        if x[i]==min(x):
            b=i
            break
    print(a-b)
