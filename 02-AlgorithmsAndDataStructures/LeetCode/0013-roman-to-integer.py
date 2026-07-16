"""
Leet Code 13 - Roman to Integer
https://leetcode.com/problems/roman-to-integer/

Problem: İçinde roma rakamlarıyla oluşturulan sayı bulunan string değişkenini,
integer sayıya dönüştür.
"""

def romanToInteger(s):
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
print(f"{roman}: {romanToInteger(roman)}")
