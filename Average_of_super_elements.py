n=int(input())
l=list(map(int,input().split()))
lis=[]
c=0
for i in l:
    if l.count(i)==i and i not in lis:
        lis.append(i)
        c+=1
if c==0:
    print(-1)
else:
    avg=(sum(lis)/len(lis))
    print("%0.2f"%avg)