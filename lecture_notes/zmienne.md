## Zmienne
Czym jest zmienna? Krótko mówiąc, jest to pojemnik na dane. Ma swoją nazwę, typ i wartość. Przykładowo w Pythonie możemy zdefiniować zmienną o nazwie liczba typu int o wartości 5 w następujący sposób:
```python
liczba = 5
```
Jak sama nazwa wskazuje, możemy tę wartość zmienić - po prostu przypisujac (w Pythonie służy do tego operator =) inną:
```python
liczba = 10
```
W Pythonie dostępnych jest kilkanaście wbudowanych typów zmiennych i wiele dodatkowych w bibliotece standardowej. Tutaj omówimy kilka podstawowych: typ logiczny (bool), typy liczbowe (int - l. całkowite, float - l. zmiennoprzecinkowe, complex - l. zespolone) oraz łańcuchy znaków, czyli napisy (str).
bool

Typ logiczny przyjmuje dwie wartości: True i False. Najczęściej są one wynikiem porównania dwóch wartości, np. liczb całkowitych. W Pythonie jest osiem operatorów porównania:

```
<, <=  - mniejszy, mniejszy bądź równy
>, >=  - analogiczne większości
==     - równości
!=     - różności
is     - identyczność (a is b - a jest tym samym obiektem, co b)
is not - przeciwny do is
```
Sprawdź ich działanie, korzystając z powłoki Pythona.

Ponadto, dla typu logicznego, mamy do dyspozycji operatory koniunkcji, alternatywy i zaprzeczenia: and, or oraz not.
int

Zmienne typu int w Pythonie mogą być dowolnej wielkości. Wyglądają i działają jak liczby całkowite - można wykonywać na nich wszystkie podstawowe działania: dodawanie (+), odejmowanie (-), mnożenie (*), dzielenie (/), dzielenie całkowitoliczbowe (//), obliczanie reszty z dzielenia (%) czy też potęgowanie (**).

Poza tymi znanymi operacjami, dla typu int zdefiniowane są operacje bitowe, działające na ich binarnej reprezentacji wewnątrz komputera. Więcej o systemie dwójkowym można przeczytać np. na Wikipedii:

http://http://pl.wikipedia.org/wiki/Dw%C3%B3jkowy_system_liczbowy

My natomiast skupimy się na tym, jakie operacje mamy do dyspozycji i jak one działają.

Pierwsze trzy: negacja bitowa (~), alternatywa (|) oraz koniunkcja (&) działają analogicznie do tych dla typu logicznego, z tym że operują na pojedynczych bitach. Negacja odwraca każdy bit na przeciwny. Weźmy np. liczbę 110001(2):
```
~110001 = 001110
```
Alternatywa bitowa daje na danym miejscu wynikowej liczby 1, jeśli przynajmniej jedna z dwóch liczb wejściowych ma na danym miejscu 1:
```
   101011110
|  001110001
-------------
   101111111
```
Koniunkcja bitowa natomiast wtedy, gdy w obu liczbach na danym miejscu występuje 1:
```
   101011110
&  001110001
-------------
   001010000
```
Dodatkowo Python, podobnie jak inne języki programowania, posiada operator ^ (xor) - tzw. alternatywy wykluczającej, którą w przypadku operowania na bitach wygodniej rozumieć jako dodawanie modulo 2:
```
   101011110
^  001110001
-------------
   100101111
```
Poza tym są jeszcze przesunięcia bitowe - w lewo (<<) i w prawo (>>) -  które również można rozumieć nieco inaczej. Mianowicie, odpowiadają one mnożeniu i dzieleniu danej liczby przez 2:
```python
>>> bin(13)
'0b1101'
>>> 13 << 3
104
>>> bin(104)
'0b1101000'
```
Jak widać na powyższym wycinku z powłoki Pythona, 13 << 3 oznacza przesunięcie bitowej reprezentacji liczby 13 o trzy miejsca w lewo z dostawieniem zer. Odpowiada to pomnożeniu przez 23, czyli 8.
float

Liczby zmiennoprzecinkowe różni od liczb całkowitych m.in. reprezentacja komputerowa (więcej tutaj: http://pl.wikipedia.org/wiki/Liczba_zmiennoprzecinkowa ). W Pythonie zmienne typu float posiadają zawsze część dziesiętną, zapisywaną po kropce (nie po przecinku, jak to zwykliśmy robić w szkole). Dostępne są dla nich te same działania, co dla typu int, poza operacjami bitowymi (nawet reszta z dzielenia!).
complex

Liczby zespolone posiadają część urojoną, oznaczaną w Pythonie przez przyrostek j. Poza operacjami dostępnymi dla opisanych wcześniej typów liczbowych (liczb zespolonych nie porządkujemy - nie można ich porównywać operatorami >, >=, <=, <), zmienne typu complex posiadają dodatkowe atrybuty i metody (gdyż, podobnie jak wszystko inne w Pythonie, są obiektami, do czego dojdziemy w dalszej części kursu). Np. każda zmienna typu complex posiada atrybuty real oraz imag zawierające jej część rzeczywistą i zespoloną, jak również można dla takiej zmiennej wywołać metodę conjugate(), która zwróci sprzężenie danej liczby. Biblioteka standardowa zawiera moduł (w Pythonie tak nazywa się pliki źródłowe) cmath, który zawiera funkcje zespolone takie jak cos() i sin() oraz funkcje liczące moduł danej liczby zespolonej czy też jej argument. Aby skorzystać z tych funkcji, należy zaimportować moduł cmath. Dostęp do zawartych w nim funkcji możemy uzyskać poprzedzając ich nazwę nazwą modułu i kropką. O tak:
```python
>>> import cmath
>>> cmath.cos(1+1j)
(0.8337300251311491-0.9888977057628651j)
>>> cmath.phase(2-0.5j)
-0.24497866312686414
```
Więcej o module cmath: https://docs.python.org/3.0/library/cmath.html


Zmienne typu str służą do przechowywania danych tekstowych, te natomiast możemy w Pythonie zapisać na wiele sposobów: w apostrofach, cudzysłowie i ich potrójnych odmianach:
```python
>>> 'to jest napis'
'to jest napis'
>>> "to również"
'to również'
>>> """Także i to - takie napisy
...
... możemy rozciągać
... na kilka
... linii... :)"""
'Także i to - takie napisy\n\nmożemy rozciągać\nna kilka\nlinii... :)'
````
Ta ostatnia wersja często jest wykorzystywana do tworzenia tzw. docstringów, o czym będzie mowa za kilka tygodni. Nie mamy do dyspozycji osobnego typu na pojedyncze znaki jak w wielu innych językach programowania. Znakiem (zwykle w innych jest to typ char) jest po prostu jednoznakowy napis. Przychodzi pewnie na myśl pytanie: "jak się dostać do pojedynczego znaku lub fragmentu?". Spieszę z odpowiedzią...

Dane typu str są sekwencjami (podobnie jak np. listy, krotki czy tablice bajtów, do czego dojdziemy) i, jak pozostałe, są indeksowane od zera, a do wybranych elementów możemy się dostać wykorzystując nawiasy kwadratowe:
```python
>>> a = 'abcdefghijk'
>>> a[1] # drugi element - indeksujemy od zera!
'b'
>>> a[3:6] # fragment od czwartego do szóstego elementu (bez znaku o indeksie 6!)
'def'
>>> a[1:6:2] # co drugi znak, od drugiego do siódmego
'bdf'
```
Ogólnie wygląda to tak: napis[poczatek, koniec, krok]. Polecam wybróbowanie różnych kombinacji w powłoce, np. z liczbami ujemnymi.

Dodatkowo (jak wszystko inne) napisy są obiektami, wobec czego mają metody, które można dla nich wywołać. Podam tu tylko dwa przykłady, po resztę odsyłam do dokumentacji i zadań. Metoda str.upper() zamienia małe litery na wielkie:
```python
>>> 'cognosce te ipsum'.upper()
'COGNOSCE TE IPSUM'
```
Natomiast metoda str.isnumeric() pozwala sprawdzić, czy napis składa się z samych cyfr (co może się przydać, np. gdy myślimy o rzutowaniu na liczbę):
```python
>>> '4013'.isnumeric()
True
```

Więcej o typach danych dostępnych w Pythonie można poczytać w dokumentacji:

https://docs.python.org/3/library/stdtypes.html

### Przykłady

Poniżej znajdują się pliki, w których na przykłaach pokazano działanie wyżej omówionych typów. Można je pobrać i uruchomić lokalnie, by sprawdzić ich działanie.

<<<<<<< HEAD
[zmienna typu int](https://gitlab.com/lhryniuk/python/tree/master/python-course/examples_zmienne/int.py)

[zmienna typu float](https://gitlab.com/lhryniuk/python/tree/master/python-course/examples_zmienne/float.py)

[zmienna typu str](https://gitlab.com/lhryniuk/python/tree/master/python-course/examples_zmienne/str.py)

[zmienna typu bool](https://gitlab.com/lhryniuk/python/tree/master/python-course/examples_zmienne/bool.py)

[zmienna typu complex](https://gitlab.com/lhryniuk/python/tree/master/python-course/examples_zmienne/complex.py)
=======
[zmienna typu int](https://github.com/kkingstoun/Kurs-Pythona/blob/main/lecture_notes/examples_zmienne/int.py)

[zmienna typu float](https://github.com/kkingstoun/Kurs-Pythona/blob/main/lecture_notes/examples_zmienne/float.py)

[zmienna typu str](https://github.com/kkingstoun/Kurs-Pythona/blob/main/lecture_notes/examples_zmienne/str.py)

[zmienna typu bool](https://github.com/kkingstoun/Kurs-Pythona/blob/main/lecture_notes/examples_zmienne/bool.py)

[zmienna typu complex](https://github.com/kkingstoun/Kurs-Pythona/blob/main/lecture_notes/examples_zmienne/complex.py)

## Zadania

* zadania podstawowe
  * [posortuj trzy liczby](https://github.com/kkingstoun/Kurs-Pythona/blob/main/exercises/zmienne/sort_three_numbers.py)
  * [ćwiartki płaszczyzny zespolonej](https://github.com/kkingstoun/Kurs-Pythona/blob/main/exercises/zmienne/complex_quadrants.py)

* zadania dodatkowe
  * [binarne sprawdzanie nieparzystości](https://github.com/kkingstoun/Kurs-Pythona/blob/main/exercises/zmienne/binary_odd_check.py)
>>>>>>> 9250fdf3a3810ae97dbf21caa8bbeeaa388ea13d
