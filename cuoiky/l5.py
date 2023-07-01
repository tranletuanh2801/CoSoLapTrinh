# # cau 3
# '''
# a = input()
# for i in a:
#     if not i.isalnum() and not i.isspace():
#         a = a.replace(i,'')
# print(a)
# '''

# # cau 4 sắp xếp ngược
# # KQ = []
# # for i in range(3):
# #     L = []
# #     x = input()
# #     char = list(x)
# #     char.reverse()
# #     KQ.append(char)
# # for i in KQ:
# #     print(''.join(i))


# # cau 2 #lấy trùng nhau
# L = []
# kq= []
# s1 = input().split(' ')
# s2 = input().split(' ')
# for i in s1:
#     for j in s2:
#         if i == j:
#             kq.append(j)
# print(kq)

# # cau4 tinh tong cac so
def Input():
    st=input()
    return st
def Output(st):
    tong=0
    for i in range(len(st)):
        if st[i].isnumeric():
            if st[i-1]=='-':
                tong-=int(st[i])
            else:
                tong+=int(st[i])
    print(tong)
st=Input()
Output(st)

# # cau3 xao khoan trang
# def Input():
#     st=input()
#     return st
# def Output(st):
#     for i in st:
#         if i.isspace():
#             st=st.replace(i,'')
#     print(st)
# st=Input()
# Output(st)

# # cau 1. chan/le
def Input():
    n=input().split()
    return n
def Output(n):
    L1=[]
    L2=[]
    for i in n:
        if int(i)%2!=0:
            L1.append(int(i))
        else:
            L2.append(int(i))
    print(L1)
    print(L2)
n=Input()
Output(n)

# # cau2 xoa phan tu
# n = input().split()
# if len(n) >= 2:
#     del (n[1])
#     if len(n) >= 3:
#         del (n[2])
#         if len(n) >= 3:
#             del (n[2])
# print(n)

# n = input().split()
# if len(n) >= 5:
#     del (n[1])
#     del (n[2])
#     del (n[2])
# elif len(n) >= 4:
#     del (n[1])
#     del (n[2])
# elif len(n) >= 2:
#     del (n[1])
# print(n)

def Input():
    st=input().split()
    return st
def Output(st):
    if len(st)>=2:
        del(st[1])
        if len(st)>=3:
            del(st[2])
            if len(st)>=3:
                del(st[2])
    print(st)
st=Input()
Output(st)