n=int(input())
l=list(map(int,input().split()))
p=int(input())
cnt=0
for i in range(0,n):
    if p==l[i]:
        cnt+=1
        break
if cnt>0:
    print("True")
else:
    print("False")
