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
    x=a/b
    print(a,ch,b,"=",x,sep="")
tiep_tuc=input("Tiep tuc:")
while True:
    if tiep_tuc=="t" or "T":
        break
    
    