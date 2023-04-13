def Nhap():
    chuoi=input()
    return chuoi
def InHoa(chuoi):
    ch=chuoi.replace('i','I')
    if len(chuoi)>0:
        ch=ch[0].upper()+ch[1:]
    x=0
    while x<len(chuoi):
        if ch[x]=='.' or ch[x]=='!' or ch[x]==',' or ch[x]=='?':
            x=x+1
            while x<len(chuoi) and ch[x]==' ':
                x+=1
            if x<len(chuoi):
                ch = ch[0:x] + ch[x].upper() + ch[x+1:]
        x+=1
    return ch
def InKQ(kq):
    print(kq)
chuoi=input()
kq=InHoa(chuoi)
InKQ(kq)