import random
def loaibienso():
    type=random.choice(['cũ','mới'])
    if type=='cũ':
        random_chu = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=3))
        random_so  = ''.join(random.choices('0123456789',k=3))
        bienso= f"{random_chu}{random_so}"
    else:
        random_chu = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=4))
        random_so  = ''.join(random.choices('0123456789',k=3))
        bienso= f"{random_chu}{random_so}"
    return bienso
print(loaibienso())