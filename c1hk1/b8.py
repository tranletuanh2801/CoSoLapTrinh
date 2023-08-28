a1=int(input('a1='))
b1=int(input('b1='))
a2=int(input('a2='))
b2=int(input('b2='))
from fractions import Fraction
if b1==0 or b2==0:
    print('Khong xac dinh')
else:
    print('Tong hai phan so(a1/b1+a2/b2)=',(Fraction(a1,b1)+(Fraction(a2,b2))))