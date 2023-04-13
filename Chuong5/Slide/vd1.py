#nhập từ bàn phím một dãy các số nguyên và lưu vào một list L
#việc nhập được dừng lại khi số nhập vào là 0
# nhập một số nguyên n
#cho biết n có nằm trong tập hợp L trên hay không
#vd
#nhap day so:
#2
#5
# 7
# 3
# 5
# 9
# 0
# n=5
# 5 có tồn tại
L=[] #khởi tạo list rổng
print("Nhap day so:")
while True:
    x=int(input())
    L=L+[x] #thêm một phần tử vào list
    if x==0:
        break
n=int(input("n="))
if n in L:
    print(n,"co ton tai")
else:
    print(n,"khong ton tai")    