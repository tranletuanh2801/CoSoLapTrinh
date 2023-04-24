def KiemTraMatKhau():
    while True:
        MatKhau=input()
        if (len(MatKhau)>=8) and any(i.isnumeric() for i in MatKhau) and any(i.isupper() for i in MatKhau) and any(i.islower() for i in MatKhau):
            print('Hop le')
            break
mk=KiemTraMatKhau()


# while True:    
#     str=input()
#     if len(str)<8 or str.islower() or str.isupper() or str.isnumeric() or str.isalpha():
#         print("Khong hop le!!!")
#     else:
#         print("Hop le!!!")
#         break

