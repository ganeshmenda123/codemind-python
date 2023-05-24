n=int(input())
lst=list(map(int,input().split()))
a=[]
b=[]
for i in lst:
    if i%2==0:
        a.append(i)
    elif i%2==1:
        b.append(i)
print(*a+b)
    