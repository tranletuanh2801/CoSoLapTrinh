a=int(input("Tien thu="))
if a<=100:
    s=a*100
    VAT=s*0.1
    S=s+VAT
    print("Phai tra=",S)
elif 101<=a<=150:
    s=100*550+(a-100)*750
    VAT=s*0.1
    S=s+VAT
    print("Phai tra=",S)
elif 151<=a<=200:
    s=100*550+50*750+(a-150)*950
    VAT=s*0.1
    S=s+VAT
    print("Phai tra=",S)
else:
    s=100*550+50*750+50*950+(a-200)*1350
    VAT=s*0.1
    S=s+VAT
    print("Phai tra=",S)