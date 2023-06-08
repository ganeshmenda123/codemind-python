n=int(input())
l=[]
for i in range(n):
    l.append(int(input()))
k=int(input())
s=0
for i in l:
    if i<=k:
        s=s+1
    else:
        s=s+2
print(s)