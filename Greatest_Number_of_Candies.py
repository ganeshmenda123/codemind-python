z=int(input())
l=list(map(int,input().split()))
n=int(input())
a=[]
m=max(l)
for i in l:
    if i+n>=m:
        a.append("True")
    else:
        a.append("False")
for i in a:
    print(i,"",end="")