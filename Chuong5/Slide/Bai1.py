def add(L,x,k):
    if k>len(L):
        L=L+[x]
    elif k==0:
        L=[x]+L
    else: #chèn vào vị trí k
        L=L[:k]+[x]+L[k:]
    return L
L=[1,2,3,4,5,6,7]

L=add(L,10,0)
print(L)
L=add(L,15,3)
print(L)
L=add(L,20,100)
print(L)

