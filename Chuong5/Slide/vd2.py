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
# L=[1,2,3,4,5]
# x=int(input("x="))
# i=0
# if x in L:
#     while i<len(L):
#         if L[i]==x:
#             del(L[i])
#         i+=1
# else: #k tồn tại thì thêm x
#     L=L+[x] #thêm phần tử x vào tập L
# print("sau khi xu ly:")        
# print(L)

# L=[1,3,2,3,4,3,5]
# x=int(input("x="))
# i=0
# if x in L:
#     while L.count(x)>0:
#         L.remove(x)# while x in L:
#     #     L.remove(x) # có while để xoá triệt để
#     #30-31 del(L[L.index(x)]) #L.index -> trả về index của x trongL
# else: #k tồn tại thì thêm x
#    L.append(x) #L=L+[x]
# print("sau khi xu ly:")        
# print(L)

#slide 49
# names = ["An","Nam","Binh","Ngoc"]
# names.remove("An")
# del(names[0])
# x=names.pop(-2)
# print(x)
# print(names)

#slide55
import copy
numbers1 = [1, 2, 3, 4, 5]
numbers2 = copy.copy(numbers1)
print(numbers2)
numbers3 = numbers1
numbers3[2] = 6
print(numbers3)