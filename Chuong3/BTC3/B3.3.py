x=float(input("x="))
y=float(input("y="))
ch=input("Phep toan:")
if ch=="+":
    a=round(x+y,1)
    print(x,"+",y,"=",a,sep="")
elif ch=="-":
    a=round(x-y,1)
    print(x,"-",y,"=",a,sep="")
elif ch=="*":
    a=round(x*y,1)
    print(x,"*",y,"=",a,sep="")
elif ch=="/":
    if y==0:
        print("Khong hop le")
    else:
        a=round(x/y,1)
        print(x,"/",y,"=",a,sep="")
else:
    print("Khong hop le")
    
    

    

    