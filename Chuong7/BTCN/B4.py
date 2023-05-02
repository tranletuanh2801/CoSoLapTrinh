str=input()
a=str.split(',')
L=[]
for i in a:
    if i not in L:
        L.append(i)
L.sort()
new=','.join(L)  
print(new) 



