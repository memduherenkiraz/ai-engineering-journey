# PYTHON NOTES

## Day-1 12.07.2026

- Python'da yorum satırı "#" ile oluşturulur.

### Print Fonksiyonu
- Bir çıktıyı ekrana yazdırmak için print() fonksiyonu kullanılır.
- Birden fazla satırdan oluşan çıktılar "\" kaçış karakteri ile ekrana sığdırılabilir.

- print() fonksiyonun içinde geliştiriciler tarafından konulmuş parametreler vardır.
- Bunlar sep ve end parametreleridir.

- sep parametresi verdiğimiz parametrelerden sonra hangi karakterin geleceğini kontrol eder.
- Varsayılan değeri boşluktur.
- print("Merhaba","Ben","Eren", sep='+' )   # sep parametresini "+" olarak değiştirdik. Artık değişkenlerden sonra aralara + gelecek.

- end parametresi fonksiyon sonlandığında diğer fonksiyonun nereden başlayacağını belirtir.
- Varsayılan değeri \n dir. Yani fonksiyon sonlandığında diğer fonksiyon için alt satıra geçer.
- print("Merhaba", "Python", end= '\t')  # \t kaçış dizisi bir TAB boşluk bırakır.

- String değişkenimiz içindeki her karakteri ayrı ayrı yazdırmak için * kullanabiliriz.
- Bunlara yıldızlı parametre denir. Stringin içindeki her karakteri parametre olarak gönderir.
- Böylelikle stringin içindeki her karakter sep parametresindeki değere göre ayrılır.
- print(*"Hello my name is Eren. I am 20 years old.", sep='_')

### Değişkenler ve Veri Tipleri

- Değişkenler, "değişken adı = değer" olarak tanımlanır.
- Metinsel, mantıksal veya sayısal değerler tutabilirler.

- Integer (Tam sayı)
- Float (Kayar noktalı sayı)
- String (Karakter dizisi)
- Boolean (Mantıksal ifadeler)
- Complex (Karmaşık sayılar)
- List (Liste)
- Dictionary (Sözlük)
- Tuple (Demet)
- Set (Küme)

- Type Fonksiyonu
- "type" fonksiyonu ile değişkenlerin veri tiplerini görebiliriz.
- type(değişkenadı) olarak kullanılır.

- STRİNG
- String veri tipleri kelime ve cümleleri tutmamızı sağlar.
- String veri tipleri çift tırnak ile tanımlanır.

- name = "eren"
- print(name)
- print(type(name))

- Çift tırnak stringin başlayıp bittiğini gösterir. Ancak bazen çift tırnağı string oluşturmak için değil
- bir kelimeyi belirtmek, vurgulamak için kullanabiliriz. Bunun için kaçış karakteri kullanılırız. (\)

- print("Merhaba \"Python\"")     # Çıktı ---> Merhaba "Python"

- INTEGER(INT)
- Int veri tipleri tam sayıları tutmamızı sağlar.
- Int veri tipleri normal olarak tanımlanır.

- num = 10
- print(num)
- print(type(num))

- FLOAT
Float veri tipleri ondalıklı yani virgüllü sayıları tutmamızı sağlar.
Virgül yerine nokta kullanılır.

- pi = 3.14
- print(pi)
- print(type(pi))

Float'ı 10'un kuvvetlerini belirtmek için kullanılan "e" ile beraber kullanılabilir.

- v = 12e3
- print(v)
- print(type(v))

- BOOLEAN
Bool veri tipleri mantıksal veri tipleridir.
True veya False değerlerini alabilir.

- isTrue = True
- isFalse = False
- print(isTrue) , print(isFalse)
- print(type(isTrue)) , print(type(isFalse))

- NONETYPE
None veri tipi bir değişkenin veri tutmadığını gösterir. Yani değişkenin içi boştur.

- x = None
- print(x)
- print(type(x))

### Value Swapping
Değişkenlerin değerlerini birbirleriyle değiştirebiliz.

- a=12
- b=13
- a,b=b,a
- print(a,b)

### Tür Dönüşümleri
- str() 
- float() 
- int()

Int bir değeri floata dönüştürebiliriz yada tam tersini yapabiliriz.
- sayı=4.5
- print(int(sayı))   # print işleminde int e çevirdiğimiz için sadece tam sayıyı(4) yazdı.

### Input Fonksiyonu
İnput fonksiyonu kullanıcıdan sadece string ifade almamızı sağlar.

- ad= input("adınızı giriniz: ")
- print(ad)

İnt veya float tipinde değer alacaksak inputtan önce belirtmemiz lazım.

- yas= int(input("yaşınızı giriniz: "))
- print(yas)
- boy= float(input("boyunuzu giriniz: "))
- print(boy)

### Random Modulü
Random modülü Python içinde hazır gelen ve rastgele değer üretmek için kullanılan bir modüldür.
Randomu kullanmak için import etmemiz gerekir.  "import random"

- random() -> 0 dahil ve 1.0 hariç olmak üzere bu aralıkta rastgele float sayı üretir.

- print(random.random()) # Örn: 0.947382

- uniform(a, b) -> Belirtilen a ve b sınırları dahil olmak üzere bu aralıkta rastgele float sayı üretir.

- print(random.uniform(5.0, 10.0)) # Örn: 8.3248

- randint(a, b) -> Belirtilen a ve b sınırları dahil olmak üzere bu aralıkta rastgele integer sayı üretir.

- print(random.randint(2, 10)) # Örn: 7

- randrange(start, stop, step) -> Belirtilen start(dahil) ve stop(hariç) aralığında, belirlenen artış miktarına(step) uygun rastgele tam sayı üretir.

- print(random.randrange(0, 10, 2)) # (0, 2, 4, 6, 8) Örn: 8

- choice(list) -> Verilen bir dizi içinden rastgele eleman seçer.

- colors = ["red", "blue", "green", "pink"]
- print(random.choice(colors)) # Örn: blue

- choices(list, k) -> Verilen bir diziden k adet rastgele eleman seçer. Seçilen eleman tekrar seçilebilir. Liste döndürür.

- colors = ["red", "blue", "green", "pink"]
- print(random.choices(colors, k=2))
- ["blue", "pink"] gibi farklı elemanlar seçebilir.
- ["blue", "blue"] gibi aynı elemanıda seçebilir.

- sample(list, k) -> Verilen bir diziden k adet rastgele eleman seçer. Seçilen eleman tekrar seçilemez. Liste döndürür.

- colors = ["red", "blue", "green", "pink"]
- print(random.sample(colors, k=2)) # Örn: ["blue", "pink"]

- shuffle(list) -> Verilen bir listede, elemanların yerlerini rastgele karıştırır. Orijinal liste değişir.

- numbers = [1, 2, 3, 4]
- print(random.shuffle(numbers)) # Örn: [3, 1, 2, 4]

- seed() -> Rastgele sayı üretecini belirli bir başlangıç değerine sabitleyerek, kod her çalıştığında aynı "rastgele" sayının üretilmesini sağlar. (test ve hata ayıklamada kulanılır.)

- random.seed(42)
- print(random.randint(1, 100)) # Her çalıştığında 82 sayısını üretir.

- Random modülü sayı üretirken matematiksel formüller kullanır. seed() içine yazdığımız sayı(tohum), matematiksel formülün başlangıç noktasıdır ve herhangi bir anlamı yoktur (Genel olarak 42 kullanılır).
- seed() fonksiyonunda tohum 42 seçilirse, randint() fonksiyonu 1 - 100 aralığında hep 82 üretir.
- Eğer aynı Runtime'da iki kez çalıştırırsak bu sefer ikinci bir sayı üretir.

- random.seed(42)
- print(random.randint(1, 100)) # Her zaman 82 üretir. Programı kapatıp yeniden çalıştırdığına bile.
- print(random.randint(1, 100)) # Bu ise her zaman 15 üretir.