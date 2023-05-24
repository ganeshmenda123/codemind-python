n=int(input())
lst=list(map(int,input().split()))
a=sum(lst)//n
b=[]
for i in lst:
    if a>=i:
        b.append(i)
print(len(b))