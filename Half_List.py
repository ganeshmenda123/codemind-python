n=int(input())
l=list(map(int,input().split()))
for i in range(len(l)-1,len(l)//2-1,-1):
    print(l[i],"",end="")
for i in range(0,len(l)//2):
    print(l[i],"",end="")