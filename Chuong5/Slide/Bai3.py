def delete(L,x):
    i=0
    while i<len(L):
        if x==L[i]: #i là index của phần tử cần xoá
            L=L[:i]+L[i+1:]
        else:
            i+=1       
    return L
L=[1,2,3,4,5]
x=3
L=delete(L,x)
print(L)
            