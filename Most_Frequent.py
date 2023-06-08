n=int(input())
l=list(map(int,input().split()))
d={}
for i in l:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
a=[]
m=max(d.values())
for i in d:
    if d[i]==m:
        a.append(i)
print(min(a))