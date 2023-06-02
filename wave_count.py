n=int(input())
lst=list(map(int,input().split()))
c=0
for i in range(1,n-1):
    if (lst[i]<lst[i+1] and lst[i]<lst[i-1] or lst[i]>lst[i+1] and lst[i]>lst[i-1]):
        c=c+1
if c==n-2:
    print((n-1)//2)
else:
    print("-1")
        