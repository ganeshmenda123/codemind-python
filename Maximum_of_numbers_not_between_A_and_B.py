n=int(input())
lst=list(map(int,input().split()))
a,b=map(int,input().split())
c=[]
d=[]
for i in range(a,b+1):
    c.append(i)
for i in lst:
    if i not in c:
        d.append(i)
if len(d)>0:
    print(max(d))
else:
    print(-1)