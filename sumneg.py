N=int(input())
if N!=0:
    x=[int(x) for x in input().split()]
    if len(x)==N:
        s=0
        for i in range(N):
            if x[i]<0:
                s=s+x[i]
        print(s)
