n=int(input())
lst=list(map(int,input().split()))
a,b=map(int,input().split())
s=0
for i in lst:
    if i>=a and i<=b:
        s+=1
        print(i,end=" ")
if s==0:
    print(-1)