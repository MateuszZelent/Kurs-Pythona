## Funkcje

Funkcja to wydzielony fragment kodu - można powiedzieć podprogram - opatrzony odpowiednim identyfikatorem. Jej
zdefiniowanie pozwala uniknąć powtarzania kodu i podzielić go na części, by
m.in. ułatwić jego zrozumienie. To swoista czarna skrzynka, która przetwarza
konkretne dane (nazywane parametrami) i zwraca (za pomocą słowa kluczowego `return`)
określony wynik. W Pythonie do tworzenia funkcji używamy słowa `def`.

Przykładowo, możemy zdefiniować funkcję o nazwie `f_in()` (od float_input),
która wczytuje i zwraca liczbę typu `float`:
```python
def f_in():
    return float(input('Podaj liczbę rzeczywistą: '))
```
Python charakteryzuje się tym, że za podział kodu na części odpowiadają
wcięcia, a nie np. klamry, jak to jest w niektórych językach. Z jednej strony
może to być nieco uciążliwe, z drugiej jednak wymaga stosowania spójnego stylu
w całym programie, co wpływa pozytywnie na wygląd kodu i łatwość jego
zrozumienia. Jak widać powyżej, ciało funkcji (bo tak nazywa się zawarty w niej
kod) musi być wcięte względem linijki, w której określamy jej nazwę i
parametry. Można stosować różne wcięcia, jednak zalecane są cztery spacje, co
stosuję w swoim kursie. Więcej o stylu pisania tutaj:
http://legacy.python.org/dev/peps/pep-0008/

Dzięki zdefiniowaniu funkcji `f_in()` zamiast pisać:
```python
a = float(input('Podaj liczbę rzeczywistą: '))
b = float(input('Podaj liczbę rzeczywistą: '))
c = float(input('Podaj liczbę rzeczywistą: '))
print ("Podałeś liczby: " + str(a) + " " + str(b) + " " + str(c))
```
wystarczy:
```python
a = f_in()
b = f_in()
c = f_in()
print ("Podałeś liczby: " + str(a) + " " + str(b) + " " + str(c))
```
Mówiliśmy wcześniej o danych przekazywanych do funkcji. Podawane są one przy
definicji, w nawiasach okrągłych, zaraz po jej nazwie. Napiszmy funkcję, która
sprawdza, czy dana liczba jest parzysta. Będzie ona miała jeden parametr, `a` i
zwracać będzie `True` lub `False` w zależności od parzystości podanej liczby:
```python
def is_even(a):
    return (a % 2 == 0)
```
Warto zwrócić uwagę na to, że nie musimy zapisywać wyniku tego porównania i tak
kod wygląda dużo lepiej stylistycznie. Nie potrzebujemy dodatkowej zmiennej, bo
i tak tylko byśmy zwrócili jej wartość.

Funkcję wywołujemy podając jej nazwę, o tak:
```python
is_even(5)
is_even(143292)
```
### Argumenty domyślne

Zdarza się, że pewne argumenty w większość wywołań funkcji są takie same lub
chcemy mieć możliwość wywoływania funkcji ze zmienną liczbą parametrów. Są trzy
metody definiowania takich funkcji. Na razie omówimy jedną z nich - argumenty
domyślne, a dwie następne poznamy, gdy dowiemy się, co to listy, krotki i słowniki
oraz jak ich używać.

Zatem, załóżmy, że chcemy mieć funkcję, która pobierze dane jakiejś
osoby i zwróci je w formie ładnie sformatowanego łańcucha znaków. Niech
przyjmuje ona imię, nazwisko i datę urodzenia (wszystko jako napisy), a zwraca trzy linijki tekstu, wyjustowane
do prawej (powiedzmy na szerokość 40 znaków). Nie zawsze jednak będziemy mogli
uzyskać nazwisko czy datę urodzenia, musimy zatem tak zaprojektować naszą funkcję, by
radziła sobie bez tych danych. Opisana funkcja może wyglądać tak:
```python
def formatuj_dane(imie, nazwisko='', data_urodzenia=''):
    return (imie.rjust(40) + '\n'
          + nazwisko.rjust(40) + '\n'
          + data_urodzenia.rjust(40) + '\n')
```
Jak widać, wartości domyślne naszych parametrów podajemy po znaku `=`. Ważne jest
to, że jeśli zrobimy tak dla jednego z parametrów, to wszystkie za nim też
muszą mieć wartości domyślne. Więcej swobody mamy w wywoływaniu funkcji. Możemy
pominać nazwisko lub datę urodzenia. Jeśli nie chcemy pominąć wartości
środkowego argumentu, musimy podać nazwy następnych. Najlepszy będzie przykład.
Powyższą funkcję możemy wywoływać na wszystkie poniższe sposoby:
```python
print(formatuj_dane('Adam', 'Smith', '05.06.1903'))
print(formatuj_dane('Ada', data_urodzenia='28.05.1943'))
print(formatuj_dane('Katarzyna', 'Nowak'))
print(formatuj_dane('Katarzyna', nazwisko='Nowak')) # to samo co wyżej
```
### Słówko o słówku pass

pass nie robi nic (albo może robi nic ;-) ). Możemy go użyć, gdy składnia języka wymaga
jakiegoś wyrażenia, a nasz program nie ma w tym miejscu nic do zrobienia lub
w przypadku, gdy piszemy jakiś fragment kodu i nie mamy jeszcze pomysłu, co
powinno znajdować się w danym miejscu, np. określamy tylko nazwy funkcji, by
ujrzeć strukturę tworzonego programu:
```python
def fun(a, b, c):
    pass
```
Od teraz zadania będa polegały na napisaniu jakiejś funkcji (lub, później,
klasy), która będzi wykonywała określone zadanie. Najczęściej funkcja będzie
już stworzona i będzie zawierała jedynie słówko pass, które będzie trzeba
zamienić na własny kod. Powodzenia :-)!

## Zadania

* zadania podstawowe
  * [Symbol Newtona](https://github.com/kkingstoun/Kurs-Pythona/blob/main/exercises/funkcje/symbol_newtona.py)


* zadania dodatkowe
  * [rok przestępny](https://github.com/kkingstoun/Kurs-Pythona/blob/main/exercises/funkcje/rok_przestepny.py)
  * [cukierki](https://github.com/kkingstoun/Kurs-Pythona/blob/main/exercises/funkcje/cukierki.py)
  * [sprawdź dzień](https://github.com/kkingstoun/Kurs-Pythona/blob/main/exercises/funkcje/sprawdz_dzien.py)
