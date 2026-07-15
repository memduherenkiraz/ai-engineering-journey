# 🐍 Python Notları
 
Python dilinin temellerinden ileri seviye konularına (OOP, decorators, generators) kadar tuttuğum kişisel çalışma notlarım. Her başlık kısa bir açıklama ve örnek kod içerir.
 
## 📑 İçindekiler
 
- [Print() Fonksiyonu](#print-fonksiyonu)
- [Veri Tipleri](#veri-tipleri)
- [Değişken Tanımlama ve Type](#değişken-tanımlama-ve-type)
- [String](#string)
- [Değişken Değiş Tokuşu (Swapping)](#değişken-değiş-tokuşu-swapping)
- [Format](#format)
- [Aritmetik Operatörler](#aritmetik-operatörler)
- [Tür Dönüşümleri](#tür-dönüşümleri)
- [İndexleme](#i̇ndexleme)
- [String Metotları](#string-metotları)
- [Input](#input)
- [Liste (List)](#liste-list)
- [Sözlük (Dictionary)](#sözlük-dictionary)
- [Setler (Kümeler)](#setler-kümeler)
- [Tuple (Demet)](#tuple-demet)
- [Karar Yapıları](#karar-yapıları)
- [Döngüler](#döngüler)
- [Fonksiyonlar](#fonksiyonlar)
- [Kaçış Dizileri](#kaçış-dizileri)
- [Hata Yönetimi](#hata-yönetimi)
- [Dosya İşlemleri](#dosya-i̇şlemleri)
- [İleri Seviye Yapılar](#i̇leri-seviye-yapılar)
- [Modüller](#modüller)
- [Class'lar (OOP)](#classlar-oop)
- [Alıştırma: Employee / ProductionWorker](#alıştırma-employee--productionworker)
---
 
## Print() Fonksiyonu
 
Python'da ekrana yazdırmak için `print()` kullanılır.
 
Yazı uzunsa `\` kaçış karakteri ile satırı bölerek ekrana sığdırabiliriz:
 
```python
print("Bu mesajı alan Python karakter dizisini soldan sağa doğru okumaya devam ediyor \
ve sonunda karakter dizisini bitiren çift tırnak işaretini bularak \
bize hatasız bir çıktı veriyor.")
```
 
`print()` fonksiyonunun içinde geliştiriciler tarafından konulmuş iki önemli parametre vardır: **sep** ve **end**.
 
### sep parametresi
 
Verdiğimiz argümanlardan sonra hangi karakterin geleceğini kontrol eder. Varsayılan değeri **boşluktur**.
 
```python
print("Merhaba", "Ben", "Eren", sep='+')
# sep parametresini '+' yaptık, artık değerler arasına + gelecek.
```
 
### end parametresi
 
Fonksiyon sonlandığında bir sonraki `print`'in nereden başlayacağını belirtir. Varsayılan değeri `\n`'dir.
 
```python
print("Merhaba", "Python", end='\t')  # \t bir TAB boşluk bırakır
print("Hello", "Python")
```
 
### Yıldızlı Parametre (`*`)
 
String içindeki her karakteri ayrı ayrı, `sep` değerine göre ayırarak yazdırmak için kullanılır:
 
```python
print(*"Hello my name is Eren. I am 20 years old.", sep='_')
```
 
---
 
## Veri Tipleri
 
- **Integer** — Tam sayı
- **Float** — Kayar noktalı sayı
- **String** — Karakter dizisi
- **Boolean** — Mantıksal ifadeler
- **Complex** — Karmaşık sayılar
- **List** — Liste
- **Dictionary** — Sözlük
- **Tuple** — Demet
- **Set** — Küme
---
 
## Değişken Tanımlama ve Type
 
Değişkenler `değişken_adı = değer` şeklinde tanımlanır:
 
```python
ad = "eren"
```
 
`type()` fonksiyonu ile bir değişkenin veri tipini görebiliriz:
 
```python
print(type(ad))
```
 
### String
 
Çift tırnak ile tanımlanır. Bir kelimeyi vurgulamak için çift tırnak kullanmak istersek `\` kaçış karakteri gerekir:
 
```python
ad = "eren"
print(ad)
print(type(ad))
 
print("Merhaba \"Python\"")  # Çıktı: Merhaba "Python"
```
 
### Integer (int)
 
```python
sayı = 10
print(sayı)
print(type(sayı))
```
 
### Float
 
Virgül yerine **nokta** kullanılır.
 
```python
kesir = 3.14
print(kesir)
print(type(kesir))
```
 
### Boolean
 
`True` veya `False` değerlerini alabilir.
 
```python
doğrumu = True
yanlışmı = False
print(doğrumu, yanlışmı)
print(type(doğrumu), type(yanlışmı))
```
 
---
 
## String
 
### Değişken Değiş Tokuşu (Swapping)
 
```python
değer1, değer2, değer3, değer4 = 1, 2, 3, 4
değer1, değer2, değer3, değer4 = değer2, değer1, değer4, değer3
print(değer1, değer2, değer3, değer4)
```
 
### Replace
 
`.replace("değiştirilecek", "yerine geçecek")` şeklinde kullanılır.
 
```python
metin = "akakakakakaeleleleleleleonononononono".replace("a", "s")
print(metin)
```
 
### Len
 
`len()` bir string'in uzunluğunu (boşluklar dahil) verir. int ve float için kullanılmaz.
 
```python
metin2 = "Merhaba benim adım Eren"
print(len(metin2))
```
 
---
 
## Format
 
`.format(değişken1, değişken2, ...)` kullanıldığında süslü parantezlere sırayla değerler yerleşir:
 
```python
myStr = "merhaba"
yourStr = "hola"
print("bizde hello {} olarak sizde {} olarak söylenir".format(myStr, yourStr))
```
 
Aynı işlem **f-string** ile de yapılabilir:
 
```python
print(f"Bizde hello {myStr} olarak sizde {yourStr} olarak söylenir.")
```
 
---
 
## Aritmetik Operatörler
 
```python
a, b, c = 10, 5, 3
 
print(a + b)   # Toplama
print(a - b)   # Çıkarma
print(b * c)   # Çarpma
print(a / b)   # Bölme
print(a // c)  # Kalansız bölme (tam sayı)
print(c ** 2)  # Üs alma
print(a % c)   # Mod alma → 10 MOD 3 = 1
```
 
String ifadelerde `*` operatörü ile tekrar sağlanır:
 
```python
print("Merhaba " * 5)
ad = "eren "
print(ad * 3)
```
 
Kısayol atama operatörleri:
 
```python
a += 1   # a = a + 1
a -= 2   # a = a - 1
a *= 3   # a = a * 3
a /= 4   # a = a / 4
```
 
---
 
## Tür Dönüşümleri
 
`str()`, `float()`, `int()` fonksiyonları ile veri tipleri birbirine dönüştürülebilir.
 
```python
sayı = 4.5
print(int(sayı))  # int'e çevirdiğimiz için sadece tam kısmı (4) yazdırır
```
 
---
 
## İndexleme
 
İndeksler her zaman **0**'dan başlar; negatif indexler sondan sayar.
 
```python
merhaba = "merhaba"
print(merhaba[0])   # m
print(merhaba[-1])  # a (sondan 1.)
 
name = "MREN"
print(name[-1])
print(name[-2])
```
 
Belirli bir aralıktaki elemanları almak için:
 
```python
# değişken[başlangıç : bitiş : artış]
surname = "kiraz"
print(surname[0:5:2])
```
 
---
 
## String Metotları
 
### capitalize()
 
İlk harfi büyütür.
 
```python
metin3 = "memduh eren kiraz"
print(metin3.capitalize())
```
 
### upper() / lower()
 
```python
metin4 = "python öğreniyorum."
print(metin4.upper())
 
metin5 = "PYTHON ÖĞRENIYORUM."
print(metin5.lower())
```
 
### isupper() / islower()
 
```python
char = 'E'
print(char.isupper())  # True
print(char.islower())  # False
```
 
### title()
 
Her kelimenin ilk harfini büyütür.
 
```python
print("python öğreniyorum.".title())
```
 
### replace()
 
```python
metin6 = "bilgisayar mühendisliği"
print(metin6.replace("bilgisayar", "elektrik elektronik"))
```
 
### strip() / lstrip() / rstrip()
 
```python
metin7 = "    boşluk bıraktım     "
print(metin7.strip())    # Baş ve son boşlukları siler (aradakileri değil)
 
metin8 = "     Merhaba Dünya    "
print(metin8.lstrip())   # Sadece soldakileri siler
print(metin8.rstrip())   # Sadece sağdakileri siler
```
 
### center()
 
Stringi belirtilen uzunluğa göre ortalar. 2 parametre alır: karakter sayısı ve dolgu karakteri.
 
```python
metinA = "Merhaba"
print(metinA.center(50, '*'))
```
 
---
 
## Input
 
`input()` kullanıcıdan **sadece string** alır. int/float almak istersek dönüşüm yapmalıyız.
 
```python
ad = input("adınızı giriniz: ")
print(ad)
 
yas = int(input("yaşınızı giriniz: "))
boy = float(input("boyunuzu giriniz: "))
```
 
---
 
## Liste (List)
 
Python listesi, farklı tiplerdeki birden fazla nesneyi bir arada tutabilen, **değişebilir (mutable)** ve **sıralı (ordered)** bir veri yapısıdır.
 
```python
meyveler = ["elma", "kiraz", "armut", "erik"]
print(meyveler)
print(type(meyveler))
 
print(meyveler[2])
print(meyveler[-1])  # sondan başlar
 
mylist = [12, 13, "kalem", "kağıt", 14, "silgi"]
mylist[2] = "kalemtıraş"  # index 2'yi (3. eleman) değiştirdik
print(mylist)
```
 
### append()
 
Elemanı listenin sonuna ekler.
 
```python
mylist.append(3.14)
```
 
### pop()
 
Son elemanı siler; `pop(index)` verilen indexi siler.
 
```python
mylist2 = [3, 4, 5, 6, 7]
mylist2.append("sayı")
enSon = mylist2.pop()
mylist2.pop(0)
```
 
### index() / count()
 
```python
mylist3 = ["a", "b", 12, "d", 45]
print(mylist3.index("b"))  # kaçıncı indexte olduğunu bulur
 
mylist4 = ["e", "e", "e", "r", "r", "n"]
print(mylist4.count("e"))  # kaç adet olduğunu bulur
```
 
### remove() / del / insert()
 
```python
mylist4.remove("r")  # spesifik elemanı siler
 
liste = ["ev", "ağaç", "araba", "yol", "insan"]
del liste[2]              # index 2'yi siler
liste.insert(2, "köpek")  # index 2'ye ekler
```
 
### Listeleri Birleştirme ve İç İçe Listeler
 
```python
my_list1 = [1, 2, 3]
my_list2 = ["a", "b", "c"]
 
my_lists = my_list1 + my_list2       # birleştirme
nested = [my_list1, my_list2]        # iç içe liste
 
numbers = list(range(3, 30, 2))      # 3'ten 30'a kadar 2'şer artan liste
 
lists = [["eren", "kiraz"], ["emre", "vişne"]]
print(lists[0][1])  # Çıktı: kiraz
```
 
### sorted() vs sort()
 
`sorted()` yeni bir liste döndürür, orijinali değiştirmez; `sort()` orijinal listeyi değiştirir ve değer döndürmez.
 
```python
mylist7 = ["elma", "erik", "cilek", "armut", "portakal"]
print(sorted(mylist7))                 # alfabetik sıralı yeni liste
print(sorted(mylist7, reverse=True))   # ters sıralama
 
sayilar2 = [99, 2, 13, 7, 21, 79]
sayilar2.sort()                        # listeyi kendisi değiştirir
sayilar2.sort(reverse=True)
```
 
### extend() / clear() / copy()
 
```python
liste1 = [1, 3, 5, 7]
liste2 = [2, 4, 6, 8]
liste1.extend(liste2)  # liste2'yi liste1'e ekler
 
liste = [1, 2, 3, 4]
liste.clear()           # tüm elemanları siler
 
listeA = [1, 2, 3, 4]
listeB = listeA.copy()  # bellekte yeni bir alana kopyalar
```
 
> **id()** fonksiyonu, bir değişkenin bellekte nerede tutulduğunu gösterir: `id(isim)`
 
---
 
## Sözlük (Dictionary)
 
Süslü parantezlerle tanımlanır; **key (anahtar)** ve **value (değer)** çiftlerinden oluşur. Key sadece string veya int olabilir, value her tür veriyi tutabilir.
 
```python
sözlük = {"apple": "elma", "cheery": "kiraz", "melon": "kavun", "sayı": "rakamlar"}
 
print(sözlük["apple"])           # değere anahtarla erişim
sözlük["strawberry"] = "çilek"   # yeni anahtar ekleme
sözlük["melon"] = "karpuz"       # mevcut anahtarın değerini güncelleme
 
print(sözlük.keys())    # tüm anahtarlar
print(sözlük.values())  # tüm değerler
print(sözlük.items())   # anahtar-değer çiftleri
 
print(len(sözlük))          # anahtar sayısı
print("apple" in sözlük)    # anahtar var mı? → True/False
 
del sözlük["cheery"]              # anahtarı sil
sözlükKopyası = sözlük.copy()     # sözlüğü kopyala
```
 
### get()
 
Anahtar sözlükte varsa değerini döndürür; yoksa belirttiğimiz varsayılan değeri döndürür (sözlüğü değiştirmez).
 
```python
print(sözlük.get("banana", "ANAHTAR MEVCUT DEĞİL"))
```
 
### setdefault()
 
Anahtar sözlükte varsa değerini döndürür; yoksa anahtarı verilen değerle **sözlüğe ekler**.
 
```python
meyveler = {"Elma": 5, "Kiraz": 10}
print(meyveler.setdefault("Elma"))    # zaten var, değerini döndürür
print(meyveler.setdefault("Muz", 8))  # yok, sözlüğe ekler
```
 
---
 
## Setler (Kümeler)
 
Birden çok veri tipini barındırabilen, **tekrarlı elemanları saklamayan** veri yapısıdır.
 
```python
küme = {"python", "python", "python", "C#", "Java", "HTML", "CSS", 4, 5, 4, 8}
print(küme)  # tekrarlar tek bir elemana indirgenir
 
küme1 = set("memduh eren kiraz")  # string'in her karakterini bir kez alır
küme.add("programlama dilleri")   # yeni eleman ekleme
```
 
### Kümelere Özel İşlemler
 
```python
kume1 = {1, 2, 3, 4, 5}
kume2 = {3, 5, 7, 9, 2}
 
print(kume1.union(kume2))         # Birleşim
print(kume1.intersection(kume2))  # Kesişim
print(kume1.isdisjoint(kume2))    # Kesişim boş mu? (dolu → False)
print(kume1.difference(kume2))    # kume1'de olup kume2'de olmayanlar
print(kume2.difference(kume1))    # kume2'de olup kume1'de olmayanlar
```
 
### frozenset
 
Değiştirilemez (immutable) bir küme türüdür.
 
```python
fkume = frozenset(kume1)
kume1.clear()   # normal küme olduğu için değişir
fkume.clear()   # frozenset olduğu için hata verir / değişmez
```
 
---
 
## Tuple (Demet)
 
Birden fazla veri türünü bir arada tutan, **değiştirilemez (immutable)** bir veri yapısıdır.
 
```python
demet = ("a", "b", "c", "d", "e", "f", "e", "e")
 
print(type(demet))
print(demet[3])       # 3. index
print(demet[-2])      # sondan 2. index
print(demet[:4])      # baştan 4. indexe kadar (4 dahil değil)
print(demet.count("e"))
```
 
> Tuple'a yeni eleman ekleme (`demet.add(...)`) veya eleman değiştirme (`demet[8] = ...`) **hata verir**, çünkü tuple immutable'dır.
 
---
 
## Karar Yapıları
 
### If - Elif - Else
 
```python
vize = int(input("VİZE NOTUNUZU GİRİNİZ: "))
final = int(input("FİNAL NOTUNUZU GİRİNİZ: "))
ortalama = (vize + final) / 2
 
if ortalama >= 50:
    print("GEÇTİNİZ!")
else:
    print("KALDINIZ!")
```
 
```python
sayi6 = int(input("Sayı Giriniz: "))
if sayi6 < 0:
    print("Sayınız 0'dan küçük")
elif sayi6 > 0:
    print("Sayınız 0'dan büyük")
else:
    print("Sayınız 0")
```
 
### and / or
 
`and` → her iki koşul da doğruysa `True`. `or` → herhangi biri doğruysa `True`.
 
```python
sayi1, sayi2 = 10, 5
 
if sayi1 > sayi2 and sayi1 / sayi2 > 0:
    print("DOĞRU")
 
if sayi1 > sayi2 or sayi1 / sayi2 < 0:
    print("DOĞRU")
```
 
### Ternary Operatör (Üçlü Operatör)
 
Çok satırlı if-else bloklarını tek satıra indirger (okunabilirlik açısından az tercih edilir).
 
```python
# <doğru durum> if <koşul> else <yanlış durum>
x, y = 10, 15
kucuk = x if x < y else y
print(kucuk)
 
x, y = 2, 5
print("X, Y'DEN BÜYÜK") if x > y else print("X, Y'DEN KÜÇÜK")
```
 
---
 
## Döngüler
 
### range()
 
```python
for i in range(0, 20, 2):  # 0'dan 20'ye, 2'şer artarak
    print(i)
```
 
### enumerate()
 
İterable bir nesnenin (liste, string, tuple vb.) hem elemanını hem indexini `tuple` olarak döndürür.
 
```python
listeNum = ["Elma", "Kiraz", "Erik", "Karpuz", "Armut"]
for i in enumerate(listeNum):
    print(i)
```
 
### While Döngüsü
 
Belli bir koşul sağlanana kadar çalışır.
 
```python
i = 0
while i <= 10:
    print(i)
    i += 1
 
i = 0
while True:  # aksi belirtilmedikçe sonsuz döngü
    print(i)
    i += 2
    if i == 100:
        break  # döngüyü kırar
```
 
### For Döngüsü
 
```python
harfler = "abcdefghıjklmnoprstuvyzqwx"
for harf in harfler:
    print(harf)
 
sayac = 0
trHarfler = "üişçöğ"
parola = input("parolanız: ")
for karakter in parola:
    if karakter in trHarfler:
        sayac += 1
if sayac != 0:
    print("parolada türkçe karakter olmamalı!")
```
 
---
 
## Fonksiyonlar
 
Bir kod bloğunu birden çok yerde kullanabilmemizi sağlayan yapılardır.
 
```python
def ortalama(sayı1, sayı2):
    ortalama = (sayı1 + sayı2) / 2
    print("ORTALAMANIZ: ", ortalama)
 
ortalama(56, 96)
```
 
### İsimsiz / İsimli Parametreler
 
Argümanların **sırasına** göre (isimsiz) ya da parametre **adına** göre (isimli) gönderilebilir:
 
```python
def islem(p1, p2, p3):
    print(f"Merhaba {p1}. Hoş Geldin!")
    print(f"Çarpım Sonucu: {p2 * p3}")
 
islem(isim, s1, s2)                   # isimsiz — sıraya dikkat
islem(p2=s1, p1=isim, p3=s2)          # isimli — sıra önemsiz
```
 
### Default (Varsayılan) Parametreler
 
Argüman verilmezse varsayılan değer kullanılır. Bir parametre varsayılan olduğunda sağındaki tüm parametreler de varsayılan olmalıdır.
 
```python
def islem(p1='Eren', p2=4, p3=5):
    print(f"Merhaba {p1}. Hoş Geldin!")
    print(f"Çarpım Sonucu: {p2 * p3}")
 
islem()  # hata almadan varsayılan değerleri kullanır
```
 
### `*args` — İsimsiz Sonsuz Parametre
 
```python
def func(*isimsiz):
    print(type(isimsiz))  # tuple olarak tutulur
    return sum(isimsiz)
 
sonuc = func(11, 45, 69, 86, 23, 10, 58, 78)
```
 
### `**kwargs` — İsimli Sonsuz Parametre
 
```python
def func(**isimli):
    print(type(isimli))  # dict olarak tutulur
    return isimli
 
sonuc = func(ad="Eren", soyad="Kiraz", yas=21)
```
 
Normal, `*args` ve `**kwargs` birlikte kullanılabilir — sıra her zaman: normal → `*args` → `**kwargs`.
 
```python
def func(p1, p2, *args, **kwargs):
    print("Normal Parametreler: ", p1, p2)
    print("args: ", args)
    print("kwargs: ", kwargs)
 
func(False, True, 1, 2, 3, ad='EREN', soyad='KİRAZ')
```
 
### Tip İpuçları (Type Hints)
 
```python
def func(sayi1: int, sayi2: int, sayi3: int) -> int:
    return sayi1 + sayi2 + sayi3
```
 
### Local ve Global Değişkenler
 
```python
def loc():
    x = 10  # local — fonksiyon dışından erişilemez
    print(x)
 
x = 10  # global — her yerden erişilebilir
def glo():
    print(x)
 
def hi():
    global x  # fonksiyon içinde global değişken oluşturma (pek tercih edilmez)
    x = "Hello"
```
 
### Pass Deyimi
 
Boş bir kod bloğunda hata almamak için kullanılır.
 
```python
def func():
    pass
 
func()
```
 
---
 
## Kaçış Dizileri
 
| Dizi | Anlamı |
|------|--------|
| `\n` | Satır başı (yeni satıra geçer) |
| `\t` | TAB boşluk |
| `\a` | Ses (bip) |
| `\b` | İmleci bir sola kaydırır |
 
```python
print("merhaba \nben eren \nbilgisayar mühendisliği okuyorum.")
print("Merhaba \tBen Eren \tBilgisayar Müh. Örğrencisiyim.")
print('youtube', '\b.', '\bcom')
```
 
---
 
## Hata Yönetimi
 
### Hata Türleri
 
- **Syntax Hataları** — Geliştirici kaynaklı: ayraç, iki nokta, virgül eksikliği vb.
- **Mantıksal Hatalar** — Kod çalışır ama sonuç yanlıştır.
- **Exceptions (İstisnalar)** — Kullanıcı ya da geliştirici kaynaklı çalışma zamanı hataları.
### Sık Karşılaşılan Exception'lar
 
```python
# KeyboardInterrupt → Ctrl+C ile sonsuz döngüden çıkarken alınır
 
# SyntaxError
# print "HELLO"  → Missing parentheses in call to 'print'
 
# ZeroDivisionError
sayi = int(input("Sayı Giriniz: "))
print(sayi / 0)
 
# NameError → tanımlanmamış değişken kullanımı
print(sayı)
 
# IndentationError → girinti eksikliği
 
# ValueError → yanlış veri tipinde atama
sayi = int(input("Sayı Giriniz: "))  # harf girilirse hata
 
# TypeError → desteklenmeyen işlem, örn: 1 + "Hello"
 
# IndexError → olmayan bir indexe erişim
list = [0, 1, 2, 3]
print(list[5])
```
 
### Try - Except - Else - Finally
 
```python
try:
    sayi1 = int(input("1. Sayıyı Giriniz: "))
    sayi2 = int(input("2. Sayıyı Giriniz: "))
    print("Sayıların Çarpımı: ", sayi1 * sayi2)
except ValueError as ex:
    print("ValueError Hatası: ", ex)
    print("Sayısal Veri Giriniz!")
else:
    print("Try Bloğu Doğru Çalıştı.. Else Bloğu")   # hata yoksa çalışır
finally:
    print("Finally Bloğu..")                         # her durumda çalışır
```
 
### Raise Deyimi
 
Geliştiricinin istediği koşulda kasıtlı olarak hata fırlatmasını sağlar.
 
```python
try:
    sayi = int(input("Sayı Giriniz: "))
    if sayi == 5:
        raise Exception("Sayı 5'e Eşit Olamaz!")
    else:
        print("Sayınız: ", sayi)
except Exception as ex:
    print("Hata: ", ex)
```
 
### Assert (AssertionError)
 
Doğru olduğunu iddia ettiğimiz koşulları kontrol eder; iddia yanlışsa `AssertionError` fırlatır.
 
```python
veri = []
 
def ekle(p1: list):
    assert len(p1) != 0, "Listeniz Boş!"
    for i in range(0, 11):
        p1.append(i)
 
try:
    ekle(veri)
except AssertionError as ex:
    print("Hata: ", ex)
```
 
> **Ne zaman ne kullanılır?** Programın çökmemesini istiyorsak `if-else`; kullanıcı kaynaklı hata bildirmek istiyorsak `raise`; geliştirici/ön koşul kontrolü içinse `assert` tercih edilir.
 
---
 
## Dosya İşlemleri
 
### Dosya Türleri ve Erişim Biçimleri
 
- **Text file** (`.txt`) — string veri tutar
- **Binary file** (`.dat`) — 0-1 bit olarak veri tutar
- **Sequential Access** — verilere sırayla erişim
- **Direct Access** — verilere doğrudan erişim
### Dosya Modları
 
| Mod | Açıklama |
|-----|----------|
| `r` | Okuma — dosya yoksa hata verir |
| `a` | Ekleme — dosya yoksa oluşturur, varsa sonuna ekler |
| `w` | Yazma — dosya varsa siler ve yeniden oluşturur |
| `x` | Oluşturma — dosya varsa hata verir |
| `r+`, `w+`, `a+`, `x+` | Yukarıdakilerin okuma-yazma birleşik (plus) modları |
| `rb`, `wb`, `ab` | Binary dosya modları |
 
```python
open("denemeW.txt", "w")        # programın klasöründe oluşturur
open("../deneme.txt", "w")      # bir üst klasörde oluşturur
open(r"C:\Users\Blake\temp\test.txt", "w")  # path başına r (raw string) koyulur
```
 
> `"x"` modunda dosya zaten varsa `FileExistsError` alınır. Dosyayla işlem bittikten sonra **mutlaka kapatılmalıdır** (`close()`), aksi halde değişiklikler kaybolabilir ve RAM boşuna kullanılır.
 
### Yazma ve rstrip ile Okuma
 
```python
dosya = open("filozoflar.txt", "w")
dosya.write("John Locke\n")
dosya.write("David Hume\n")
dosya.write("Edmund Burke\n")
dosya.close()
 
dosya = open("filozoflar.txt", "r")
satir1 = dosya.readline().rstrip("\n")  # \n karakterine kadar alır
satir2 = dosya.readline().rstrip("\n")
satir3 = dosya.readline().rstrip("\n")
dosya.close()
```
 
> Dosyaya sayısal veri yazarken mutlaka `str()` ile string'e çevrilmelidir; aksi halde `TypeError` alınır.
 
### With Deyimi
 
`close()` çağırmaya gerek kalmadan dosyayı otomatik kapatır.
 
```python
with open("dosya.txt", "w") as fi:
    fi.write("Hello\nWorld\nPython 3.9.4")
 
with open("dosya.txt", "r") as fi:
    print(fi.read(3))       # 3 karakter okur
    print(fi.readline())    # satır satır okur, string döndürür
    print(fi.readlines())   # tüm satırları liste olarak döndürür
```
 
### tell() ve seek()
 
```python
with open("dosya.txt", "r") as fi:
    print(fi.tell())    # imlecin bulunduğu karakteri gösterir
    print(fi.read())
    print(fi.tell())    # okuduktan sonra imleç sona gelir
    fi.seek(6)           # imleci 6. karaktere getirir
    print(fi.read())
```
 
### Dosya Güncelleme
 
```python
# Başa veri eklemek için "r+" modu:
with open("dosya.txt", "r+") as fi:
    eskiVeriler = fi.read()
    fi.seek(0)
    fi.write("My name is Eren\n" + eskiVeriler)
 
# Sona veri eklemek için "a" modu (eski veriler silinmez):
with open("dosya.txt", "a") as fi:
    fi.write("\nPython Öğreniyorum..")
 
# Ortaya veri eklemek için yine "r+" ve liste dönüşümü:
with open("dosya.txt", "r+") as fi:
    eskiVeri = fi.readlines()
    eskiVeri.insert(1, "My surname is Kiraz\n")
    fi.seek(0)
    fi.writelines(eskiVeri)
```
 
---
 
## İleri Seviye Yapılar
 
### İç İçe Fonksiyonlar
 
```python
def dfunc():
    print("Dış Fonksiyon!")
    def ifunc():
        print("İç Fonksiyon!")
    ifunc()
 
dfunc()
```
 
### Closure
 
Bir fonksiyonun içindeki fonksiyonu, çağırmadan (`()` kullanmadan) `return` ederek dışarıya taşımasıdır.
 
```python
def func1(p1: int):
    print("1. Sayı: ", p1)
    def func2(p2: int):
        print("2. Sayı: ", p2)
        print("Çarpım: ", p1 * p2)
        return p1 * p2
    return func2
 
v1 = func1(24)  # v1 artık func2'nin kendisi
v2 = v1(85)     # func2'yi çağırdık
print(v2)
```
 
### Decorators
 
Parametre olarak fonksiyon alan, geriye fonksiyon döndüren ve ana fonksiyona yeni özellik kazandıran fonksiyonlardır.
 
```python
def decarator(func):
    def sekil():
        print("**********\n" + func() + "\n**********")
    return sekil
 
def isim():
    return input("Lütfen İsminizi Giriniz: ")
 
v1 = decarator(isim)
v1()
```
 
### Recursive (Özyineli) Fonksiyonlar
 
Kendi içinde kendini çağıran fonksiyonlardır; sonsuz döngüye girmemesi için bir durdurma koşulu gerekir.
 
```python
def fakt(n: int):
    if n == 1:
        return 1
    else:
        return n * fakt(n - 1)  # n! = n * (n-1)!
 
print(fakt(6))
```
 
### Lambda Fonksiyonları
 
İsimsiz, tek satırlık ve tek değer döndüren fonksiyonlardır.
 
```python
# 1. Kullanım: doğrudan çağırmak
a = (lambda x: x ** 2)(12)
 
# 2. Kullanım: bir değişkene atamak
b = lambda x: x ** 3
 
la = lambda isim, soyİsim: f"AD: {isim}\nSOYAD: {soyİsim}"
print(la("Eren", "Kiraz"))
 
# Başka bir fonksiyonun içinde/return değeri olarak kullanımı:
def topla(p1):
    return lambda x: x + p1
 
a = topla(3)
print(a(6))
```
 
### Iterators (Yineleyiciler)
 
- **Iterable** — gezilebilen nesne (liste, tuple, sözlük...)
- **Iterator** — bu nesnenin elemanlarında gezmemizi sağlayan araç
```python
sayilar = [1, 2, 3, 4]
veri = iter(sayilar)      # iterable → iterator
print(next(veri))         # elemanları tek tek döndürür
print(next(veri))
# Eleman kalmayınca StopIteration hatası alınır
 
harfler = ["a", "b", "c", "d", "e"]
veri = iter(harfler)
while True:
    try:
        print(next(veri))
    except StopIteration:
        break
```
 
### Generators
 
Bir defalık kullanılan, `yield` ile değer döndüren ve iterasyonun kaldığı yerden devam eden yapılardır. `range()` de bir generator ile yazılmıştır.
 
```python
def generator():
    i = 0
    yield i
    i += 2
    yield i
    i += 4
    yield i
 
x = generator()
print(next(x))
print(next(x))
```
 
Bellek verimliliği için normal fonksiyon yerine generator kullanımı:
 
```python
def generator(p1):
    for i in p1:
        yield i ** 3
 
x = generator(range(1, 11))
for i in x:
    print(i)
 
# Kısa (generator expression) hali:
x = (i ** 3 for i in range(1, 11))
```
 
### Comprehensions
 
Döngüleri tek satırda, okunabilir şekilde yazmamızı sağlar.
 
| Yapı | Sembol |
|------|--------|
| Liste | `[]` |
| Küme | `{}` |
| Generator | `()` |
| Sözlük | `{key: expression for ...}` |
 
```python
kuvvetAl = [i ** 4 for i in range(1, 11)]           # liste comprehension
kuvvetAl = {i: i ** 4 for i in range(1, 11)}        # sözlük comprehension
 
metin = "Memduh Eren Kiraz"
v1 = {i for i in metin if i in "meKzqdhilp"}        # koşullu küme comprehension
```
 
---
 
## Modüller
 
Büyük programları küçük ve yönetilebilir hale getirmek için modüller kullanılır. `import` ile içe aktarılır.
 
```python
import işlemler
v1 = işlemler.toplama(2, 5)
 
import işlemler as işl
v1 = işl.toplama(445, 62)
 
from işlemler import toplama
v1 = toplama(145, 78)  # doğrudan çağırabiliriz
```
 
> Eğer programda aynı isimde kendi fonksiyonumuzu tanımlarsak, Python o an tanımlı olan (kendi) fonksiyonu kullanır.
 
### Random Modülü
 
```python
import random
 
rastSayı = random.randint(1, 100)
print("Rastgele Sayınız:", rastSayı)
```
 
**Örnek — Sayı Tahmin Oyunu:**
 
```python
number = random.randint(1, 100)
tahmin = 0
adet = 0
tahminler = []
 
while tahmin != number:
    tahmin = int(input("Tahmininiz Nedir: "))
    if tahmin < number:
        print("Lütfen Sayınızı Yükseltin!")
    elif tahmin > number:
        print("Lütfen Sayınızı Düşürün!")
    else:
        print("Tebrikler! Tahmininiz Doğru")
    if tahmin != number:
        adet += 1
        tahminler.append(tahmin)
 
print("Tahmin Sayısı: ", adet)
print("Tahminleriniz: ", tahminler)
```
 
### Math Modülü
 
| Fonksiyon | Açıklama |
|-----------|----------|
| `math.pi` | Pi sayısı |
| `math.e` | e sayısı |
| `math.factorial()` | Faktöriyel |
| `math.ceil()` | Üst tam sayıya yuvarlar |
| `math.floor()` | Alt tam sayıya yuvarlar |
| `math.fabs()` | Mutlak değer |
| `math.fmod(a, b)` | a % b (mod işlemi) |
 
**Örnek — Daire Çevresi ve Alanı:**
 
```python
import math
 
yarıcap = int(input("Dairenin Yarıçapını Giriniz: "))
çevre = 2 * math.pi * yarıcap
alan = math.pi * (yarıcap ** 2)
 
print(f"Dairenin Çevresi: {çevre:.2f}")
print(f"Dairenin Alanı: {alan:.2f}")
```
 
---
 
## Class'lar (OOP)
 
### Terminoloji
 
| Terim | Anlamı |
|-------|--------|
| Class | Sınıf |
| Object | Nesne |
| Instance | Üretilen nesne |
| Instantiating | Nesne üretme işlemi |
| Data Attributes | Veri öznitelikleri |
| Class Attributes | Sınıf özellikleri |
| Metot | Class içindeki fonksiyonlar |
| Constructor | Yapıcı metot |
 
Sınıf, bir nesnenin özelliklerini ve işlevlerini tanımlayabileceğimiz **şablondur**. Bir sınıftan sınırsız nesne türetilebilir.
 
### Class Attributes
 
Nesnelerin özelliklerinin **varsayılan** değeridir; birden fazla nesne oluşturulduğunda hepsi aynı varsayılan değeri paylaşır (bu istenmeyen bir durum olabilir — bunun için `__init__` kullanılır).
 
```python
class Insan:
    # class attributes
    ad = "###"
    soyad = "***"
    boy = 0
    kilo = 0
 
i1 = Insan()
print(i1.ad, i1.soyad, i1.boy, i1.kilo)  # her nesne için aynı varsayılan değerler
```
 
### `__init__` Metodu
 
Nesne oluşturulurken ilk değer ataması yapan **constructor**'dır (dunder method). Yazılmasa bile Python tarafından örtük olarak vardır.
 
### `__str__` Metodu
 
C#'taki `ToString()` benzeri; nesneyi string olarak temsil eder.
 
### self Parametresi
 
Class içindeki data attribute ve metotlara erişmek için kullanılan referanstır.
 
```python
class Insan:
    def __init__(self, ad, soyad, boy, kilo):
        # data attributes
        self.ad = ad
        self.soyad = soyad
        self.boy = boy
        self.kilo = kilo
 
    def __str__(self):
        return (f"İnsanın Adı: {self.ad} \nİnsanın Soyadı: {self.soyad} "
                f"\nİnsanın Boyu: {self.boy} \nİnsanın Kilosu: {self.kilo}")
 
i1 = Insan("Eren", "Kiraz", 185, 75)
print(i1.__str__())
```
 
### Inheritance (Kalıtım - Miras Alma)
 
Bir sınıftaki özellik ve metotların başka bir sınıfta tekrar yazılmadan kullanılmasını sağlar.
 
- **Base Class** — miras veren (türetilen) sınıf
- **Derived Class** — miras alan (türeyen) sınıf
```python
class derivedClass(baseClass):
    ...
```
 
```python
import user
 
u1 = user.Manager("Eren", "WisTonWest", 1245)  # User'dan miras aldı
u2 = user.User("Emre", "Qenavja", 2356)
u3 = user.CEO("Resul", "Mast.", 4578, "elbistan@gmail.com")
 
print(user.Manager.__bases__)  # base class'ı gösterir
```
 
### Polymorphism (Çok Biçimlilik)
 
Base class'taki bir metodu, derived class içinde **yeniden tanımlayarak** farklı sınıflarda farklı işlevlerde kullanabiliriz (örn. `User` sınıfındaki `__init__`'i `CEO` sınıfında yeniden tanımlamak).
 
### isinstance()
 
Bir nesnenin belirli bir sınıfa ait olup olmadığını kontrol eder (`True`/`False` döndürür).
 
```python
i1 = ogrenci.Ogrenci("Eren", "Kiraz", 2001, "Bilg. Müh.")
print(isinstance(i1, ogrenci.Ogrenci))  # True
print(isinstance(i1, user.User))        # False
 
x = [1, 2, 3]
print(isinstance(x, list))  # diğer veri tipleri için de kullanılabilir
```
 
---
 
## Alıştırma: Employee / ProductionWorker
 
**Görev:** Aşağıdaki bilgiler için veri özniteliklerini tutan bir `Employee` (Çalışan) sınıfı yazın:
 
- İşçi adı
- Çalışan sayısı
Ardından `Employee` sınıfının bir alt sınıfı olan `ProductionWorker` sınıfını yazın. Bu sınıf şu veri özniteliklerini tutmalıdır:
 
- Shift numarası (1, 2 veya 3 gibi bir tam sayı) — gündüz vardiyası `1`, gece vardiyası `2`
- Saatlik ödeme oranı
Her sınıf için uygun **accessor** (erişimci) ve **mutator** (değiştirici) metotlarını yazınız.
 
Son olarak, `ProductionWorker` sınıfından bir nesne oluşturan, kullanıcıdan her veri özniteliği için giriş isteyen, verileri nesnede saklayan ve accessor metotları kullanarak ekranda gösteren bir program yazınız.