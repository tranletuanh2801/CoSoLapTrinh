while True:
    n=int(input())
    # if n<0:
    #     break
    s=1
    if n==0 or n==1:
        s=1
        print(s)
    elif n>1:
        i=2
        while i<=n:
            s=s*i
            i=i+1
    
        print(s)
    else:
        break
    
#giai thừa