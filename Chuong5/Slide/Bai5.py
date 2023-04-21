# Nhập từ bàn phím 2 số nguyên x, y;
# Nhập một số nguyên n và n số nguyên lưu vào list L;
#Hàm replace(L, x, y) tìm x trong List L và thay thế bằng y;
def Nhap():
    x=int(input())
    y=int(input())
    n=int(input())
    L=[]
    for i in range(n):
        a=int(input())
        L=L+[a]
    return L,x,y 
def update(L,x,y):
    for i in range(len(L)):
        if L[i]==x:
            L[i]=y
    print(L)        
L,x,y=Nhap()
update(L,x,y)