n=int(input())
l=list(map(int,input().split()))
a=[]
for i in l:
    c=0
    for j in l:
        if i>j:
            c=c+1
    a.append(c)
for i in a:
    print(i,"",end="")