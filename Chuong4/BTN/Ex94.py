import random
def matkhau():
    mk = []
    max_len = random.randint(7, 10)
    for i in range(max_len):
        a = chr(random.randint(33,126))
        mk = mk + [a]
    matkhau = ''.join(mk)
    return matkhau
print(matkhau())