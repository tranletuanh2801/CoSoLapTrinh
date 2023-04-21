# Nhập từ bàn phím 2 số nguyên x, k;
# Nhập một số nguyên n và n số nguyên lưu vào list L;
# Hàm add(L, x, k) thêm phần tử x vào List L tại vị trí index k, nếu
# k lớn hơn số phần tử của L thì thêm x vào cuối L;
def Nhap():
    x=int(input())
    k=int(input())
    n=int(input())
    L=[]
    for i in range(n):
        a=int(input())
        L=L+[a]
    return L,x,k   
def add(L,x,k):
    # if k>len(L):
    #     L=L+[x]
    # elif k==0:
    #     L=[x]+L
    # else: 
    L=L[:k]+[x]+L[k:]
    print(L)
L,x,k=Nhap()
add(L,x,k)


