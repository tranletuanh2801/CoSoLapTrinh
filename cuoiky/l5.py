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
# n = input()
# tong = 0
# for i in range(len(n)):
#     if n[i].isnumeric():
#         if n[i - 1] == '-':
#             tong -= int(n[i])
#         else:
#             tong += int(n[i])
# print(tong)

# # cau3 xao khoan trang
# n = input()
# for i in n:
#     if i.isspace():
#         n = n.replace(i,'')
# print(n)

# # cau 1. chan/le
# chan = []
# le = []
# n = input().split()
# for i in n:
#     if int(i) % 2 == 0:
#         chan.append(int(i))
#     else:
#         le.append(int(i))
# print(le)
# print(chan)

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
