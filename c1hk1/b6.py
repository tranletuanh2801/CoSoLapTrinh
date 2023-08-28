def Nhap():
    n=int(input('n='))
    print('Nhap',n,'so nguyen:')
    L=[]
    for i in range(n):
        a=int(input())
        L.append(a)
    return L
def KiemTra(L):
    max=L[0]
    for i in range(1,len(L)):
        if L[i]>max:
            max=L[i]
    return max
def Xuat(max):
    print('Phan tu lon nhat la:',max)
L=Nhap()
max=KiemTra(L)
Xuat(max)