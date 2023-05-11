st='''--Người---đâu-gặp---gỡ-làm-chi---
Trăm----năm-biết-có---duyên---gì--hay--không.
Ngổn-ngang---trăm-mói---bên---lòng----
----Nên-câu---tuyệt--diệu-ngụ-trong-tính-tình.'''
def XuLyDong(xau):
    L=xau.split('-') #tách mỗi từ trong xâu bằng dấu -
    while '' in L: #Xoá tất cả các ký tự rỗng trong list L
        L.remove('')
    return ' '.join(L)  # nối mỗi từ trong L thành một xâu st

def TienXuLy(st):
    L=st.split('\n') #tách mỗi dòng thành 1 phần tử của list L
    for dong in L:
        print(XuLyDong(dong)) #Xử lý từng dòng

TienXuLy(st)
