def nhap():
    a = float(input())
    b = float(input())
    c = float(input())
    return a,b,c
def canh_tam_giac(a,b,c):
    if (a+b<=c) or (b+c<=a) or (c+a<=b):
        return False
    else:
        return True
def inkq():
    if canh_tam_giac(a, b, c):
        print(a,",",b,",",c ,"có thể tạo thành một tam giác.")
    else:
        print(a,",",b,",",c ,"không thể tạo thành một tam giác.")
    return
a,b,c=nhap()
canh_tam_giac(a,b,c)
inkq()



