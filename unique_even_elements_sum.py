n=int(input())
lst=list(map(int,input().split()))
a=[]
b=[]
for i in lst:
    if i not in a:
        a.append(i)
for i in a:
    if i%2==0:
        b.append(i)
print(sum(b))