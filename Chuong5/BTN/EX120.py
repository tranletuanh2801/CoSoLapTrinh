def Nhap():  
    n=input("Nhap danh sach cac so, cach nhau boi dau phay: ")
    b=n.split(",")
    return b
def SapXep(L):
    if L==sorted(L) or L==sorted(L,reverse=True):
        return True
    else: 
        return False     
L=Nhap()
print(SapXep(L))


