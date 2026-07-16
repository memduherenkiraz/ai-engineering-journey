"""
Leet Code 58 - Length of Last Word
https://leetcode.com/problems/length-of-last-word/

Problem: Verilen stringdeki son kelimenin uzunluğunu döndür.
Kısıt: String en az bir harf içerir.
"""

def lengthOfLastWord(s: str):
    #if s.isspace(): return 0  # Eğer kısıt olmasaydı, bu satırı ekleyerek boş stringlerde hata almazdık.
    return len(s.split()[-1])

str = "Hello World"
print(f"{str} Stringinin Son Kelimesinin Uzunlugu: {lengthOfLastWord(str)}")

# Fonksiyon, stringin sadece boşluk içerdiği durumda ("   " gibi) IndexError verir.
# Bunun nedeni split metodunun bölecek değer bulamamasıdır.
# Ancak problem kısıtında stringin en az bir harf içerir demesinden dolayı
# string asla boş olamaz veya boşluklardan oluşamaz.