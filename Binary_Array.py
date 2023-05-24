n=int(input())
lst=list(map(int,input().split()))
r=len(lst)
c=0
for i in lst:
    if i==0 or i==1:
        c+=1
if c==r:
    print("True")
else:
    print("False")