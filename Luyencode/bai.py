# i=1
# while i<=9:
#     print(" "*(9-i),end="")
#     print("*"*(2*i-1))
#     i+=1   tam giác
    
# i=9
# while i>=1:
#     print("*"*(2*i-1))
#     print(" "*(9-i),end="")
#     i-=1 lỗi tam giác ngược

# n=int(input("n="))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print("",end=" ")
#     for j in range(1,n+2-i):
#         print("*",end=" ")
#     print()  tam giác ngược

a = int(input("Nhập số nguyên dương a: "))
b = int(input("Nhập số nguyên dương b: "))

# Đảm bảo a ≤ b để thuận tiện cho việc tính toán
if a > b:
    a, b = b, a

# Tìm USCLN
while b > 0:
    r = a % b
    a = b
    b = r
uscln = a

# Tìm BSCNN
bscnn = (a * b) // uscln

# In kết quả
print("USCLN của", a, "và", b, "là:", uscln)
print("BSCNN của", a, "và", b, "là:", bscnn)
