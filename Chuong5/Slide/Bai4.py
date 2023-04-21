# Nhập một số nguyên n và n số nguyên lưu vào list L
# Hàm count(L) trả về số lượng phần tử trong List L;
def Nhap():   
    n=int(input())
    L=[]
    for i in range(n):
        a=int(input())
        L=L+[a]
    return L
def count(L):
    dem=0
    for i in L:
        dem=dem+1
    print(dem)
L=Nhap()
count(L)

