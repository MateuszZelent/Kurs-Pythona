## Operacje na plikach

### Dostęp do plików

Operacje na plikach wykonujemy przez obiekty klasy `file`. Aby utworzyć obiekt
tej klasy, skojarzony z danym plikiem, korzystamy z wbudowanej funkcji open():
```python
open(nazwa_pliku, tryb)
```
gdzie jako tryb (czyli sposób, w który będziemy korzystać z pliku) możemy podać:

* r - read, czytanie z pliku (domyślny)
* w - write, zapisywanie do pliku
* a - append, dopisywanie do końca pliku
* r+ - czytanie i zapisywanie

Dodatkowo do każdego z podanych wyżej trybów możemy dodać literę (przełącznik)
'b', co sprawi, że plik zostanie otwarty w trybie binarnym - dla plików nie
zawierających tekstu.

Dla przykładu załóżmy, że mamy plik o nazwie `example.txt`, o następującej
treści:
```
1 43
2 84
3 66
4 103
```
otwórzmy go w trybie do zapisywania i czytania:
```python
>>> ex = open('example.txt', 'r+')
```
### Czytanie z pliku

Do odczytania zawartości pliku służy metoda read():
```python
>>> ex.read()
'1 43\n2 84\n3 66\n4 103\n'
>>> ex.read()
''
````
Jak widzimy, druga próba odczytania zawartości pliku dała jedynie pusty napis.
Spowodowanie jest to tym, że plik jest postrzegany przez program jako sekwencja
bajtów i obiekt `ex` pamięta pozycję w tym pliku, z której powinien czytać dalsze
dane lub zapisywać nowe. Po pierwszym wykonaniu metody `read()` docieramy do
końca pliku `example.txt`, przez co następne jej wywołanie, `read()` zwraca pusty
napis. Możemy określić, ile bajtów chcemy odczytać, przekazując ich liczbę do
metody `read()`:
```python
>>> ex.seek(0)
0
>>> ex.read(4)
'1 43'
```

### Przeszukiwanie

W jaki sposób zatem wrócić do tego, co już odczytaliśmy? Czy trzeba raz jeszcze
otwierać dany plik i ponownie użyć metody `read()`? Nie! Klasa `file` pozwala na
przeszukiwanie pliku, tzn. ustalanie pozycji (czyli numeru bajtu), z/do której
ma odczytywać/zapisywać dane. Służy do tego metoda `seek()`:
```python
>>> ex.seek(6)
6
>>> ex.read()
' 84\n3 66\n4 103\n'
```
Jako argument przyjmuje ona przesunięcie (offset) względem początku pliku. W
naszym przykładzie 6 oznacza, że plik zostanie odczytany od pozycji za szóstym
bajtem, czyli od siódmego. Dodajmy tylko, że kolejne bajty to:
'1', ' ', '4', '3', '\n' (znak nowej linii), '2', ' ', '8', ...

`ex.seek(0)` spowoduje przejście do początku. Być może zastanawiasz się
teraz jak sprawdzić, w którym miejscu danego pliku jesteśmy po odczytaniu
iluś danych. Można to sprawdzić równie łatwo, służy do tego metoda `tell()`:
```python
>>> ex.tell() # po poprzednim wykonaniu read() jesteśmy na końcu pliku
21
>>> ex.seek(4)
4
>>> ex.tell()
4
```
Możemy odczytywać plik również linia po linii i istnieją przynajmniej dwa
sposoby, jak to zrobić:

* metoda readline():
```python
>> ex.seek(0)
0
>>> ex.readline()
'1 43\n'
>>> ex.readline()
'2 84\n'
```
* pętla for (analogicznie jak to robiliśmy w przypadku list, krotek czy
  słowników):
```python
>>> ex.seek(0)
0
>>> for i in ex:
...     print(i)
...
```
```
1 43
2 84
3 66
4 103
```
Po zrobieniu z plikiem tego, co chcieliśmy, należy wywołać metodę close(),
która go zamknie i zwróci zajęte zasoby systemowi:
```python
>>> ex.close()
```

### Zapisywanie do pliku

Jak powiedzieliśmy na początku, przy otwieraniu pliku możemy podać tryb
pozwalający na zapisywanie do niego:
```python
>>> ex2 = open('example2.txt', 'w')
```
Do zapisywania danych służy metoda `write()`:
```python
>>> ex2.write('There is nothing a Code can\'t do.\n')
34
>>> ex2.close()
```
Zwraca ona liczbę zapisanych w pliku bajtów (czyli długość podanego napisu w
tym przypadku).


### Konstrukcja z with

Słowo kluczowe `with` pozwala w nieco wygodniejszy (i bezpieczniejszy - zapewnia
zamknięcie pliku przy wyrzuceniu wyjątku - przez co jest zalecany) sposób
obsługiwać pliki. Składnia wygląda następująco:
```python
>>> with open('example2.txt') as ex2:
...     ex2.read()
...     # ...
...
"There is nothing a Code can't do.\n"
>>>
```

### Specjalne formaty

Biblioteka standardowa Pythona zawiera moduły pozwalające na obsługę plików
formatowanych w konkretny sposób, np. JSON (JavaScript Object Notation), csv
(comma separated values), bz2 (kompresja) czy XML. Ich omówienie znacznie
wykracza poza ramy podstawowego kursu, więc osoby zainteresowane odsyłam do
zewnętrznych źródeł.

JSON
https://docs.python.org/3.4/library/json.html#module-json

bz2
https://docs.python.org/3.4/library/bz2.html#module-bz2

XML
https://docs.python.org/3.4/library/xml.html

pickle (przechowywanie pythonowych obiektów)
https://docs.python.org/3.4/library/pickle.html#module-pickle
