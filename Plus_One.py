n=int(input())
l=list(map(int,input().split()))
d=0
i=0
while i!=len(l):
    d=d*10+l[i]
    i=i+1
d=d+1
a=[]
c=0
while d:
    a.append(d%10)
    d=d//10
for i in range(len(a)-1,-1,-1):
    print(a[i],"",end="")