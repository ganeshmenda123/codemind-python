import math
n=int(input())
l=list(map(int,input().split()))
s=0
for i in l:
    if math.sqrt(i)==int(math.sqrt(i)):
        s=s+i
print(s)