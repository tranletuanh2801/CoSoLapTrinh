def thang():
    t = int(input('Nhap thang:'))
    if 1<=t<=12:
        return t
def nam(n): 
    if n%100!=0 and n%4==0:
        return True
    elif n%100==0 and n%400==0:
        return True
    return False
def kiemtra(t,n):
        if t==1: print('Thang 1 co 31 ngay')
        if t==2:
            if nam(n)==True: print('Thang 2 nam', n, 'co 29 ngay')
            if nam(n)==False: print('Thang 2 nam', n, 'co 28 ngay')
        if t==3: print('Thang 3 nam', n, 'co 31 ngay')
        if t==4: print('Thang 4 nam', n, 'co 30 ngay')
        if t==5: print('Thang 5 nam', n, 'co 31 ngay')
        if t==6: print('Thang 6 nam', n, 'co 30 ngay')
        if t==7: print('Thang 7 nam', n, 'co 31 ngay')
        if t==8: print('Thang 8 nam', n, 'co 31 ngay')
        if t==9: print('Thang 9 nam', n, 'co 30 ngay')
        if t==10: print('Thang 10 nam', n, 'co 31 ngay')
        if t==11: print('Thang 11 nam', n, 'co 30 ngay')
        if t==12: print('Thang 12 nam', n, 'co 31 ngay')
t = thang()
n = int(input('Nhap nam:'))
kiemtra(t,n)
