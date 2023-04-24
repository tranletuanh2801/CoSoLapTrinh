L=[]
while True:
    n=int(input())
    L=L+[n]
    if n==0:
        L.remove(n)
        break   
L.reverse()
for n in L:
    print(n)
 
