n=int(input())
lst=list(map(int,input().split()))
c=0
for i in range(n):
    while lst[i]:
        c=c+lst[i]%10
        lst[i]=lst[i]//10
print(c)