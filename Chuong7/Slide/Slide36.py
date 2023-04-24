# st='''--Người---đâu-gặp---gỡ-làm-chi---
# Trăm----năm-biết-có---duyên---gì--hay--không.
# Ngổn-ngang---trăm-mói---bên---lòng----
# ----Nên-câu---tuyệt--diệu-ngụ-trong-tính-tình.'''
# L=st.split('-')
# print(L)


text = "--Người---đâu-gặp---gỡ-làm-chi---\nTrăm----năm-biết-có---duyên---gì--hay--không.\nNgổn-ngang---trăm-mối---bên---lòng----\n----Nên-câu---tuyệt--diệu-ngụ-trong-tính-tình."

# Xóa các ký tự "-" thừa ở đầu và cuối câu
text = text.strip("-")

# Xóa các ký tự "-" thừa ở giữa câu và thay thế bằng khoảng trắng
text = text.replace("--", " ")
text = text.replace("---", " ")

# Chuẩn hóa khoảng trắng
text = " ".join(text.split())

# Viết hoa chữ cái đầu tiên của mỗi câu
text = ". ".join([sentence.capitalize() for sentence in text.split(".")])

# In đoạn văn bản đã được xử lý
print(text)
