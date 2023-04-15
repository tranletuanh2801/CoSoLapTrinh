import math
def LaSoNguyenTo(x):
    if x<2:
        return False
    for i in range(2,int(math.sqrt(x)+1)):
        if x%i==0:
            return False
    return True
def SoHopLe(x):
    if x<=1:
        return True
    return False
def NhapVaDem():
    print("Nhap day so:")
    dem=0
    
    while True:
        x =int(input())
        if SoHopLe(x):
            break
        else:
            if LaSoNguyenTo(x):
                dem+=1
    return dem
def InKQ(kq):   
    print("Co", kq, "so nguyen to")

kq= NhapVaDem()
InKQ(kq)
