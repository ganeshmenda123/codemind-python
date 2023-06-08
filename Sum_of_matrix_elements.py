s=0
m=int(input())
n=int(input())
for i in range(m):
    lst=list(map(int,input().split()))
    s=s+sum(lst)
print(s)