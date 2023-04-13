def nhap():
    a=float(input("a="))
    b=float(input("b="))
    c=float(input("c="))
    return a,b,c
def trung_vi(a,b,c):
    if a<b<c:
        print(b)
    if b<a<c:
        print(a)
    if a<c<b:
        print(c)
a,b,c=nhap()
trung_vi(a,b,c)    
    