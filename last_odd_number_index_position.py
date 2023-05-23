n=int(input())
lst=list(map(int,input().split()))
cnt=0
for i in range(len(lst)):
    if lst[i]%2!=0:
        cnt=i
print(cnt)