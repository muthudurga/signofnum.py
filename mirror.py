n=int(input())
x=[int(x) for x in input().split()]
if len(x)==n:
    y=[int(y) for y in input().split()]
    if len(y)==n:
        y.reverse()
        if x==y:
            print('yes')
        else:
            print('no')
