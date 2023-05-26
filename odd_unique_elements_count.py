n=int(input())
lst=list(map(int,input().split()))
lis=[]
c=0
for i in lst:
    if i%2==1 and i not in lis:
        lis.append(i)
        c+=1
print(c)
 