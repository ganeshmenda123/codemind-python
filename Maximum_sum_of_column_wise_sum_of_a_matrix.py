n,m=map(int,input().split())
lis=[]
for i in range(n):
    k=list(map(int,input().split()))
    lis.append(k)
m=[]
for j in range(len(k)):
    c=0
    for k in range(len(lis)):
        c+=lis[k][j]
    m.append(c)
print(max(m))