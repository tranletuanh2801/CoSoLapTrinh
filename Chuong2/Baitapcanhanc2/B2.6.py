Hoten=input("Ho ten: ")
ngaycong=int(input("So ngay cong: "))
dongiangaycong=int(input("Don gia ngay cong: "))
phucap=float(input("He so phu cap: "))
tamung=int(input("Tam ung: "))
Luong=dongiangaycong*ngaycong*phucap
ThucLinh=Luong-tamung
print("Nhan vien ",Hoten,", Co tien luong=",Luong,", Tam ung=",tamung," va Thuc linh=",ThucLinh,sep="")