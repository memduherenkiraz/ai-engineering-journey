
#----------------------------------------------------------------------------------------------------------------------------------------------

#region BUBBLE SORT

# BUBBLE SORT (BALONCUK SIRALAMASI)
# Komşu elemanları sürekli karşılaştırıp sırası yanlış olanları takas (swap)
# ederek en büyük elemanı her adımda dizinin sonına taşır.
# -----------------------------------------------------------------------------

def bubble_sort(arr):
    # Dizinin eleman sayısı kadar dönecek olan dış döngü.
    # Her bir turda en az bir eleman (en büyük olan) doğru yerine yerleşir.
    for i in range(len(arr)):
        # Bu turda hiç eleman değişikliği (takas) yapıldı mı kontrol eden bayrak (flag).
        # Eğer bir turda hiç takas olmazsa dizi sıralanmış demektir.
        swapped = False

        # Yan yana olan (ardışık) elemanları karşılaştırmak için iç döngü.
        # len(arr) - i - 1 yapılmasının nedeni: Her dış döngü sonunda en büyük eleman
        # zaten en sona yerleştiği için son i adete tekrar bakmaya gerek kalmaz.
        for j in range(0, len(arr) - i - 1):
            # Sol taraftaki eleman, sağ taraftaki elemandan büyükse (sıralama yanlışsa):
            if arr[j] > arr[j + 1]:
                # İki elemanın yerini birbiriyle değiştir (Takas / Swapping).
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                # Değişiklik yapıldığını belirtmek için bayrağı True yapıyoruz.
                swapped = True

        # İç döngü bittiğinde hiç takas yapılmadıysa (swapped hâlâ False ise):
        if not swapped:
            # Dizi halihazırda tamamen sıralıdır, erken çıkış yaparak algoritmayı bitir.
            break

# TEST KODU
array = [10, 9, 8, 7, 6, 5]
bubble_sort(array)
print("Sorted List:", array)

#endregion

#----------------------------------------------------------------------------------------------------------------------------------------------

#region SELECTION SORT

# SELECTION SORT (SEÇMELİ SIRALAMA)
# Dizinin sıralanmamış kısmındaki en küçük elemanı bulur ve o kısmın
# başındaki eleman ile yer değiştirerek sıralı kısmı adım adım genişletir.
# -----------------------------------------------------------------------------

def selection_sort(arr):
    # Sıralanacak doğru konumu (indeksi) baştan sona doğru ilerleten dış döngü.
    # len(arr) - 1 olmasının sebebi: Son eleman kaldığında zaten en büyük o olacağı için tek kalır.
    for i in range(len(arr) - 1):
        # Şimdilik en küçük elemanın 'i' indeksinde olduğunu varsayıyoruz.
        min_ind = i

        # 'i' indeksinden sonra gelen tüm sıralanmamış elemanları tarayan iç döngü.
        for j in range(i + 1, len(arr)):
            # Eğer taradığımız yerde, varsaydığımız min_ind'deki elemandan daha küçük bir eleman bulursak:
            if arr[j] < arr[min_ind]:
                # Yeni en küçük elemanın indeksini 'min_ind' olarak güncelle.
                min_ind = j

        # Eğer bulunan en küçük eleman zaten koymak istediğimiz pozisyonda ('i') değilse:
        if min_ind != i:
            # Bulunan en küçük eleman ile 'i' indeksindeki elemanı yer değiştir (takas yap).
            arr[i], arr[min_ind] = arr[min_ind], arr[i]

# TEST KODU
arr = [14, 12, 10, 15, 11]
selection_sort(arr)
print("Sorted Dizi:", arr)

#endregion

#----------------------------------------------------------------------------------------------------------------------------------------------

#region INSERTION SORT

# INSERTION SORT (EKLEMELİ SIRALAMA)
# İskambil kâğıtlarını elde sıralamaya benzer. Her adımda diziden bir eleman
# alınır (key) ve sol taraftaki zaten sıralı olan kısmın doğru yerine yerleştirilir.
# -----------------------------------------------------------------------------

def insertion_sort(arr):
    # 1. indeksten başlayarak dizinin sonuna kadar giden dış döngü.
    # 0. indeksteki ilk eleman tek başına zaten sıralı kabul edildiği için 1'den başlar.
    for i in range(1, len(arr)):
        # Sıralı kısma doğru yerine yerleştirilecek olan mevcut elemanı 'key' olarak saklıyoruz.
        key = arr[i]
        
        # 'key' elemanının solundaki (yani sıralı kısımdaki) son elemanın indeksini tutuyoruz.
        j = i - 1

        # Sıralı kısımdaki elemanlar 'key' değerinden büyük olduğu sürece sağa kaydırma döngüsü.
        # j >= 0: Dizinin sol sınırına ulaşana kadar devam eder.
        # key < arr[j]: 'key' değerinden büyük elemanları buldukça çalışır.
        while j >= 0 and key < arr[j]:
            # 'key'den büyük olan elemanı bir sağ pozisyona kopyalayarak yer açıyoruz.
            arr[j + 1] = arr[j]
            # Sıralı kısımda bir sola doğru ilerlemek için indeksi azaltıyoruz.
            j -= 1

        # Sağa kaydırma işlemleri bittikten sonra, açılan boşluğa (j + 1 indeksine) 'key' elemanını yerleştiriyoruz.
        arr[j + 1] = key

# TEST KODU
arr = [14, 12, 10, 15, 11]
insertion_sort(arr)
print("Sorted Dizi: ", arr)

#endregion

#----------------------------------------------------------------------------------------------------------------------------------------------

#region MERGE SORT

# MERGE SORT
# -----------------------------------------------------------------------------
# MERGE (BİRLEŞTİRME) FONKSİYONU
# Sıralanmış iki alt diziyi (first ve last) alır, elemanları tek tek 
# karşılaştırarak yeni ve tek bir sıralı liste (sorted_list) halinde birleştirir.
# -----------------------------------------------------------------------------
def merge(first, last):
    sorted_list = []  # Sıralanmış elemanları toplayacağımız boş ana liste
    i = j = 0         # i: 'first' dizisinin indeksi, j: 'last' dizisinin indeksi

    # Her iki dizide de hâlâ bakılacak eleman varken döngü devam eder
    while i < len(first) and j < len(last):
        # 'first' dizisindeki eleman 'last' dizisindekinden küçükse:
        if first[i] < last[j]:
            sorted_list.append(first[i])  # Küçük olan elemanı yeni listeye ekle
            i += 1                        # 'first' dizisindeki ibreyi bir sağa kaydır
        # 'last' dizisindeki eleman küçük veya eşitse:
        else:
            sorted_list.append(last[j])  # Küçük olan elemanı yeni listeye ekle
            j += 1                        # 'last' dizisindeki ibreyi bir sağa kaydır

    # Eğer 'first' dizisinde karşılaştırılmamış eleman kaldıysa:
    # (Diğer dizi erken bittiği için kalan bu elemanlar zaten sıralıdır)
    while i < len(first):
        sorted_list.append(first[i])  # Kalan elemanları sırayla listenin sonuna ekle
        i += 1                        # İbreyi ilerlet

    # Eğer 'last' dizisinde karşılaştırılmamış eleman kaldıysa:
    while j < len(last):
        sorted_list.append(last[j])  # Kalan elemanları sırayla listenin sonuna ekle
        j += 1                        # İbreyi ilerlet

    # İki parçanın birleşimiyle oluşan tam sıralı listeyi geri döndür
    return sorted_list

# -----------------------------------------------------------------------------
# MERGE SORT (BİRLEŞTİRMELİ SIRALAMA) FONKSİYONU
# Diziyi özyinelemeli (recursive) olarak tek eleman kalana kadar ortadan ikiye böler,
# ardından 'merge' fonksiyonunu çağırarak sıralı şekilde yukarı doğru birleştirir.
# -----------------------------------------------------------------------------
def merge_sort(arr):
    # TABAN DURUMU (BASE CASE - DURMA KOŞULU):
    # Eğer dizide 0 veya 1 eleman varsa, dizi zaten sıralıdır.
    # Özyinelemeyi burada durdururuz ve eldeki bu sıralı parçayı geri döndürürüz.
    if len(arr) <= 1:
        return arr
    
    # Dizinin tam orta noktasının indeksini hesaplar (Tam sayı bölmesi // kullanılır)
    mid = len(arr) // 2

    # Dizinin sol yarısını (0'dan mid'e kadar) özyinelemeli olarak parçalamaya gönderir.
    # Tek elemana düşene kadar bölünür ve sıralanmış sol yarı 'fh' içine döner.
    fh = merge_sort(arr[:mid])

    # Dizinin sağ yarısını (mid'den sona kadar) özyinelemeli olarak parçalamaya gönderir.
    # Tek elemana düşene kadar bölünür ve sıralanmış sağ yarı 'lh' içine döner.
    lh = merge_sort(arr[mid:])

    # Eldeki sıralanmış sol yarıyı (fh) ve sağ yarıyı (lh) birleştirip üst fonksiyona döndürür.
    return merge(fh, lh)

# TEST KODU
arr = [70, 50, 30, 10, 20, 40, 60, 80]
merged = merge_sort(arr)
print("Sorted Dizi: ", merged)

#endregion

#----------------------------------------------------------------------------------------------------------------------------------------------

