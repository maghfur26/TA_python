import math

def lingkaran():
    r = int(input("masukan nilai r: "))
    luas = math.pi*r**2
    keliling = 2*math.pi*r
    print("Luas: ", luas)
    print("Keliling: ", keliling)
    return luas, keliling

def segitiga(a,t,sisi):
    luas = 0.5*a*t
    keliling = sisi*3
    print("Luas: ", luas)
    print("Keliling: ", keliling)
    return luas,keliling