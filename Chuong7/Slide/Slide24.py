
def NhapSo(tb):
    while True:
        a=input(tb)
        if a.isnumeric():
            return int(a)
        else:
            print("Khong hop le!")


a=NhapSo("a=")
b=NhapSo("b=")
print("a=",a,sep="")
print("b=",b,sep="")

        
    
    