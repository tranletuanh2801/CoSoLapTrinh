def Input():
    n=int(input("n="))
    L=[]
    for i in range(n):
        a=int(input())
        L.append(a)
    return L
def Loai_Bo(L):
    M=[]
    for i in L:
        if i not in M:
            M.append(i)
    for i in M:
        print(i,end=" ")
L=Input()
Loai_Bo(L)
