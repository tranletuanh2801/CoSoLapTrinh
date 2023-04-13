import math
def Nhap():
    a=int(input('a='))
    b=int(input('b='))
    return a,b
def Tinh(a,b):
    c=int(math.sqrt(a**2+b**2))
    return c
def InKQ(c):
    print('Chieu dai canh huyen=',c,sep='')
a,b=Nhap()
c=Tinh(a,b)
InKQ(c)


