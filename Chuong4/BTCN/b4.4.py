def nhap():
    print("Nhap 3 so nguyen:")
    a=int(input("a="))
    b=int(input("b="))
    c=int(input("c="))
    return a,b,c
def max3(a,b,c):
    kq=a
    if(b>kq):
        kq=b
    if(c>kq):
        kq=c
    return kq
def inkq(kq):
    print("So lon nhat la: ",kq,sep="")
a,b,c=nhap()
kq=max(a,b,c)
inkq(kq)