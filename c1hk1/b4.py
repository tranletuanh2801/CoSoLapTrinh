n=int(input('n='))
print('Tat ca cac so nguyen to tu 1 den n:')
for i in range(2,n+1):
    d=0
    for j in range(2,i):
        if i%j==0:
            d=1
    if d==0:
        print(i,end=' ')
