def Nhap():
    n=int(input())
    if n>=2 : 
        for i in range(2,n):
            if n%i==0:
                print("Flase")
                break
        else:
            print("True")
Nhap()