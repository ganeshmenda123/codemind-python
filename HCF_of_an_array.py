n=int(input())
lst=list(map(int,input().split()))
h=[]
cf=[]
for i in lst:
    for j in range(1,i+1):
        if i%j==0:
            h.append(j)
for i in h:
    if h.count(i)==n:
        cf.append(i)
print(max(cf))