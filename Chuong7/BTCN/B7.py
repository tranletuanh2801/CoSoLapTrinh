import re
string = input()
# Tìm chuỗi email trong chuỗi đầu vào bằng biểu thức chính quy
match = re.search(r'[\w\.-]+@[\w\.-]+\.[\w\.]+', string)
# In kết quả tìm được hoặc in chuỗi rỗng nếu không tìm thấy
if match:
    print(match.group())
else:
    print()
