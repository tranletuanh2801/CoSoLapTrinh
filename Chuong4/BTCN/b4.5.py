def LaSoNguyenTo(x):
    if x < 2:
        return False
    for i in range(2,x+1):
        if x % i == 0:
            return False
    return True
def SoHopLe(x):
    if x <= 1:
        return True
    else:
        return False
def NhapVaDem():
    count = 0
    nums = []
    while True:
        x = int(input("Nhap day so: "))
        if SoHopLe(x):
            break
        nums.append(x)
        if LaSoNguyenTo(x):
            count += 1
    return nums, count

def InKQ(kq):
    nums = kq[0]
    count = kq[1]
    print("Nhap day so:\n", " ".join(map(str, nums)))
    print("Co", count, "so nguyen to")

result = NhapVaDem()
InKQ(result)
