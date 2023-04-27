def Nhap():
    L=input("Nhap danh sach L (cach nhau boi dau cach): ")
    lst=L.split()
    L1=input("Nhap danh sach con L1 (cach nhau boi dau cach): ")
    lst1=L1.split()
    L2=input("Nhap danh sach con L2 (cach nhau boi dau cach): ")
    lst2=L2.split()
    return lst,lst1,lst2
def isSublist(DScon, DSlon):
    if DScon==[]:
        return True
    if DSlon==[]:
        return False
    if DScon[0] == DSlon[0]:
        return isSublist(DScon[1:],DSlon[1:])
    return isSublist(DScon,DSlon[1:])

L,L1,L2=Nhap()
print(isSublist(L1,L)) 
print(isSublist(L2,L))
