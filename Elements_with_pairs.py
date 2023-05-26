n=int(input())
lst=list(map(int,input().split()))
if n%2==1:
    lst.append(0)
print(*lst)