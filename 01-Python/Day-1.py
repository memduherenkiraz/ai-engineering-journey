
#----------------------------------------------------------------------------------------------------------------

# Print Fonksiyonu
# name = "Eren"
# age = 25

# print(name)

# Birden fazla değişkeni ekrana yazdırmak için "," kullanabiliriz.
# print(name, age)

# String değişkenleri birleştirmek için "+" kullanabiliriz.
# Ancak "+" operatörü stringleri birleştirirken boşluk koymaz.
# surname = "Kiraz"

# print(name + surname)  # Çıktı: ErenKiraz

#----------------------------------------------------------------------------------------------------------------

# Veri Tipleri
# String
# language = "Python"
# print(type(language))

# Integer
# year = 2026
# print(type(year))

# Float
# weight = 80.25
# print(type(weight))

# v = 12e3
# print(v)
# print(type(v))

# Complex
# num = complex(2, 5)
# print(num)
# print(type(num))

# Boolean
# isTrue = True
# print(type(isTrue))

# NoneType 
# deg = None
# print(type(deg))

#----------------------------------------------------------------------------------------------------------------

# Swapping
# number1 = 15
# number2 = 20

# Değişkenlerin değerlerini yer değiştirdik.
# number1, number2 = number2, number1

# print(number1)
# print(number2)

#----------------------------------------------------------------------------------------------------------------

# Tür Dönüşümleri

# x = str(True) # Boolen to String
# print(x)
# print(type(x))

# y = int(False)  # Boolean to Integer
# print(y)  # False=0 olduğu için 0 değeri alınır.
# print(type(y))

# z = bool(1)   # Integer to Boolean
# print(z)   # True=1 olduğu için True değerini aldı.
# print(type(z))

# num1 = 12
# num2 = "25"
# print("Sum:", num1 + int(num2))  # String to Integer

# info = dict(name = "Eren", age = 25)
# print(info)
# print(type(info))

#----------------------------------------------------------------------------------------------------------------

# Input Fonksiyonu
# ad = input("adınızı giriniz: ")
# print(ad)

# ÖRNEK: Girilen iki sayının toplamını gösteren kod bloğunu yazınız.
# num1 = int(input("1. Sayıyı Giriniz:"))
# num2 = int(input("2. Sayıyı Giriniz:"))
# print(f"{num1} + {num2} = {num1+num2}")

# ÖRNEK: Yarı çapı verilen bir dairenin çevresini ve alanını hesaplayan kod bloğunu yazınız.
# Daire Çevre: 2*pi*r 
# Daire Alan: pi*r^2

# import math

# r = float(input("Daire Yarı Çapı: "))

# def daire_cevre(yaricap):
#     return 2 * math.pi * yaricap

# def daire_alan(yaricap):
#     return math.pi * (yaricap**2)

# print("Daire Cevre: ", daire_cevre(r), "\nDaire Alan:", daire_alan(r))

#----------------------------------------------------------------------------------------------------------------
