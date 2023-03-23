while True:
    a=float(input("a="))
    b=float(input("b="))
    ch=input("Toan tu:")
    if ch=="+":
        x=a+b
        print(a,ch,b,"=",x,sep="")
    elif ch=="-":
        x=a-b
        print(a,ch,b,"=",x,sep="")
    elif ch=="*":
        x=a*b
        print(a,ch,b,"=",x,sep="")
    elif ch=="/":
        if a==0 or b==0:
            print("Khong hop le")
        else:
            x=a/b
            print(a,ch,b,"=",x,sep="")
    else:
        print("Khong hop le")
        continue
    tiep_tuc=input("Tiep tuc:")
    if tiep_tuc=="t" or tiep_tuc=="T":
        break
    
    