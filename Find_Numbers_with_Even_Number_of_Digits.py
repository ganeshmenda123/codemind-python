n=int(input())
c=0
l=list(map(int,input().split()))
for i in l:
    k=0
    while i:
        k=k+1
        i=i//10
    if k%2==0:
        c=c+1
print(c)