import math
def nhap():
    n=int(input('n='))
    return n
def snt(n):
    for x in range (2,int(math.sqrt(n)+1)):
        if n%x==0:
            return False
    return True
def inKQ(kq,n):
    if kq==True:
        print(n,'la SNT')
    else:
        print(n,'khong la SNT')
    return kq
n=nhap()
kq=snt(n)
inKQ(kq,n)