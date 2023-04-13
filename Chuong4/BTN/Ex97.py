from random import randint
import random
def randomPassword(): 
    I = random.randint(7, 10)
    matkhau = ""
    for i in range(I):
        matkhau=matkhau+chr(randint(33,126))
    return matkhau
import re
def matkhautot(matkhau): 
    if len(matkhau) < 8:
        return False
    if not re.search("[a-z]", matkhau):
        return False
    if not re.search("[A-Z]", matkhau):
        return False
    if not re.search("[0-9]", matkhau):
        return False
    return True
def main(): 
    solanthu = 0
    matkhau = input()
    while not matkhautot(matkhau):
        solanthu += 1
    matkhau = randomPassword()
    print("Mat khau tot ngau nhien sau {} lan thu: {}".format(solanthu, matkhau))
main()
