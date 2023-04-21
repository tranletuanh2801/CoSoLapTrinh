# Nhập từ bàn phím  số nguyên x
# Nhập một số nguyên n và n số nguyên lưu vào list L;
# Hàm search(L, x) tìm x trong List L, nếu tìm thấy thì trả về index của x trong L, còn lại trả về None
def Nhap():
    x=int(input())
    n=int(input())
    L=[]
    for i in range(n):
        a=int(input())
        L=L+[a]
    return L,x
def search(L,x):
    for i in range(len(L)):
        if x==L[i]:
            return i
    return None
L,x=Nhap()
print(search(L,x))