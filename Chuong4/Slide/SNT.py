import math
def nhap():
    n=int(input("n="))
    return n
def SNT(x):
    # if n<2:
    #     False
    for i in range(2,int(math.sqrt(x)+1)):
        if x%i==0:
            return False
        
    return True
def inkq(n):
    dem=0
    k=2
    while (dem<n):
        if SNT(k)==True:
            print(k,end=", ")
            dem+=1
        k+=1
    
   
n=nhap()
inkq(n)        