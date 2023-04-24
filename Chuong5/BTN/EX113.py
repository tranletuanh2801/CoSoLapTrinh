def Dinh_dang(L):
    if len(L)==1:
        return L[0]
    elif len(L)==2:
        return L[0]+" and "+L[1]
    else:
        return ", ".join(L[:-1])+" and "+L[-1]
L=[]
while True:
    n=input()
    if n=='':
        break
    L.append(n)
format_list=Dinh_dang(L)
print(format_list)
