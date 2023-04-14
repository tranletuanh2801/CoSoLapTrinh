def update(L,x,y):
    for i in range(len(L)):
        if L[i]==x:
            L[i]=y
            
L=[1,2,3,4,5]
L.insert(1,9)  #update(L,2,0)
print(L)