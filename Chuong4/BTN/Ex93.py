def nextPrime(n):
    while True: 
        if n < 0: 
            print('Khong hop le, nhap lai:')
            n = float(input())
        elif n != int(n): 
            print('Khong hop le, nhap lai:')
            n = float(input())
        else: 
            break
    n = int(n)
    n = n+1
    while True:
        for i in range(2,n): 
            if n%i == 0: 
                n = n+1
                break
        else: 
            print( n)
            break
def Nhap():
    number = float(input())
    nextPrime(number)
Nhap()