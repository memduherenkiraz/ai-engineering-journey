# Print Fonksiyonu
name = "Eren"
age = 25

print(name)

# Birden fazla değişkeni ekrana yazdırmak için "," kullanabiliriz.
print(name, age)

# String değişkenleri birleştirmek için "+" kullanabiliriz.
# Ancak "+" operatörü stringleri birleştirirken boşluk koymaz.
surname = "Kiraz"

print(name + surname)  # Çıktı: ErenKiraz

# Veri Tipleri
# String
language = "Python"
print(type(language))
# Integer
year = 2026
print(type(year))
# Float
weight = 80.25
print(type(weight))
# Boolean
isTrue = True
print(type(isTrue))
# NoneType 
deg = None
print(type(deg))

# Swapping
number1 = 15
number2 = 20

# Değişkenlerin değerlerini yer değiştirdik.
number1, number2 = number2, number1

print(number1)
print(number2)
