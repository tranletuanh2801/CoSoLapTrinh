n=int(input())

s=1
if n==0 or n==1:
    s=1
    print(s)
else:
    for i in range(2,n+1):
        s=s*i
        print(s)
        if n<0:
            break


   
    