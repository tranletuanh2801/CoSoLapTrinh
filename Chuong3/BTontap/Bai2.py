# n=int(input("n="))
# if n%2==1 and n/n==1:
#     print(n,"la SNT")
# else:
#     print(n,"khong la SNT")
n=int(input("n="))
# if n==2:
#     print(n,"la SNT")
if n>=2 and n<=100: #if n>2 and n<=100:
    for i in range(2,n):
        if n%i==0:
            print(n,"khong la SNT")
            break
    else:
        print(n,"la SNT")
#c3
# n=int(input())
# SNT=True #Biến cờ
# for i in range (2,n):
#     if n%i==0:
#         SNT=False
#         break
# if  SNT==True:
#     print(n,'la SNT')
# else:
#     print(n,'khong la SNT')

