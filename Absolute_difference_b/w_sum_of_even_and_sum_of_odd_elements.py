n=int(input())
lst=list(map(int,input().split()))
cnt=0
cn=0
for i in lst:
    if i%2==0:
        cnt+=i
    else:
        cn+=i
print(abs(cnt-cn))
    