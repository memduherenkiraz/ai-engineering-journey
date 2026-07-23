
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

# Random Modülü
# import random

# num1 = random.random()  # 0.0 - 1.0 aralığı: float
# print(num1)

# num2 = random.uniform(4,10)   # 4 - 10 aralığı: float
# print(num2)

# num3 = random.randint(4, 10)   # 4 - 10 aralığı: int
# print(num3)

# num4 = random.randrange(0, 10, 2) # (0, 2, 4, 6, 8) arasından rastgele seçer.
# print(num4)

# colors = ["red", "orange", "yellow", "green", "blue", "pink", "purple"]

# print("Choice:", random.choice(colors))
# print("Choices:", random.choices(colors, k=2))
# print("Sample:", random.sample(colors, k=2))

# print(colors)
# random.shuffle(colors)
# print(colors)

# Seed Fonksiyonu
# import random

# random.seed(42)
# Her zmaan 82 üretir. Çünkü Seed=42 ve Randint(1,100). İlk eleman 82
# print("Seed 42 - Number1:", random.randint(1, 100))

# Her zaman 15 üretir. Çünkü Seed=42 ve Randint(1,100). İkinci eleman 15
# print("Seed 42 - Number2:", random.randint(1, 100))

#----------------------------------------------------------------------------------------------------------------

# String İşlemleri

# String Slicing
# Upper Lower
# strip ,replace, split
# format ,f-string

#----------------------------------------------------------------------------------------------------------------

# Virgülden Sonra Basamak Sayısı

# f-stringle kullanılır.
# değişken:.xf olarak kullanılır. "x" basamak sayısını ifade eder.

# price = 20.68475
# print(f"{price:.1f}") # Virgülden sonra 1 basamak
# print(f"{price:.2f}") # Virgülden sonra 2 basamak
# print(f"{price:.3f}") # Virgülden sonra 3 basamak

# pi = 3.14159
# # %.2f ifadesi virgülden sonra 2 basamak float demektir.
# print("Pi değeri: %.2f" % pi)

#----------------------------------------------------------------------------------------------------------------

# Örnek: Öğrencinin vize ve final puanlarının ortalamasını gösteren kod bloğu.

# midterm = int(input("Enter Your Midterm Score:"))
# final = int(input("Enter Your Final Score:"))

# average = (midterm + final) / 2
# print(f"Average Score: {average:.3f}")

#----------------------------------------------------------------------------------------------------------------

# text = "I need to learn Python. Python is a cool language. python is good."
# print(text.count("Python"))

#----------------------------------------------------------------------------------------------------------------

# Bir dizideki puanlar arasından en yüksek puandan FARKLI olan ikinci en yüksek puanı (runner-up) bulup yazdırmak.

# Tuzak: En yüksek puanı birden fazla katılımcı almış olabilir. Bu durumda dizi sadece sıralanıp sondan ikinci eleman alınırsa yanlış sonuç
# çıkar (en yüksek puanın kendi kopyası runner-up sanılır). "Runner-up" demek, en yüksekten FARKLI olan bir sonraki en yüksek puan demektir.


# n = int(input("Sayiyi Giriniz:"))
# arr = map(int, input("Liste Elemanlarını Giriniz:").split())

# arr = list(arr)
# biggest = float('-inf')
# bigger = float('-inf')

# for i in range(n):
#     if arr[i] > biggest:
#         bigger = biggest
#         biggest = arr[i]
#     elif arr[i] < biggest and arr[i] > bigger:
#         bigger = arr[i]

# print(bigger)

#----------------------------------------------------------------------------------------------------------------

# Bir sınıftaki öğrencilerin isim ve notlarını nested list olarak saklayıp,
# ikinci en düşük nota sahip öğrenci(ler)in isimlerini alfabetik sırayla,
# her biri ayrı satırda yazdırmak.

# listem = []
# for i in range(int(input("Kaç Kişi:"))):
#     name = input("İsim Giriniz:")
#     score = float(input("Score Giriniz:"))
#     listem.append([name, score])


# lowest = float('inf')
# lower = float('inf')

# names = []

# for i in range(len(listem)):
#     if listem[i][1] < lowest:
#         lower = lowest
#         lowest = listem[i][1]
#     elif listem[i][1] < lower and listem[i][1] > lowest:
#         lower = listem[i][1]

# for i in range(len(listem)):
#     if listem[i][1] == lower:
#         names.append(listem[i][0])

# names.sort()
# for i in names:
#     print(i)

# ALTERNATİF (Tek for döngüsü)

# listem = []
# lowest = second = float('inf')
# names_lowest = []
# names_second = []

# for _ in range(int(input("Kişi Sayısı: "))):
#     name = input("Name: ")
#     score = float(input("Score: "))
#     listem.append([name, score])

#     if score < lowest:
#         second = lowest
#         names_second = names_lowest
#         lowest = score
#         names_lowest = [name]
#     elif score == lowest:
#         names_lowest.append(name)
#     elif score < second:
#         second = score
#         names_second = [name]
#     elif score == second:
#         names_second.append(name)

# print("================================================")
# for isim in sorted(names_second):
#     print(isim)

#=====================================================================================================

# Bir tam sayı dizisindeki pozitif, negatif ve sıfır elemanların oranını
# (toplam eleman sayısına bölünmüş hallerini), 6 ondalık basamak hassasiyetle, her biri ayrı satırda yazdırmak.

# def plusMinus(arr):
#     n = len(arr)
#     pos = 0
#     neg = 0
#     zero = 0
    
#     for i in arr:
#         if i > 0:
#             pos += 1
#         elif i < 0: 
#             neg += 1
#         else:
#             zero += 1
    
#     ratio = [pos/n, neg/n, zero/n]
    
#     for i in ratio:
#         print(f"{i:.6f}")


# n = int(input("Eleman Sayisi: ").strip())
# arr = list(map(int, input("Elemanlar: ").rstrip().split()))

# plusMinus(arr)

#=====================================================================================================

# Bir string içinde verilen sub-string'ten kaç adet olduğunu bulan kod bloğunu yazınız.
"""
String: ABCDCDC
Sub-String: CDC
Count: 2
"""

# Kendi Çözümüm

# def count_substring(string, sub_string):
#     count = 0
#     for i in range(len(string) - len(sub_string) + 1):
#         state = 0
#         for j in range(len(sub_string)):
#             if string[j + i] == sub_string[j]:
#                 state += 1
#         if state == len(sub_string):
#             count += 1
#     return count

# string = input().strip()
# sub_string = input().strip()
    
# count = count_substring(string, sub_string)
# print(count)


# Kısa Çözüm

# def count_substring(string, sub_string):
#     n = len(sub_string)
#     return sum(
#         1 for i in range(len(string) - n + 1)
#         if string[i:i+n] == sub_string
#     )

# string = input().strip()
# sub_string = input().strip()
    
# count = count_substring(string, sub_string)
# print(count)


# def solve(s: str):
#     return " ".join(i.capitalize() for i in s.split())

# string = "1 w 2 r 3g"

# print(solve(string))



# def print_formatted(number):
#     for i in range(1, number):
#         print(f"{i}   {(oct(i)[2:])}   {hex(i)[2:].upper()}   {bin(i)[2:]}")

# number = int(input("Sayiyi Giriniz:"))
# print_formatted(number)

