def nhap():
    n=int(input("n="))
    return n
def NhapVaDem(n):
    print("Nhap",n,"so nguyen")
    kq=0
    for i in range(1,n+1):
        x=int(input())
        # if x!=0 and x%2==0:
        #     kq+=1
        if x==0:
            continue
        if x%2==0:
            kq+=1
    return kq
def InKQ(kq):
    print("So chu so chan la:",kq)
n=nhap()
kq=NhapVaDem(n)
InKQ(kq)
    
    
    

    