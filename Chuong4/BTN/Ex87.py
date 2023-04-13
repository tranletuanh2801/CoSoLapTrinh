def Nhap():
    s,n=input().split()
    return s,n
def tmp(s,n):
    tmp=(int(n)-len(s))//2
    for i in range(0,tmp-1):
        print(' ',end='')
def inkq(s):
    print(s)
s,n=Nhap()
tmp=tmp(s,n)
inkq(s)