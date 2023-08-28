#c1
# cannang=float(input())
# chieucao=float(input())
# BMI=cannang/(chieucao*chieucao)
# if BMI<18.5:
#     print('Gay')
# elif 18.5<=BMI<=24.9:
#     print('Binh thuong')
# elif 25.0<=BMI<=29.9:
#     print('Hoi thua can')
# elif BMI >= 30.0:
#         print('Beo phi')
        

#c2
# songuyen=int(input())
# list=list(str(songuyen))
# S=0
# for i in range(len(list)):
#     S+=int(list[i])*int(list[i])*int(list[i])
# if S==songuyen:
#     print(True)
# else: print(False)


#c3
# n=int(input())
# L=[]
# for i in range(n):
#     x=int(input())
#     L+=[x]
# M=[]
# for i in range(len(L)):
#     if L[i] not in M:
#         M+=[L[i]]
# if len(M)==len(L):
#     print(True)
# else: print(False)



#c4
chuoi=input()
chuoi=chuoi.lower()
L=chuoi.split()
a=e=i=o=u=0
for j in range(len(L)):
    List=list(L[j])
    for l in range(len(List)):
        if List[l]=='a':
            a+=1
        elif List[l]=='e':
            e+=1
        elif List[l]=='i':
            i+=1
        elif List[l]=='o':
            o+=1
        elif List[l]=='u':
            u+=1
M=[a,e,i,o,u]
for k in range(len(M)):
    print(M[k])
    
    
#c5
# X=int(input())
# dayso=input().split()
# List=[]
# if str(X) not in dayso:
#     print([0, 0])
# else:
#     for i in range(len(dayso)):
#         if int(dayso[i])==X:
#             D=i
#             List+=[D]
#             break
#     if int(dayso[-1])==X:
#         C=len(dayso)-1
#         List+=[C]
#     else:
#         for i in range(dayso.index(str(X)),len(dayso)):
#             if int(dayso[i])!=X:
#                 C=i-1
#                 break
# # List=[D,C]
#     print(List)
# print(D)
# print(C)


def Nhap():
    n=int(input("n="))
    L=[]
    for i in range(n):
        x=int(input(""))
        L.append(x)
    return L    
def Dem(L):
    for i in L:
        if L.count(i)>=2:
            return False     
    return True
def InKQ(L):
    if Dem(L)==True:
        print("True")
    elif Dem(L)==False:
        print("False")         
L=Nhap()
InKQ(L)



cannang=float(input(""))
chieucao=float(input(""))
BMI=cannang/(chieucao*chieucao)
if BMI<18.5:
    print("Gay")
elif BMI<=24.9:
    print("Binh thuong")
elif BMI<=29.9:
    print("Hoi thua can")
else:
    print("Beo phi")



y=str(input(""))
x=y.lower()
a=x.count("a")
print(a)
e=x.count("e")  #để đếm và tính tổng từng ký tự nguyên âm ở trong chuỗi s
print(e)
i=x.count("i")
print(i)
o=x.count("o")
print(o)
u=x.count("u")
print(u)