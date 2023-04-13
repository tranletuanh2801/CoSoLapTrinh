def tinh_gia_tien(distance):
    gia_goc = 4.0
    don_gia = 0.25
    so_don_vi = distance / 140
    gia_tien = gia_goc + don_gia * so_don_vi
    return round(gia_tien, 2)
distance = float(input("Nhap khoang cach di chuyen (tinh bang met): "))
print("Tong chi phi la:", tinh_gia_tien(distance),"$",sep=" ")

