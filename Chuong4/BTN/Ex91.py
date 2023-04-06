def nhap():
    n=input("Nhap toan tu:")
    return n
def precedence(x):
    if x =="+" or x=="-":
        t=1
    elif x=='*' or x=='/':
        t=2
    elif x =='^':
        t=3
    else:
        t=-1
    return t
def inkq(t):
    if t==-1:
        print("Đây không phải toán tử.")
    else:
        print("Độ ưu tiên của toán tử",n,"là",t)
    
n=nhap()
x=precedence(n)
inkq(x)