def Input():
    L=[]
    for i in range(10):
        a=int(input())
        L.append(a)
    return L
def Hoan_Vi(L):
    B=list(L)
    for i in range(0,len(L)-1,2):
        B[i]=L[i+1]
        B[i+1]=L[i]
    for i in B:
        print(i,end=" ")
L=Input()
Hoan_Vi(L)