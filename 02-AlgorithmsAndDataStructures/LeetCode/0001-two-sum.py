"""
LeetCode 1 - Two Sum
https://leetcode.com/problems/two-sum/

Problem: “nums” adlı bir tamsayı dizisi ve ‘target’ adlı bir tamsayı verildiğinde, toplamı “target” olan iki sayının indekslerini döndürün.
Her girdi için tam olarak tek bir çözüm olduğunu varsayabilirsiniz ve aynı elemanı iki kez kullanamazsınız.
Cevabı herhangi bir sırayla döndürebilirsiniz.
"""

#================
# BENİM ÇÖZÜMÜM
#================

def twoSum1(nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]

nums = [2,7,11,15]
target = 9

inds = twoSum1(nums, target)
print(inds)

# Zaman Karmaşıklığı: O(n²) - iç içe döngü
# Yer Karmaşıklığı: O(1)

#===================
# HASH MAP ÇÖZÜMÜ
#===================

def twoSum2(nums, target):
        seen = {}  # değer -> index
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i


nums = [2, 7, 11, 15]
target = 9

a = twoSum2(nums, target)
print(a)

# Zaman Karmaşıklığı: O(n) - tek geçiş
# Yer Karmaşıklığı: O(n) - hash map için ekstra alan

# ============================================
# NOTLAR
# ============================================
# İlk çözümümde her eleman için tüm diziyi tekrar tarıyordum, bu yüzden karmaşıklık O(n²) oluyordu.
# Hash map kullanarak "daha önce gördüğüm sayıları" saklayıp, karşılığını (complement) anlık kontrol edince O(n)'e düştü. 
# Zaman kazanmak için O(n) ekstra yer kullanmayı kabul ediyoruz - bu klasik bir "time-space tradeoff".