def Nhap():
    str=list(map(int,input().split(' ')))
    s=int(input())
    return str,s
def XuLy(st,s):
    vi_tri=[]
    for i in range(len(str)):
        if str[i]==s:
            vi_tri.append(i+1)       
    if len(vi_tri)==0:
        print('0')
    else:
        for j in vi_tri:
            print(j)          
str,s=Nhap()
XuLy(str,s)
