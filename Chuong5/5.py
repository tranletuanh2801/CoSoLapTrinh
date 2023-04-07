def nhap():
    print("Nhap 10 so nguyen:")
    L=[]
    for i in range(0,10):
        n=int(input())
        L=L+[n] #a=a+[int(input())]
    x=int(input("Nhap so nguyen x:"))
    return L,x
def inkq(L):
    for x in L:
        print(x,end=", ")
def CauA(L,x):
    for i in range(len(L)):
        if L[i]==5:
            L[i]=x
    inkq(L) 
def CauB(L,x):
    i=0
    while i<len(L):
        if L[i]==x:
            del(L[i])
        else:
            i+=1
    print("\nSau khi xoa x khoi tap L:")
    inkq(L)            
L,x=nhap()
CauA(L,x)
CauB(L,x)
