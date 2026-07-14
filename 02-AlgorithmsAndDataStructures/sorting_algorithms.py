
#----------------------------------------------------------------------------------------------------------------------------------------------

# Bubble Sort

# def bubble_sort(arr):
   
#     for i in range(len(arr)):   # Dizinin sonuna kadar giden dış döngü.
#         swapped = False   # Eleman değişme olup olmadığını kontrol eden bayrak.
#         for j in range(0, len(arr) - i - 1):   # Her defasında ardışık elemanları karşılaştırmak için iç döngü.
#         # range'in len(arr) - i - 1 olmasının sebebi, her dış döngüde en büyük eleman en sona gelecek. Oyüzden tekrar bakmamıza gerek yok.
#             if arr[j] > arr[j + 1]:
#                 # Swapping
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#                 swapped = True
#         if not swapped:   # Eğer Dış döngünün birinde hiç swap işlemi olmadıysa bu tüm dizinin sıralandığı anlamına gelir.
#             break

# array = [10, 9, 8, 7, 6, 5]
# bubble_sort(array)

# print("Sorted List:", array)

#----------------------------------------------------------------------------------------------------------------------------------------------