def Taxi():
    m=float(input("m="))
    km=m*0.001
    Gia_ve_co_ban=4.00
    Gia_ve=0.25*(140*km)
    Gia=Gia_ve_co_ban+Gia_ve
    return Gia



# def tinh_gia_ve(distance):
#     # Chuyển đổi quãng đường từ km sang mét
#     distance_meters = distance * 1000
    
#     # tính giá vé theo công thức đã cho
#     base_fare = 4.00
#     distance_fare = (distance_meters / 140) * 0.25
    
#     total_fare = base_fare + distance_fare
#     return total_fare

