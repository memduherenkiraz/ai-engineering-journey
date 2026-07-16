"""
Leet Code 13 - Roman to Integer
https://leetcode.com/problems/roman-to-integer/

Problem: İçinde roma rakamlarıyla oluşturulan sayı bulunan string değişkenini integer sayıya dönüştür.
"""

# ============================================
# BENİM ÇÖZÜMÜM (Metot ile)
# ============================================

def romanToInteger1(s):
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    total = 0
    prev_value = 0

    for i in reversed(s):
        if roman[i] < prev_value:
            total -= roman[i]
        else:
            total += roman[i]
        
        prev_value = roman[i]
    
    return total

roman = "MCMXCIV"
print(f"{roman}: {romanToInteger1(roman)}")

# Zaman Karmaşıklığı: O(n) - Döngü var.
# Alan Karmaşıklığı: O(1)

# ============================================
# ALTERNATİF ÇÖZÜM (Metotsuz))
# ============================================

def romanToInteger2(s):
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    total = 0
    n = len(s)

    for i in range(n):
        prev_value = roman[s[i]]

        if i + 1 < n and prev_value < roman[s[i + 1]]:
            total -= prev_value
        else:
            total += prev_value
    
    return total

roman = "MCMXCIV"
print(f"{roman}: {romanToInteger2(roman)}")

# Zaman Karmaşıklığı: O(n)
# Alan Karmaşıklığı: O(1)