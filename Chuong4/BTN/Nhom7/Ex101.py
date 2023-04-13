def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
def reduce_fraction(a,b):
    div = gcd(a,b)
    return a // div, b // div
a=int(input('a='))
b=int(input('b='))
reduced_a, reduced_b = reduce_fraction(a,b)
print(f"phan so sau khi rut gon la: {reduced_a}/{reduced_b}")