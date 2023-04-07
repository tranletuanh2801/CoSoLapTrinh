import math
def nhap():
    n=int(input("n="))
    return n
def SNT(n):
    if n<2:
        False
    for i in range(2,int(math.sqrt(n)+1)):
        if n%i==0:
            return False
        
    return True
def inkq(n):
    if SNT(n):
        print(n,"la SNT")
    else:
        print(n,"khong la SNT")
n=nhap()
inkq(n)        
    
