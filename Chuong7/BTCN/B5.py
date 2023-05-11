def Nhap():
    str=input().split(' ')
    x=int(input())
    return str,x
def In(str,x):

    for i in range(len(str)):
        if int(str[i])==x:
            return i+1
    return 0
str,x=Nhap()
print(In(str,x))   
    
