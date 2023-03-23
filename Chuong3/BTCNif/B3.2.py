Muc1=int(input("M1="))
Muc2=int(input("M2="))
Muc3=int(input("M3="))
Dien_nang=int(input("S="))
if Dien_nang<=100:
    t=Muc1*Dien_nang
elif Dien_nang<=150:
    t=100*Muc1+(Dien_nang-100)*Muc2
else :
    t=100*Muc1+50*Muc2+(Dien_nang-150)*Muc3
print("Phai tra=",t,sep="")
