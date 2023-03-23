n=int(input("Nhap so n="))
s=0 #số lượng số đã in trên một dòng
for i in range(1,n+1):
        print(i,end=" ")
        s=s+1
        if s==10:
            print()
            s=0
           
    