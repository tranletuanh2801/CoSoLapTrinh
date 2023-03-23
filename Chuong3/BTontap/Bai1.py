print("n=",end="")
n=int(input())
if n>=1:
    giaithua=1
    for i in range(1,n+1):
        giaithua=giaithua*i
    print(n,"!=",giaithua,sep="")
elif n==0:
    giaithua=1
    print(n,"!=",giaithua,sep="")
else:
    print("Nhạp lại n>=0")