import math

# Öklid mesafesi hesaplayan fonksiyon
def euclideanDistance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

# 2D uzayda iki nokta
a = (1, 2)
b = (4, 6)

# İki nokta arasındaki mesafeyi hesapla ve yazdır
distance = euclideanDistance(a, b)
print(f"İki nokta arasındaki Öklid mesafesi: {distance}")
