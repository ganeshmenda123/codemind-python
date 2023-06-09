z=int(input())
l=list(map(int,input().split()))
e=0
for i in range(0,len(l),2):
    e=e+l[i]
o=0
for i in range(1,len(l),2):
    o=o+l[i]
if o-e==0:
    print("YES")
else:
    print("NO")