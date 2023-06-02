n=int(input())
lst=list(map(int,input().split()))
c=[]
for i in range(n):
    s=0
    while lst[i]:
        s=s*10+lst[i]%10
        lst[i]=lst[i]//10
    c.append(s)
for i in range(n):
    print(c[i],"",end="")