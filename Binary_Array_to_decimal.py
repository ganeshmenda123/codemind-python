n=int(input())
lst=list(map(int,input().split()))
lst.reverse()
sm=0
for i in range(len(lst)):
    sm=sm+((2**i)*lst[i])
print(sm)
    