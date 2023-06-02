n=int(input())
lst=list(map(int,input().split()))
c=0
for i in range(n):
    r=lst[i]
    s=0
    while lst[i]:
        s=s*10+lst[i]%10
        lst[i]=lst[i]//10
        if r==s:
            c=c+1
print(c)