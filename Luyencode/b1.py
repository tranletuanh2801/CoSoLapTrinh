
# Lenh=input()
# if Lenh=='tg':
#     a=float(input())
#     b=float(input())
#     c=float(input())
#     Stg=a+b+c
#     print(Stg)
# elif Lenh== 'ht':
#     bk=float(input())
#     pi=3.14
#     Sht=2*bk*pi
#     print(Sht)


# w= int(input())
# h= int(input())
# mucthue=input()
# khoandonggop=int(input())
# thue=w*h*mucthue
# tlt=w*h+thue+khoandonggop
# tltkt=w*h+thue
# if w%2==0:
#     print()
# if h%2==0:
#         print()
# if mucthue=="A":
#     print(mucthue==0)
# elif mucthue=="B":
#     print(mucthue==0.1)
# elif mucthue=="C":
#     print(mucthue==0.2)
# elif mucthue=="D":
#     print(mucthue==0.29)
# elif mucthue=="E":
#     print(mucthue==0.35)    
# if khoandonggop=="y":
#     khoandonggop==10
#     thue=w*h*mucthue
#     print(tlt)
# elif khoandonggop=="n":
#     print(tltkt)
    
    
    
# a=int(input())
# b=int(input())
# tong=a+b
# if a<=b and a>0 and a<=tong<b:
#     print(a+b)
# else:
#     print("0")   

# for i in range(0,10):
#     for j in range(i+1,101,10):
#         print("{:<3}".format(j),end=" ")
#     print()

# n=int(input("n="))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print("",end=" ")
#     for j in range(1,n+2-i):
#         print("*",end=" ")
#     print() 
     
     
n=int(input("n="))
for i in range(1,n+1):
    for j in range(1,n+1-i):
        print("",end=" ")
    for k in range(1,i+1):
        print("*",end=" ")
    print()