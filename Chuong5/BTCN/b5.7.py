def Input():
    n=int(input("n="))
    L=[]
    for i in range(n):
        a=int(input())
        L.append(a)
    return L
def Loai_Bo(L):
    A=[]
    for i in L:
        if i not in A:
            A.append(i)
    print(A)
L=Input()
Loai_Bo(L)