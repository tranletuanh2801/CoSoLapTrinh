def nhap():
    n=int(input())
    return n
def so_thu_tu(n):
    if n < 1 or n > 12:
        t="nhap tu so 1 đến 12"
    elif n == 1:
        t="first"
    elif n == 2:
        t="second"
    elif n == 3:
        t="third"      
    elif n == 4:
        t="fourth"   
    elif n == 5:
        t="fifth"  
    elif n == 6:
        t="sixth"
    elif n == 7:
        t="seventh"
    elif n == 8:
        t="eighth"
    elif n == 9:
        t="ninth"
    elif n == 10:
        t="tenth"
    elif n == 11:
        t="eleventh"
    else:
        t="twelfth"
    return t
def inkq(t):
    print(t)
n=nhap()
t=so_thu_tu(n)
inkq(t)