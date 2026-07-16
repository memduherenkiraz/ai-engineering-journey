"""
LeetCode 136 - Single Number
https://leetcode.com/problems/single-number/

Problem: Verilen bir dizide her eleman iki kez geçiyor, sadece bir eleman tek kez geçiyor. O elemanı bul.
Kısıt: O(n) zaman karmaşıklığı ve O(1) ekstra yer kullanmalısın.
"""

# ============================================
# BENİM ÇÖZÜMÜM (Liste ile)
# ============================================

def singleNumber1(nums):
    single = []
    
    for i in range(len(nums)):
        if nums[i] not in single:
            single.append(nums[i])
        else:
            single.remove(nums[i])
    return single[0]

nums = [3,4,5,8,5,4,3]

print(singleNumber1(nums))

# Zaman Karmaşıklığı: O(n²) - "in" ve "remove" liste üzerinde O(n) sürüyor, bunu n eleman için tekrarlıyoruz.
# Yer Karmaşıklığı: O(n) - single listesi en kötü durumda büyüyor.
# Sorun: O(n) zaman ve O(1) yer şartını karşılamıyor

# ============================================
# OPTİMİZE EDİLMİŞ ÇÖZÜM (XOR ile)
# ============================================
def singleNumber2(nums):
    result = 0
    for num in nums:
        result ^= num
    return result

nums = [3,4,5,8,5,4,3]

print(singleNumber2(nums))

# Zaman Karmaşıklığı: O(n) - tek geçiş
# Yer Karmaşıklığı: O(1) - sadece tek bir değişken (result) kullanıyoruz

# ============================================
# NOTLAR
# ============================================
# İlk çözümümde bir listeyi "gördüğüm sayılar" gibi kullanıyordum:
# sayı yoksa ekle, varsa çıkar. Sonunda listede tek eleman kalıyordu.
# Bu doğru sonucu veriyordu ama liste üzerindeki "in" ve "remove"
# işlemleri O(n) sürdüğü için toplamda O(n²) oluyordu, ayrıca liste
# ekstra yer kapladığı için O(1) yer şartını da karşılamıyordu.
#
# XOR (^) operatörünün üç özelliği bu problemi O(n) zaman karmaşıklığı ve O(1) yer karmaşıklığıyla çözmeyi mümkün kılıyor:
#   a ^ a = 0   (bir sayı kendisiyle XOR'lanınca sıfırlanır)
#   a ^ 0 = a   (bir sayı sıfırla XOR'lanınca değişmez)
#   XOR sırayı ve gruplamayı önemsemez (commutative + associative)
# Diziyi tek tek XOR'layınca çiftler birbirini götürüyor, geriye sadece tek kalan sayı kalıyor. Ekstra veri yapısına hiç gerek yok.

