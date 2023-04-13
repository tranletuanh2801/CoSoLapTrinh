def add(L,x,k):
    if k>len(L):
        L=L+[k] # them vao cuoi
    else: #chèn vào vị trí k
        L=L[:k-1]+[x]+L[k-1:]
    return L
L=[1,2,3,4,5]
x=10
k=3
L=add(L,x,k)
print(L)
