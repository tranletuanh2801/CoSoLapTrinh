##input: so nguyen duong n (1<=n<=50)
#output: day so nguyen to, moi so cach nhau boi mot dau cach


n=int(input())
if n<1 or n>50:
    print("nhap lai")
else:
    SNT=True
    for i in range(2,n+1):
        for j in range(2,i):
            if i%j==0:
                SNT==False
                break
        else :
            print(i,end=" ")

# n=int(input())
# print("Cac so nguyen to")
# for i in range(2,n+1):
#     d=0
#     for j in range(2,i):
#         if i%j==0:
#             d=1
#     if d==0:
#         print(i,end=" ")


