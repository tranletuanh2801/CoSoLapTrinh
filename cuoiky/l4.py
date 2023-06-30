# Cho một danh sách và một từ, viết chương trình để chèn một phần tử vào trước mỗi phần tử của danh sách
# -INPUT nhập vào dòng thứ 1 là một dãy các từ, mỗi từ cách nhau đúng 1 ký tự trắng. Dòng thứ 2 là 1 từ
# -OUTPUT in lên màn hình một danh sách mới gồm các phần tử chung từ hai danh sách trên
# INPUT
# Red Green Black
# Blue
# OUTPUT
# ['Blue', 'Red', 'Blue', 'Green', 'Blue', 'Black']

# def nhap():
#     st=input().split(' ')
#     a=input()
#     return st,a
# def Xuly(st,a):
#     L=[]
#     for i in st:
#         L.append(a)
#         L.append(i)
#     print(L)
# st,a=nhap()
# Xuly(st,a)


# Viết chương trình để tạo một danh sách mới gồm các phần tử chung từ hau danh sách cho trước
# -INPUT nhập vào hai dòng, mỗi dòng là một dãy các từ, mỗi từ cách nhau đúng 1 ký tự trắng
# -OUTPUT in lên màn hình một danh sách mới gồm các phần tử chung từ hai danh sách trên
# INPUT
# Red Green White Organge
# Green Black White Pink
# OUTPUT
# ['Green', 'White']

# def nhap():
#     st1=input().split(' ')
#     st2=input().split(' ')
#     return st1,st2
# def XuLy(st1,st2):
#     L=[]
#     for i in st1:      for i in st1:
#         if i in st2:       for j in st2:   if i==j:   L.append(j)
#             L.append(i)
#     print(L)
# st1,st2=nhap()
# XuLy(st1,st2)   


# Viết chương trình để loại bỏ các ký tự không mong muốn khỏi một chuỗi đã cho. Biết rằng, các ký tự không mong muốn bao gồm #,^,%,*,!
# INPUT nhập vào một chuỗi đã được loại bỏ các ký tự không mong muốn
# OUTPUT in lên màn hình chuỗi đã được loại bỏ các ký tự không mong muốn
# INPUT
# Pyth*^on Execris^es
# OUTPUT
# Python Execrises

# def nhap():
#     st=input()
#     kytu=['#','%','^','*']
#     return st,kytu
# def Xuly(st,kytu):
#     st1=st
#     for i in kytu:
#         st1=st1.replace(i,'')
#     print(st1)
# st,L=nhap()
# Xuly(st,L)


# cho 3 chuỗi ký tự, viết chương trình đảo ngược các ký tự của chuỗi và in kết quả lên màn hình
# -INPUT nhập vào 3 dòng, mỗi dòng là 1 chuỗi ký tự
# -OUTPUT in lên màn hình các chuỗi ký tự đã được đảo ngược các ký tự
# INPUT
# python
# list
# ver
# OUTPUT
# nohtyp
# tsil

# KQ = []
# for i in range(3):
#     L = []
#     x = input()
#     char = list(x)
#     char.reverse()
#     KQ.append(char)
# for i in KQ:
#     print(''.join(i))