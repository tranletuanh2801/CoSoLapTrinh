So_am=[]
So_Khong=[]
So_Duong=[]
while True:
    x=input()
    if x=='':
        break
    x=int(x)
    if x<0:
        So_am.append(x)
    elif x==0:
        So_Khong.append(x)
    else:
        So_Duong.append(x)
for x in So_am:
    print(x)
for x in So_Khong:
    print(x)
for x in So_Duong:
    print(x)

