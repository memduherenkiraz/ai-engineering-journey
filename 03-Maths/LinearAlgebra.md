# LİNEER DENKLEM SİSTEMLERİ VE MATRİSLERLE GÖSTERİMİ

## **Lineer Denklem Nedir?**

İçerdiği tüm bilinmeyenlerin (x, y gibi) birinci dereceden olduğu ve bilinmeyenlerin birbiriyle çarpım durumda olmadığı matematiksel eşitliklerdir.
a1x1+ a2x2 + … + anxn = b
- x1, x2, …, xn : Bilinmeyenleri temsil eder.
- a1, a2, …, an : Katsayıları temsil eder. 
- b: Denklemin sonucunu temsil eder.

**Örnekler:**
- 2x + 4y = 12
- x – 2y = 9
- x2 + y = 8  -> Lineer denklem değil.
Ayrıca bir lineer denklemde trigonometrik veya logaritmik ifadeler olmaz. Değişkenlerin üsleri her zaman 1’dir. Bilinmeyenlerin çarpımı lineerliği bozar.

## **Lineer Denklem Sistemi Nedir?**

Aynı bilinmeyenlere sahip, birden fazla lineer denklemden oluşan gruba lineer denklem sistemi denir.

> **Not:** Denklem sistemlerinde amaç, denklemlerin hepsini sağlayan bilinmeyenleri bulmaktır.

**Örnek:**
- x + 4y – 5z = 10
- y + 2z = 8

## **Denklem Sistemlerinin Matrisler ile Gösterimi**

Matris; sayıların, sembollerin ve ifadelerin köşeli parantezler içinde satır ve sütunlar şeklinde sıralanmasıyla oluşan matematiksel tablolardır.

- 2x - 3y = 10  
- x + 4y = 8

```
| 2  -3 |   | x |   | 10 |
| 1   4 | * | y | = | 8  |
    A     *   x   =    b
```

- A : Katsayılar Matrisi
- x: Bilinmeyenler Matrisi
- b: Sonuç Matrisi

> **Not:** Matrislerde her sütun bir bilinmeyeni temsil eder. Her satır bir denklemi temsil eder. Yani sütun sayısı bilinmeyen sayısını, satır sayısı denklem sayısını verir.

## **Genişletilmiş Katsayılar Matrisi**

Genişletilmiş Katsayılar matrisinde köşeli parantez açılıp içine katsayılar yazıldıktan sonra kay-tsayıların sağına dikey kesikli çizgi çekilir ve sonuçlar yazılır.

Son olarak parantez kapatılır.

```
3x - 2y = 5
x + y = 4
3x + y = 6

|3 -2  . 5|
|1  1  . 4|
|3  1  . 6|
```

