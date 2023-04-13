#Nhập từ bàn phím một số nguyên x, nếu x tồn tại trong tập L thì
#thực hiện xoá x khỏi tập L
# L=[1,2,3,4,5]
# x=int(input("x="))
# i=0
# while i<len(L):
#     if L[i]==x:
#         del(L[i])
#     i+=1
# print("sau khi xoa:")        
# print(L)
 #nhập x nếu tồn tại thì xoá, còn lại thì thêm x vào L
L=[1,2,3,4,5]
x=int(input("x="))
i=0
if x in L:
    while i<len(L):
        if L[i]==x:
            del(L[i])
        i+=1
else: #k tồn tại thì thêm x
    L=L+[x] #thêm phần tử x vào tập L
print("sau khi xu ly:")        
print(L)