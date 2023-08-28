def Nhap():
    n=int(input('n='))
    return n
def KiemTra(n):
    tong=0
    for i in range(1,n):
        if n%i==0:
            tong=tong+i
    if n==tong:
        return True
    return False
def LietKe(n):
    print('Tat ca so hoan hao tu 1 den n:')
    for i in range(1, n):
        if KiemTra(i):
            print(i,end=' ')
n=Nhap()
LietKe(n)
        