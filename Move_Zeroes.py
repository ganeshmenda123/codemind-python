n=int(input())
l=list(map(int,input().split()))
a=[]
for i in l:
    if i>0:
        a.append(i)
for i in a:
    print(i,"",end="")
for i in range(len(l)-len(a)):
    print("0","",end='')