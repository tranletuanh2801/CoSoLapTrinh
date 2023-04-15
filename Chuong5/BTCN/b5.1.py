def Input():
    n=int(input("n="))
    L=[]
    for i in range(n):
        a=int(input())
        L.append(a)
    x=int(input("x="))
    return L,x
def FirstAndLast(L):
    L1=[L[0],L[-1]]
    print(L1)
def Search(L,x):
    if x in L:
        return True
    return False
L,x=Input()
FirstAndLast(L)
print(Search(L,x))