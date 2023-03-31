# def Taxi():
#     m=float(input("m="))
#     km=m*0.001
#     Gia_ve_co_ban=4.00
#     Gia_ve=0.25*(140*km)
#     Gia=Gia_ve_co_ban+Gia_ve
#     return Gia



def tinh_gia_ve(km):
    # Chuyển đổi quãng đường từ km sang mét
    m = km*1000
    Gia_ve_co_ban=4.00
    Phi_phu_thu=0.25
    so_don_vi_phu_thu=m//140
    phi=Phi_phu_thu*so_don_vi_phu_thu
    gia_ve=Gia_ve_co_ban+phi
    return gia_ve
km=float(input("Nhap quang duong da di (km): "))
gia=tinh_gia_ve(km)
print("Tong gia ve taxi la:",gia,"do la")
    # tính giá vé theo công thức đã cho
    # base_fare = 4.00
    # distance_fare = (distance_meters / 140) * 0.25
    
    # total_fare = base_fare + distance_fare
    # return total_fare

