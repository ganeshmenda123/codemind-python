n=int(input())
l=list(map(int,input().split()))
a=[]
for i in l:
    a.append(i**2)
a.sort()
for i in a:
    print(i,"",end="")