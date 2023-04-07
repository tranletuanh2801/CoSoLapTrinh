import math
def nhap():
    print("Nhap 3 so nguyen:")
    a=float(input("a="))
    b=float(input("b="))
    c=float(input("c="))
    return a,b,c
def giaipt(a,b,c):
    d=b*b-4*a*c
    if d<0:
        return "Phuong trinh vo nghiem"
        # print("Phuong trinh vo nghiem")
    elif d==0:
        x1=(-b/2*a)
        return x1
        # print("Phuong trinh co nghiem kep")
        # print("x1=x2=",x,sep="")
    else:
        x1=(-b+math.sqrt(d))/2*a
        x2=(-b-math.sqrt(d))/2*a
        return x1,x2
        # print("Phuong trinh co hai nghiem")
        # print("x1=",x1,sep="")
        # print("x2=",x2,sep="")
def inkq(x1, x2):
    if giaipt(a,b,c):
        print("Phuong trinh vo nghiem")
    elif giaipt(a,b,c):
        print("Phuong trinh co nghiem kep")
        print("x1=x2=",x1,sep="")
    else:
        print("Phuong trinh co hai nghiem")
    # print("Nghiem cua phuong trinh la:")
        print("x1=",x1,sep="")
        print("x2=",x2,sep="")
a,b,c=nhap()
x1,x2=giaipt(a,b,c)
inkq(x1,x2)
