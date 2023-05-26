n=int(input())
lst=list(map(int,input().split()))
s=0
l=[]
for i in lst:
    if i not in l:
        l.append(i)
for j in l:
    if j%2==0:
        s=s+1
print(s)