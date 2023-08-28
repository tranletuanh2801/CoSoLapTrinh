n=int(input('n='))
giaithua=1
if n==0 or n==1:
    print(n,'!=',giaithua,sep='')
else:
    for i in range(2,n+1):
        giaithua=giaithua*i
    print(n,'!=',giaithua,sep='')