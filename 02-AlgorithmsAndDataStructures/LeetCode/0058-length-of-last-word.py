"""
Leet Code 58 - Length of Last Word
https://leetcode.com/problems/length-of-last-word/

Problem: Verilen stringdeki son kelimenin uzunluğunu döndür.
Kısıt: String en az bir harf içerir.
"""

# ================================
# BENİM ÇÖZÜMÜM (metotlar ile)
# ================================

def lengthOfLastWord1(s: str):
    #if s.isspace(): return 0  # Eğer kısıt olmasaydı, bu satırı ekleyerek boş stringlerde hata almazdık.
    return len(s.split()[-1])

s = "Hello World"
print(f"'{s}' Stringinin Son Kelimesinin Uzunlugu: {lengthOfLastWord1(s)}")

# Fonksiyon, stringin sadece boşluk içerdiği durumda ("   " gibi) IndexError verir.
# Bunun nedeni split metodunun bölecek değer bulamamasıdır.
# Ancak problem kısıtında stringin en az bir harf içerir demesinden dolayı
# string asla boş olamaz veya boşluklardan oluşamaz.

# Zaman Karmaşılığı: O(n) - split ile stringin tamamı taranır. 
# Alan Karmaşıklığı: O(n) - split ile ekstra liste oluşturduğundan ekstra bellek harcar.

# ================================
# ALTERNATİF ÇÖZÜM (metotsuz)
# ================================

def lengthOfLastWord2(s: str):
    end = len(s) - 1

    while s[end] == " ":
        end -= 1
    
    length = 0

    while end >= 0 and s[end] != " ":
        length += 1
        end -= 1
    
    return length

s = "Python is cool"
print(f"'{s}' Stringinin Son Kelimesinin Uzunlugu: {lengthOfLastWord2(s)}")

# Zaman Karmaşıklığı: O(n)
# Alan Karmaşıklığı: O(1) - ekstra bellek kullanmaz.(ekstra veri yapısı yok)

