def Input():
    n=int(input("n="))
    L=[]
    for i in range(n):
        a=int(input())
        L.append(a)
    return L
def dem(L):
    dem=0
    for i in range(len(L)):
        if L[i]>0:
            dem+=1
    print("SND=",dem,sep="")   
def TBC(L):
    sum=0
    d=0
    for i in range(len(L)):
        if L[i]%2==0:
            sum+=L[i]
            d+=1
    if d>0:
        print("TBC=",sum/d,sep="")
    else:
        print("TBC=",0,sep="")       
L=Input()
dem(L)
TBC(L)     

        