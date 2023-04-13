def namnhuan(n):
    if n%100!=0 and n%4==0:
        return True
    elif n%100==0 and n%400==0:
        return True
    return False
def kiemtra(t,n):
    if t==1: T = 31
    if t==2:
        if namnhuan(n)==True: T = 28
        if namnhuan(n)==False: T = 29
    if t==3: T = 31
    if t==4: T = 30
    if t==5: T = 31
    if t==6: T = 30
    if t==7: T = 31
    if t==8: T = 31
    if t==9: T = 30
    if t==10: T = 31
    if t==11: T = 30
    if t==12: T = 31
    return T
def magicday(T,t,n):
    for i in range(1,T+1):
        if i*t==n%100: 
            print(str(i) +'/' + str(t) + '/' + str(n))
print('Magic day trong the ki 20 la:')
for n in range(1900, 2000):
    for t in range(1, 13): 
            T = kiemtra(t,n)
            magicday(T,t,n)
    