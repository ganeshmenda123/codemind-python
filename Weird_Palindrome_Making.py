for i in range(int(input())):
    n=int(input())
    li=list(map(int,input().split()))
    l=[i for i in li if i%2!=0]
    print(len(l)//2)