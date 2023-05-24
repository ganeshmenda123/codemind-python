n=int(input())
lst=list(map(int,input().split()))
a=0
for i in range(n-2):
    if lst[i]%2 and lst[i+2]%2 and lst[i+1]%2==0:
        a+=1
print(a)