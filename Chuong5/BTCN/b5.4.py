def Input():
    n=int(input("n="))
    L=[]
    for i in range(n):
        a=int(input())
        L.append(a)
    return L
def DaoNguoc(L):
    L.reverse()
    print(L)
def SapXep(L):
    L.sort()
    print(L) 
L=Input()
DaoNguoc(L)
SapXep(L)