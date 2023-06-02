m,n=map(int,input().split())
lst=list(map(int,input().split()))
c=0
for i in range(m):
    if lst[i]%n!=0:
        c=c+1
print(c)