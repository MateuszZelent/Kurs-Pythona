## Słowniki

#### Wprowadzenie

W przypadku list i krotek nasze możliwości są ograniczone m.in. przez konieczność
indeksowania liczbami naturalnymi. Załóżmy, że chcielibyśmy przechowywać
tłumaczenia słów z polskiego na angielski. Aby móc łatwo dodawać nowe słowa,
wykorzystując naszą dotychczasową wiedzę, zapisalibyśmy to w liście, np.:
```python
pol_ang = [ ('pies', 'dog'), ('kot', 'cat'), ('adres', 'address')]
```
Jak jednak znaleźć teraz tłumaczenie słowa 'kot'? Musimy przejść po całej
liście i sprawdzać pierwszy element każdej krotki:
```python
for para in pol_ang:
    if para[0] == 'kot':
        print(para[1])
```
Tymczasem, wykorzystując typ zwany słownikiem, możemy to zrobić w nieco
przyjemniejszy sposób:
```python
slownik_pol_ang = { 'pies': 'dog',
                    'kot': 'cat',
                    'adres': 'address'}
# tłumaczenie słowa kot
print(slownik_pol_ang['kot'])
```
...i znacznie szybszy. Jak widzimy, słowniki można indeksować napisami. Ale nie
tylko, o czym za chwilę. Najpierw, jak robiliśmy w przypadku poprzednio
omawianych typów, powiedzmy trochę o ich inicjalizacji.

### Tworzenie słowników

Słowniki definiuje się podobnie do list czy krotek, korzystając z nawiasów
klamrowych:
```python
pusty_slownik = { }
```
Pary klucz-wartość podajemy w nawiasach, oddzielając pierwsze od drugiego
dwukropkiem, jak widzieliśmy wyżej.

Możemy też stworzyć słownik z listy krotek lub podając pary klucz=wartość w
konstruktorze:

stwórzmy słownik z listy z pierwszego przykładu
```python
>>> pol_ang = [ ('pies', 'dog'), ('kot', 'cat'), ('adres', 'address')]
>>> a = dict(pol_ang)
>>> print (a)
{'pies': 'dog', 'adres': 'address', 'kot': 'cat'}
```
Jak widzimy, zmieniła się kolejność elementów - w przypadku słowników nie jest
ona określona, nie można więc zapytać, np. jaki jest trzeci element słownika.
Odwołujemy się do nich jedynie przez użycie klucza.

### Dostęp do elementów

Do pojedynczego elementu słownika możemy się dostać zasadniczo na dwa sposoby:
podając klucz w nawiasach kwadratowych oraz korzystając z metody `get()`.
```python
>>> a['pies']
'dog'
>>> a.get('pies')
'dog'
```
Jak widać, różnicy w tym przypadku nie widać. Jednak zauważymy ją, gdy
spróbujemy dostać się do elementu, którego w słowniku nie ma:
```python
>>> a.get('ciasto')
>>>
>>> a['ciasto']
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
KeyError: 'ciasto'
```
Metoda `get()` zwraca wartość `None` i nic poza tym, natomiast korzystając z
nawiasów kwadratowych dostaniemy wyjątek `KeyError`.

Słowniki udostępniają kilka metod, które ułatwiają przechodzenie po wszystkich
ich elementach:
```python
# klucze, czyli polskie słowa
for slowo in slownik_pol_ang.keys():
    print(slowo)

# wartości, czyli słowa angielskie
for word in slownik_pol_ang.values():
    print(word)

# wszystkie elementy
for slowo, word in slownik_pol_ang.items():
    print(slowo + ' to po angielsku ' + word)
```
### Modyfikacja

Elementy możemy modyfikować analogicznie jak w przypadku list, podając klucz w nawiasach
kwadratowych. W ten sam sposób możemy też dodawać nowe elementy:
```python
>>> a['wilk'] = 'wlf'
>>> a['wilk']
'wlf'
>>> a['wilk'] = 'wolf'
>>> a['wilk']
'wolf'
```
Inną możliwością jest użycie metody `update()`:
```python
>>> b = {}
>>> b.update(ania=3, ola=5, bolek=10) # dodajemy trzy pary do słownika
>>> b
{'ania': 3, 'ola': 5, 'bolek': 10}
>>> b.update(ania=10) # zmieniamy wartość pod kluczem 'ania'
>>> b
{'ania': 10, 'ola': 5, 'bolek': 10}
```
Usuwać elementy ze słownika możemy też na kilka sposobów: instrukcją `del` oraz
metodami `pop()`, `popitem()` i `clear()`. Pokażmy na przykładzie działanie dwóch
pierwszych - jest podobne. Metoda `pop()` tak jak `del` usuwa wskazany element, ale
dodatkowo zwraca jego wartość. Mając zdefiniowany słownik z przykładu wyżej:
```python
>>> b.pop('kasia', 0) # jako drugi argument podajemy domyślną wartość
0                     # zwracaną w przypadku braku wskazanego elementu
>>> b.pop('ola') # usuwamy element pod kluczem 'ola'
5                # zwracana jest jego wartość
>>> b
{'ania': 10, 'bolek': 10}
>>> del b['bolek'] # usuwamy element pod kluczem 'bolek', bez zwracania wartości
>>> b
{'ania': 10}
```
Więcej o słownikach i dostępnych metodach znaleźć można tu i tam:

https://docs.python.org/3/library/stdtypes.html?highlight=dict#dict

https://docs.python.org/3/tutorial/datastructures.html#dictionaries

## Zbiory
Ostatnimi kontenerami jakie poznamy, będą zbiory. Są one odpowiednikiem zbiorów
znanych nam z matematyki. W Pythonie występują dwa rodzaje:
 * set - modyfikowalny
 * frozenset - niemodyfikowalny (dzięki czemu może być użyty jako klucz w
   słowniku)

Mając doświadczenie z poprzednich lekcji, łatwo możemy domyślić się tego jak tworzymy
zbiory - możemy użyć konstruktora, któremu podamy iterowalny obiekt (m.in. krotkę,
listę, zasięg - range(), napis) lub odpowiednich nawiasów (tylko w przypadku
modyfikowalnego zbioru):
```python
>>> set('skakanka')
{'s', 'n', 'a', 'k'}
>>> frozenset([i for i in range(1, 10) if i % 2 == 0])
frozenset({8, 2, 4, 6})
>>> {1, 2, 3}
{1, 2, 3}
```
Jak widzimy wyżej i jak można było się spodziewać po przywołaniu zbiorów
matematycznych, set i frozenset nie zawierają duplikatów (więc możemy je
wykorzystać do ich usuwania).

### Dodawanie i usuwanie elementów z obiektów typu set

Metody służące do tego nazywają się tak jak te znane nam z list, mianowicie:
`add(a)`, `remove(a)`, `discard(a)`, `pop()`, `clear()`.

Wypadałoby tu tylko zwrócić uwagę na różnicę między trzema środkowymi.
Wszystkie usuwają pojedynczy element, ale:
- `remove(a)` i `discard(a)` usuwają element podany jako argument i jeśli go nie ma w
  zbiorze, `remove` wyrzuca wyjątek, natomiast `discard(a)` to przemilcza,
- `pop()` usuwa losowy element i zwraca go jako wynik

Przykład:
```python
>>> set([2, 4, 6, 8, 10, 12])
{2, 4, 6, 8, 10, 12}
>>> zbior = set([2, 4, 6, 8, 10, 12])
>>> zbior.remove(3)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
KeyError: 3
>>> zbior.discard(3)
>>> zbior.discard(4)
>>> zbior
{2, 6, 8, 10, 12}
>>> zbior.pop()
2
>>> zbior.add(3)
>>> zbior
{3, 6, 8, 10, 12}
```
Oczywiście istnienie danego elementu w zbiorze możemy sprawdzić za pomocą `in`,
do czego już powinniśmy się przyzwyczaić.

### Operacje na zbiorach

Python wspiera wszystkie znane nam z matematyki operacje na zbiorach, a ich
nazwy są wprost zaczerpnięte z angielskiego: `isdisjoint(other)`,
`issubset(other)`, `issuperset(other)`, `union(other)`, `intersection(other)`,
`difference(other)`, `symmetric_difference(other)`, oznaczane z pomocą symboli,
kolejno (od issubset): `<=`, `>=`, `|`, `&`, `-`, `^`.

I to właściwie wszystko :). Zakończmy lekcję krótkim przykładem:
```python
>>> a = {3, 1, 4, 10, 6, 7}
>>> b = {2, 5, 0, 1, 4, 3}
>>> a >= b
False
>>> a | b
{0, 1, 2, 3, 4, 5, 6, 7, 10}
>>> a.intersection(b)
{1, 3, 4}
>>> a - b
{10, 6, 7}
>>> a.symmetric_difference(b)
{0, 2, 5, 6, 7, 10}
```
Dokładniejsze omówienie:
https://docs.python.org/3.4/library/stdtypes.html?highlight=set#set

## Zadania

* zadania podstawowe
  * [xor słowników](https://gitlab.com/lhryniuk/python/blob/course/python-course/exercises/zbiory_i_slowniki/xor_slownikow.py)
  * [usuwanie ogonków](https://gitlab.com/lhryniuk/python/blob/course/python-course/exercises/zbiory_i_slowniki/usuwanie_ogonkow.py)


* zadania dodatkowe
  * [operacje na zbiorach](https://gitlab.com/lhryniuk/python/blob/course/python-course/exercises/zbiory_i_slowniki/operacje_na_zbiorach.py)
