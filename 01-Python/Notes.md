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
- Float veri tipleri ondalıklı yani virgüllü sayıları tutmamızı sağlar.
- Virgül yerine nokta kullanılır.

- pi = 3.14
- print(pi)
- print(type(pi))

- BOOLEAN
- Bool veri tipleri mantıksal veri tipleridir.
- True veya False değerlerini alabilir.

- isTrue = True
- isFalse = False
- print(isTrue) , print(isFalse)
- print(type(isTrue)) , print(type(isFalse))

- NONETYPE
- None veri tipi bir değişkenin veri tutmadığını gösterir. Yani değişkenin içi boştur.

- x = None
- print(x)
- print(type(x))

### Value Swapping
- Değişkenlerin değerlerini birbirleriyle değiştirebiliz.

- a=12
- b=13
- a,b=b,a
- print(a,b)