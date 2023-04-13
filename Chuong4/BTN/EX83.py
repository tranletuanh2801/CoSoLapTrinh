def Nhap():
    sosanpham=int(input('So mon hang trong don hang:'))
    return sosanpham
def tong_chi_phi(sosanpham):
    sanphamdau = 10.95
    sanphamtt = 2.95
    tong = sanphamdau + (sosanpham - 1) * sanphamtt
    return tong
def InKQ(tong):
    print('Tong chi phi van chuyen don hang la: $',tong,sep='')
sosanpham=Nhap()
tong=tong_chi_phi(sosanpham)
InKQ(tong)