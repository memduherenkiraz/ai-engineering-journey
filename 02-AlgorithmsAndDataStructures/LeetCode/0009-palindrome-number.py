"""
LeetCode 9 - Palindrome Number
https://leetcode.com/problems/palindrome-number/

Problem: Verilen bir tam sayının palindrom olup olmadığını bul 
(baştan okunuşu ile sondan okunuşu aynı mı).
"""

# ============================================
# BENİM ÇÖZÜMÜM (Basamak ile)
# ============================================

def isPalindrome(number):
    bas = []

    if number < 0:
        return False
    
    while number != 0:
        tmp = number
        number = number // 10
        bas.append(tmp - number * 10)
    
    if len(bas) >= 2:
        for i in range(0, len(bas) // 2):
            if bas[i] != bas[len(bas) - i - 1]:
                return False
    return True

number = 112

if isPalindrome(number):
    print("Sayi Polindrome")
else:
    print("Sayi Polindrome Değil")

# Zaman Karmaşıklığı: O(n) - n, sayının basamak sayısı; while döngüsü basamak
#                      sayısı kadar dönüyor, for döngüsü de en fazla n/2 kere çalışıyor.
# Yer Karmaşıklığı: O(n) - basamaklar "bas" listesinde saklanıyor.
# Not: Negatif sayılar palindrom kabul edilmez (- işareti tersten okunca
#      anlamsızlaşır), bu yüzden en başta erken çıkış (early return) yapıldı.