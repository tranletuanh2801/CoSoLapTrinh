def Nhap():
    n=int(input('n='))
    return n
def LaSNT(x):
    for i in range(2,x):  #for i in range(2,n)
        if x%i==0:
            return False
    return True
def InSoNguyenTo(n):
    for i in range(2,n+1):
        if LaSNT(i):
            print(i,end=' ')
# def InKQ(n):
#     if LaSNT(n):
#         print(n,'la SNT')
#     else:
#         print(n,'khong la SNT')
n=Nhap()
InSoNguyenTo(n)

