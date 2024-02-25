## Listy

Lista jest pierwszym z kontenerów (typów mogących przechowywać zmienne), który
omówimy. Podobnie jak krotki, tablice bajtów, napisy i zakresy (range(), które widzieliśmy w
poprzednich częściach), listy są sekwencjami (wszystkie takie typy wspierają
pewien zestaw funkcjonalności). Listy wyróżnia to, że są modyfikowalne (napisy
jak wiemy nie są, krotki również) i uporządkowane, tzn. zachowują kolejność
przechowywanych elementów.

### Tworzenie list

Listę definiuje się w nawiasach kwadratowych, umieszczając w nich jej
zawartość, np.:
```python
pierwsze = [ 2, 3, 5, 7, 11, 13, 17, 19]
```
Powyższa lista składa się z liczb pierwszych mniejszych od 20.

Elementy listy nie muszą być tych samych typów:
```python
dane = [ 'drzewo', 2.99, [ True, True, False], 2 ]
```
...choć jest to pożądane, gdyż ułatwia ich przetwarzanie (np. trudno jest
posortować listę złożoną z napisów i liczb czy też dodać elementy takiej
listy).

### Indeksowanie

Tak samo jak w przypadku napisów, do elementów listy odwołujemy się nawiasami
kwadratowymi:
```python
>>> c = [4, 3, 6, 10, -2]
>>> c[1:3]
[3, 6]
>>> c[1:5:2]
[3, 10]
>>> c[4]
-2
```
Analogicznie też możemy sprawdzić czy dany element znajduje się w liście:
```python
>>> imiona = ['Staszek', 'Leszek', 'Maria', 'Daria']
>>> 'Staszek' in imiona
True
>>> 'Iwona' in imiona
False
```
Metoda `index()` pozwala dowiedzieć się, na którym miejscu się znajduje wybrany
element:
```python
>>> imiona.index('Maria')
2
```
W łatwy sposób możemy przewidzieć jak tworzyć listę list (np. dwuwymiarową
tablicę) i odwołać się do pojedynczego elementu:
```python
>>> c = [[4, 3, 6], [10, -2, 3]]
>>> c[0][0]
4
```
### Operacje na elementach

#### Dodawanie i modyfikacja
Elementy do listy możemy dodać na kilka sposobów. Pierwszy polega na użyciu
nawiasów kwadratowych. Analogicznie jak powyżej uzyskiwaliśmy dostęp do jednego
lub wielu elementów, możemy zmienić ich wartość:
```python
>>> a = [5, -1, 3, 2]
>>> a[1] = 3
>>> a
[5, 3, 3, 2]
```
W tym przypadku nadpisaliśmy nowym elementem stary. Drugim sposobem jest
dodawanie elementów na koniec listy metodami `append(x)` i `extend(x)`. Różnią
się one tym, że `append(x)` dodaje dany element na koniec listy,
a `extend(x)` jego "zawartość". Widać to dobrze w przypadku list:
```python
>>> p = [ 9, 3, -6]
>>> p.extend([1, 2])
>>> p
[9, 3, -6, 1, 2]
>>> p.append([1, 2])
>>> p
[9, 3, -6, 1, 2, [1, 2]]
```
Jak widzimy w drugim przypadku do listy została dołączona nowa lista.

Możemy też coś wstawić na konkretne miejsce w liście. Służy do tego metoda
`insert(i, x)` (wstawia x na miejsce o indeksie `i`).

#### Usuwanie elementów

Istnieje również kilka sposobów usuwania elementów z listy - instrukcja `del`
oraz metody `pop([i])` i `remove(x)`.

`Del` pozwala usuwać elementy w podanym zakresie, zgodnie z tym, co robiliśmy
dostając się do obiektów. Metoda `pop()` (z domyślnym argumentem, oznaczającym
indeks elementu, który chcemy wyciągnąć) zwraca wybrany element i usuwa go z
listy, natomiast `remove(x)` pozwala usunąć pierwsze wystąpnienie danego elementu x.
```python
>>> t = [6, 1, 9, 3, -10]
>>> del t[1:2]
>>> t
[6, 9, 3, -10]
>>> t.pop()
-10
>>> t
[6, 9, 3]
>>> t.remove(9)
>>> t
[6, 3]
```
### List comprehension

Z listami związana jest pewna konstrukcja - list comprehension - której nazwy
co prawda raczej się nie tłumaczy, ale na nasze potrzeby możemy
nazwać wyrażeniem listowym. Jest to sposób tworzenia list w oparciu o
sekwencje, z użyciem znanej nam pętli `for` i, opcjonalnie, instrukcji warunkowej.
Przypomina zapisem definicję zbioru. Pokażemy to na przykładzie. Załóżmy,
że mając listę `a = [9, -7, 2, 5, 1]`, chcemy uzyskać listę `b` złożoną z kwadratów
liczb znajdujących się w liście `a`. Możemy to zrobić następująco:
```python
b = [k ** 2 for k in a]
```
I tyle :-)! Jak to odczytać? Rozłóżmy to wyrażenie na części:
```python
b = # b to
[ ] # lista
k ** 2 # złożona z k ** 2
for k in a # dla każdego elementu k w liście a
```
Jak powiedzieliśmy wcześniej, w wyrażeniu listowym możemy użyć instrukcji
warunkowej. Załóżmy, że mając daną poprzednio listę a chcemy uzyskać listę `c`, w
której znajdować się będą sześciany wszystkich liczb dodatnich z `a`. To proste:
```python
c = [k ** 3 for k in a if k > 0]

c = # c to
[ ] # lista
k ** 3 # złożona z k ** 3
for k in a # dla każdego elementu k w liście a
if k > 0 # większego od zera
```
Więcej sposobów wykorzystania tych konstrukcji znajdziecie w załączonych
przykładach.

Z listami można zrobić jeszcze więcej, np. sortować czy odwracać kolejność
elementów (`reversed(lista)`). Gdy dojdziemy do elementów programowania funkcyjnego, poznamy bardzo
przydatne funkcje `map`, `filter` i `reduce`. Na razie zachęcamy do własnych
poszukiwań, choćby w dokumentacji:
https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range

## Krotki

Krotki (ang. tuple) to kolejny rodzaj sekwencji, jak napisy czy listy.
Od tych pierwszych różnią się tym, że mogą przechowywać elementy różnych typów
(napisy to ciągi znaków/bajtów), a od list tym, że nie można modyfikować ich
zawartości:
```python
a = (1, 3, 2)
>>> a[2] = 1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
```
### Tworzenie krotek

Możemy je zdefiniować albo za pomocą nawiasów okrągłych:
```python
() # pusta krotka
(1,) # krotka jednoelementowa - (1) nie tworzy krotki a liczbę typu int
('dad', 'mom', 'plum') # krotka trzyelementowa
```
albo skonstruować z obiektów iterowalnych (napisów, list, krotek, przedziałów,
itd.) jawnie wywołując konstruktor:
```python
tuple([1, 2, 3]) # (1, 2, 3)
tuple(range(4, 8, 2)) # (4, 6)
tuple('halllo') # ('h', 'a', 'l', 'l', 'l', 'o')
```
### Indeksowanie i inne operacje

Krotki wpierają wszystkie operacje spośród tych, które można wykonać na listach
i które nie zmieniają ich elementów. Kilka przykładów (nowością są tu operatory
`+` i `*`, które odpowiednio łączą dwie krotki - nie zmienia to zawartości,
tworzony jest nowy obiekt - i powielają zawartość danej krotki):
```python
>>> a = (4, 1, 6, -3)
>>> 4 in a
True
>>> a[2:]
(6, -3)
>>> len(a)
4
>>> a * 3
(4, 1, 6, -3, 4, 1, 6, -3, 4, 1, 6, -3)
>>> a.index(-3)
3
>>> (1, 3) + (2, 4)
(1, 3, 2, 4)
>>> min(a)
-3
```
A więc to, co już znamy. Dzięki temu, że są nie modyfikowalne (w szczególności
nie można dodawać ani usuwać ich elementów), krotki mogą być wykorzystywane
jako klucze w słownikach (o nich wkrótce) i są nieco szybsze od list, jednak
nie to powinno być argumentem za czy przeciw używaniu jednego czy drugiego
rozwiązania.

Więcej o krotkach i tym, co je wyróżnia:

https://docs.python.org/3/library/stdtypes.html#tuple

https://docs.python.org/3.4/tutorial/datastructures.html#tuples-and-sequences

http://news.e-scribe.com/397

https://www.asmeurer.com/blog/posts/tuples/

## Przykłady

[listy](https://gitlab.com/lhryniuk/python/blob/course/python-course/lecture_notes/examples_listy_i_krotki/listy.py)

## Zadania

* zadania podstawowe
  * [xor napisów](https://gitlab.com/lhryniuk/python/blob/course/python-course/exercises/listy_i_krotki/xor_napisow.py)
  * [podzielne](https://gitlab.com/lhryniuk/python/blob/course/python-course/exercises/listy_i_krotki/podzielne.py)


* zadania dodatkowe
  * [pola i obwody](https://gitlab.com/lhryniuk/python/blob/course/python-course/exercises/listy_i_krotki/pola_obwody.py)
  * [mnożenie macierzy](https://gitlab.com/lhryniuk/python/blob/course/python-course/exercises/listy_i_krotki/mnozenie_macierzy.py)
