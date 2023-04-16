def Input():
    n=int(input("n="))
    L=[]
    for i in range(n):
        a=int(input())
        L.append(a)
    return L
def STT_Chan(L):
    sum=0
    for i in range(len(L)):
        if i%2!=0:
            sum+=L[i]
    
    print("Tong=",sum,sep="")
L=Input()
STT_Chan(L)

    