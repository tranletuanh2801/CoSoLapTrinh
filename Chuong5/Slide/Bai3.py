# Nhập từ bàn phím  số nguyên x
# Nhập một số nguyên n và n số nguyên lưu vào list L
# Hàm delete(L, x) xóa tất cả phần tử có giá trị bằng x trong List L
def Nhap():
    x=int(input())
    n=int(input())
    L=[]
    for i in range(n):
        a=int(input())
        L=L+[a]
    return L,x
def delete(L,x):
    M=[]
    for z in L:
        if z!=x:
            M=M+[z]
    print(M)
    # i=0
    # while i<len(L):
    #     if x==L[i]: #i là index của phần tử cần xoá
    #         L=L[:i]+L[i+1:]
    #     else:
    #         i+=1       
    # print(L)

L,x=Nhap()
delete(L,x)
            