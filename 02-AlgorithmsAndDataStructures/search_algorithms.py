
#----------------------------------------------------------------------------------------------------------------------------------------------

# Linear Search

# def linear_search(array, char):
#     for i in range(len(arr)):
#         if arr[i] == char:
#             return i
#     return -1

# arr = [2 ,13, 6, 33, 11, 1, 5]
# ch = int(input("Aranacak Değer:"))

# print("Aranan Değerin Indeksi:", linear_search(arr, ch))

#----------------------------------------------------------------------------------------------------------------------------------------------

# Binary Search

# def binary_search(arr, char):
#     low = 0   # Dizinin ilk indeksini tutar. 
#     high = len(arr) - 1   # Dizinin son indeksini tutar. 
   
#     while low <= high:   # Dizinin ilk ve son indeksi eşitlenene kadar bir döngü oluşturduk. Bunun nedeni low = high olunca dizi tek eleman düşer.

#         mid = (low + high) // 2   # Her karşılaştırmada aranan elemanın olduğu tarafla aramaya devam edilir.
#         # Bu yüzden dizinin başlangıç ve bitiş indeksleri değişir. Ortance elemanıda sürekli yeniden hesaplamak gerekir.

#         if char > arr[mid]:   # Eğer aranan eleman, ortanca elemandan büyükse; demekki aranan eleman sağ tarafta kalıyor demektir.
#             low = mid + 1   # Ortanca elemanın solundaki elemanlara gerek yok demektir. Dizinin ilk indeksi mid +1 olur, high aynı kalır.
#         elif char < arr[mid]:   # Eğer aranan eleman, ortanca elemandan küçükse; demekki aranan eleman sol tarafta kalıyor demektir.
#             high = mid - 1   # Ortanca elemanın sağındaki elemanlara gerek yok demektir. Dizinin ilk indeksi low aynı kalır, son indeksi mid-1 olur.
#         else:   # Eğer eşitse direkt olarak bulunmuş olur. mid, elemanın indeksini tuttuğundan direkt döndürülür.
#             return mid
#     return -1   

# array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# char = 3

# print("Aranan Elemanın Indeksi:", binary_search(array, char))

#----------------------------------------------------------------------------------------------------------------------------------------------