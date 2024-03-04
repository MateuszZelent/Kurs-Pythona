## Instrukcje sterujące

### Instrukcja warunkowa if

Czasami chcielibyśmy, by nasz program reagował na różne sposoby w zależności od
otrzymanych danych, np. wpisanej przez użytkownika liczby bądź informacji o
systemie operacyjnym. Do tego celu używamy instrukcji `if`:
```
if warunek:
    # instrukcje
    # ...
else:
    # w przeciwnym wypadku:
    # ...
```
Przykładowo:
```python
a = int(input('Podaj liczbę całkowitą z zakresu 1-10\n'))
if a % 3 == 0:
    print('Podałeś liczbę podzielną przez 3')
else:
    print(str(a) + ' nie dzieli się przez 3')
```
Zdarza się, że warunków do sprawdzenia jest więcej -w takimprzypadku korzystamy
z instrukcji `elif` (skrót od else if):
```python
a = int(input('Podaj liczbę naturalną do sprawdzenia: '))
if jest_pierwsza(a):
    print(str(a) + ' jest liczbą pierwszą')
elif a < 2:
    print(str(a) + ' nie jest ani liczbą pierwszą, ani liczbą złożoną')
else:
    print(str(a) + ' jest liczbą złożoną')
```
Z instrukcją `if` związana jest pewna konstrukcja, znana niektórym z języka C++
(operator trójargumentowy ?:). Mianowicie, możliwe jest zapisanie instrukcji
warunkowej, która zwróci wynik (np. żebyśmy mogli przypisać go do zmiennej):
```python
a = 5
# zmienna b będzie miała wartość 'Nieparzysta'
b = 'Parzysta' if a % 2 == 0 else 'Nieparzysta'
```
Na razie to tyle. Wrócimy do instrukcji `if` przy omawianiu list (pojawią się
tam tzw. 'list comprehension').

### Pętle

Python, tak jak inne języki udostępnia konstrukcje służące do powtarzania
pewnych operacji - pętle. Pierwszą jaką omówimy jest pętla `while`. Działa ona
dopóki podany warunek jest prawdziwy. Jako przykład, napiszmy przy użyciu tej
pętli funkcję, która wylicza silnię liczby n:
```python
def fact(n):
    f = 1
    # wyjdziemy z petli, gdy n bedzie mniejsze badz rowne 1
    while n > 1:
        f *= n
        # n -= 1 to to samo co n = n - 1
        n -= 1
    return f
```
Drugą jest pętla `for`, nieco bardziej skomplikowana, ale jednocześnie
bardziej elastyczna. Pozwala na przetwarzanie jeden po drugim elementów
wybranego zbioru, np. kilku liczb czy elementów listy.
Składnię pokażemy na przykładzie. Założmy, że chcemy wpisać kwadraty kolejnych
liczb naturalnych, od 1 do 10. Z aktualną wiedzą, nasze rozwiązanie mogłoby
wyglądać tak:
```python
print(1 ** 2)
print(2 ** 2)
print(3 ** 2)
# ...
print(10 ** 2)
```
W przypadku dziesięciu liczb to nie jest problemem. Jednak jeśli chcielibyśmy
wypisać ich, powiedzmy, pięćdziesiąt, stałoby się to uciążliwe i nasz kod
rozrósłby się do sporych rozmiarów. Dużo łatwiej uzyskać to przy użyciu pętli:
```python
for i in range(1, 11):
    print(i ** 2)
```
Pętla `for` pozwala również przechodzić po elementach kontenerów i napisów:
```python
>>> napis = 'ala'
>>> for znak in napis:
...     print(znak)
...
a
l
a
```
W przypadku obu pętli mamy do dyspozycji jeszcze dwie instrukcje: `break` i
`continue`. Pierwsza z nich pozwala wyjść z pętli w dowolnym momencie, natomiast
druga przerywa wykonanie aktualnej iteracji i przechodzi do następnego elementu
danego zbioru.

Poniższa pętla z dwiema instrukcjami `if` w podanej postaci wypisze 0, 1, 2,
następnie pominie 3 (continue) i zakończy wypisywanie przy 5 (nie wypisując
tej liczby):
```python
for i in range(7):
    if i == 3:
        continue
    if i == 5:
        break
    print(i)
```
Nowością dla osób, które wcześniej programowały w innym języku może być fakt,
że pętle również mogą posiadać klauzulę else. Kod w niej zawarty jest
wykonywany po pętli (w przypadku, gdy nie wyjdziemy z niej wcześniej, np.
używając instrukcji `break`):
```python
for i in range(3):
    print(i)
else:
    print('Wszystko wypisane!')
```
To na razie wszystko, co powinniśmy wiedzieć o pętlach i instrukcji warunkowej.
Wrócimy do tego tematu jeszcze przy okazji omawiania kontenerów, tj. list,
krotek i słowników. Chcących dowiedzieć się więcej, odsyłamy do dokumentacji. A
osoby, dla których coś jest nie jasne mogą zadać pytanie poprzez sekcję `issues`,
lub drogą mailową :-).

### Zadania

* zadania podstawowe
  * [Weryfikacja adresu email](https://github.com/kkingstoun/Kurs-Pythona/blob/main/exercises/instrukcje_sterujace/weryfikacja_adresu_email.py)
  * [Problem Collatza](https://github.com/kkingstoun/Kurs-Pythona/blob/main/exercises/instrukcje_sterujace/problem_collatza.py)


* zadania dodatkowe
  * [odległość napisów](https://github.com/kkingstoun/Kurs-Pythona/blob/main/exercises/instrukcje_sterujace/odleglosc_napisow.py)
  * [pochodna arytmetyczna](https://github.com/kkingstoun/Kurs-Pythona/blob/main/exercises/instrukcje_sterujace/pochodna_arytmetyczna.py)
  * [zlicz samogłoski](https://github.com/kkingstoun/Kurs-Pythona/blob/main/exercises/instrukcje_sterujace/zlicz_samogloski.py)
