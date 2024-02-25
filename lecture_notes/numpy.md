## Czym jest Numpy?
NumPy jest biblioteką Pythona służącą do obliczeń naukowych. Jako biblioteka NumPy dostarcza matematyczne funkcje użytecze w takich zagadnieniach jak:

* algebra linionwa,
* transformacje Fouriera,
* generowanie liczb losowych,
* oraz wszystkie potrzebne do operowania na tablicach i macierzach, które to są podstawowymi obiektami w Numpy.


### Importowanie biblioteki do środowiska pracy
Przed przystąpieniem do właściwej pracy należy zaimportować NumPy. Można to zrobić na wiele sposobów. Na użytek tego skryptu zaprezentujemy dwie możliwości: Po pierwsze:

```python
>>> from numpy import *
```

Po drugie:

```python
>>> import numpy as np
```

Są różnice między jednym a drugim sposobem importowania. W pierwszym przypadku funkcje NumPy są dostępne bezpośrednio. W drugim są one wywoływane z przedrostkiem `np`. Przeanalizujmy to na przykładzie.
Importując bibliotekę NumPy, `pi` będzie już posiadało zawsze wartość liczbową. Jeśli zaimportujesz ją w pierwszy sposób, wywołasz ją wpisując po prostu:

```python
>>> pi

pi
```
jeśli zaimportujesz bibliotekę Numpy w drugi podany sposób, do `pi` odwołasz się przez:

```python
>>> np.pi

3.1415926535897931
```
Podobnie z wszystkimi innymi funkcjami dostępnymi z poziomu tej biblioteki.

**Uwaga**: Oczywiście importujemy bibliotekę tylko raz jednym z wybranych sposobów na początku dokumentu! W dalszej części przyjmijmy, że importujemy bibliotekę NumPy przy użyciu drugiego sposobu.

### Operacje na tablicach (arrays)



#### 2.1 Tworzenie tablic
Aby stworzyć prostą jednowymiarową tablicę używamy funkcji "array" :
```python
>>> a = np.array( [1,2,3] )
print(a)
```

podobnie dwuwymiarową:

```python
>>> b = np.array([[1,2,3] , [4,5,6]] )
print(b)
```

a przez analogie dowolnie wielowymiarową:

```python
>>> c = np.array( [ [ [1,1,1],[1,1,1] ], [ [2,2,2],[2,2,2] ] ] )
print(c)

[[[1 1 1]
  [1 1 1]]

 [[2 2 2]
  [2 2 2]]]
```

`c` jest tablicą trójwymiarową.

Przy tworzeniu tablicy istnieje możliwość zadeklarowania jej typu:

```python
>>> e = np.array( [ [1,0], [0,1] ], dtype=complex )
print(e0

[[ 1.+0.j  0.+0.j]
 [ 0.+0.j  1.+0.j]]
 ```

W ten sposób utworzona tablica będzie zawierała liczby zespolone.

W praktyce rzadko wpisujemy do tablicy element po elemencie. Aby zautomatyzować ten proces możemy odwołać się na przykład do takich poleceń:

```python
>>> f = np.arange(10)
 ```

utworzy to jednowymiarową tablicę zawierającą liczby 10 elementów, liczby od 0 do 9.

```python
>>> print(f)

[0 1 2 3 4 5 6 7 8 9]
```

W ogólności, możemy utworzyć tablicę używając argumentu początkowego, końcowego i kroku zgodnie z formułą:

```python
>>> np.arange(start, stop, krok)
```

Na przykład:

```python
>>> tablica1 = np.arange(1, 11, 1)
>>> tablica2 = np.arange(1.,11.,1.)
```

**Uwaga**: Zapewne zauważasz różnice w deklaracji tablic: tablica1 i tablica2. Czy jednak wiesz w czym się to objawia?

Sprawdźmy to:

```python
>>>print (tablica1.dtype)

dtype('int64')

>>> print(tablica2.dtype)

dtype('float64')
```

Jaki stąd wniosek?

W tablicy w naturalny sposób możemy implementować elementy  zmiennoprzecinkowe. Daje to konkretne zalety, ale ma również swoje wady! Przy wielu zagadnieniach będzie konieczność używania liczb zmiennoprzecinkowych, należy jednak pamiętać o ograniczeniach nałożonych na ten typ zapisu.

W szczególności, jeśli zadeklarujemy "krok" w postaci zmiennoprzecinkowej, przy dużych tablicach, możemy nie być pewni wartości ostatnich elementów tablicy.

Aby poradzić sobie z powyższą uwagą, możemy odwołać się do funkcji "linspace". Przyjmuje ona jako argumenty wartość początkową, końcową i ilość elementów pomiędzy nimi.

```python
>>> np.linspace(0., 10., 3.)

>>> array([  0.,   5.,  10.])
```

### Zadanie:

czas: 1 min.

Przy użyciu powyższych funkcji oblicz wartość `sin(x)` dla kolejnych 100 punktów pomiędzy (0,2Π).

#### 2.2 Tworzenie "typowych" tablic
Biblioteka Numpy oferuje wiele możliwości. Łatwo przy jej użyciu tworzyć najczęściej używane tablice.

```python
>>> tablica3 = np.ones((3,3)) # Utworzy dwuwymiarową  tablice (3x3) wypełniona jedynkami.
>>> print(tablica3)

[[ 1.  1.  1.]
 [ 1.  1.  1.]
 [ 1.  1.  1.]]

>>> tablica4 = np.zeros((3,3,3)) # Utworzy trójwymiarową tablicę wypełnioną zerami.
>>> print(tablica4)

[[[ 0.  0.  0.]
  [ 0.  0.  0.]
  [ 0.  0.  0.]]

 [[ 0.  0.  0.]
  [ 0.  0.  0.]
  [ 0.  0.  0.]]

 [[ 0.  0.  0.]
  [ 0.  0.  0.]
  [ 0.  0.  0.]]]

>>> np.eye(4) # Utworzy jednostkową macierz 4x4.

array([[ 1.,  0.,  0.,  0.],
       [ 0.,  1.,  0.,  0.],
       [ 0.,  0.,  1.,  0.],
       [ 0.,  0.,  0.,  1.]])

```

Wspomnieliśmy powyżej, że rzadko zdarza się  wpisywać elementy tablic ręcznie. NumPy oferuje polecenia pozwalające manipulować rozmiarem tablicy. W połączeniu z poznanymi wyżej poleceniami `arange` i `linspace` łatwo tworzyć wielowymiarowe tablice wypełnione zadaną sekwencją:

```python
>>> tablica5 = np.arange(12).reshape(4,3) # Utworzy tablicę 12 elementów a następnie
                                      # ułoży ją w 4 kolumnach i 3 wierszach.
>>> print(tablica5)

[[ 0  1  2]
 [ 3  4  5]
 [ 6  7  8]
 [ 9 10 11]]

>>> tablica6 =  np.arange(24).reshape(2,3,4) # Przykład rozlokowania 24 elementów
                                         # w trójwymiarową tablicę.
>>> print(tablica6)

[[[ 0  1  2  3]
  [ 4  5  6  7]
  [ 8  9 10 11]]

 [[12 13 14 15]
  [16 17 18 19]
  [20 21 22 23]]]

```

###  Indeksowanie, iteracje, obcinanie

W tej części skryptu zapoznamy się z metodami indeksowania, iterowania i obcinania tablic.

Na początek weźmy na warsztat jednowymiarową tablice:

```python
>>> tablica7 = np.arange(20)
>>> print(tablica7)

[ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19]
```

W poniższym przykładzie wyświetlamy kolejno pierwszy (pamiętajmy, że NumPy wszystkie indeksy liczy od 0!!), trzeci licząc od początku listy  oraz przedostatni i ostatni od końca element tablicy.

Zatem dla `n` wymiarowej tablicy polecenie tablica[n] wyświetla `n−1` element.

```python
>>> tablica7[0], tablica7[2], tablica7[-1], tablica7[-2]

(0, 2, 19, 18)
```
**Uwaga**: Istotne jest abyśmy pamiętali, że takie operacje nie zmieniają zawartości tablicy!!
```python
>>> print(tablica7)

[ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19]
```

Aby wyświetlić fragment tablicy  od `n−1` -go do `m−1`  elementu używamy składni: `tablica[n:m]`,analogicznie aby wyświetlić elementy tablicy pomiędzy  `n−1` -ym  a (`m−1`) -szym przesuwając sie o wartość k używamy składni: `tablica[n:m:k]`.

```python
>>> tablica7[1:10] # Wyświetli elementy od drugiego do dziewiątego.

>>> array([1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> tablica7[2:18:2] # Wyświetli elementy od trzeciego do siedemnastego, co dwa.

>>> array([ 2,  4,  6,  8, 10, 12, 14, 16])

```
Sprawdźmy działania dla wielowymiarowych tablic, na przykładzie dwuwymiarowym:

```python

>>> tablica8 = np.arange(25).reshape(5,5) # tworzymy 25 elementową tablicę
>>> print(tablica8)

[[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [10 11 12 13 14]
 [15 16 17 18 19]
 [20 21 22 23 24]]

>>> tablica8[2,3] # Wyświetlamy element w trzecim wierszu i czwartej kolumnie.
13

>>> tablica8[2][3] # W inny sposób element z trzeciego wiersza i czwartej kolumny.
13

>>> tablica8[4] # Wyświetlamy piąty wiersz.

>>> array([20, 21, 22, 23, 24])

>>> tablica8[2:4] # Wyświetlamy  wiersze od trzeciego do czwartego.

>>> array([[10, 11, 12, 13, 14],
       [15, 16, 17, 18, 19]])
```

Nie! W opisie powyższego przykładu nie ma błedu. Zwróćmy uwagę jak wywoływaliśmy elementy tablic jednowymiarowych. W przypadku wielowymiarowym jest podobnie.

```python
>>> tablica8[:,4] # Wyświetlamy elementy z piątej kolumny.

>>> array([ 4,  9, 14, 19, 24])

>>> tablica8[:,2:4]# Wyświetlmy trzecią i czwartą kolumnę.

>>> array([[ 2,  3],
        [ 7,  8],
        [12, 13],
        [17, 18],
        [22, 23]])
```

Z analizy powyższego przykładu wynika, że przecinek (`[:,2:4]` tu zaznaczony na czerwono) w składni rozdziela poszczególne wymiary (w oryginalnej dokumentacji NymPy nazywane są one "osiami").

Mając w pamięci ten fakt, czytelne powinny być poniższe przykłady:

```python

>>> print(tablica8[1,1:5])  # Wyświetli elementy w drugim wierszu i w drugiej do piątej kolumnie.

array([6, 7, 8, 9])

>>> print(tablica8[1::3,:2]) # Wyświetli elementy od drugiego do trzeciego wiersza,
                  # znajdujące się w kolumnach od pierwszej do  drugiej.

array([[ 5,  6],
        [20, 21]])

>>> print(tablica8[1,0:5:2]) # Wyświetli elementy drugiego wiersza i
                  # biorąc kolumny od pierwszej do piątej co dwie.

array([5, 7, 9])

>>> print(tablica8[0:2,0:5:2]) # Wyświetli elementy w wierszach od pierwszego do drugiego
                    # które znajdują się w  co drugiej kolumnie licząc od pierwszej do piątej.

array([[0, 2, 4],
        [5, 7, 9]])
```

Jeszcze raz zwróćmy uwagę na to, że operacje powyższe nie zmieniły zawartości `tablica8`:

```python

>>> print(tablica8)

array([[ 0,  1,  2,  3,  4],
    [ 5,  6,  7,  8,  9],
    [10, 11, 12, 13, 14],
    [15, 16, 17, 18, 19],
    [20, 21, 22, 23, 24]])
```

Zaprezentujmy bardziej skomplikowany przykład:

```python

>>> tablica9 = np.arange(35).reshape(5,7)
>>> tablica10 = tablica9[np.array([0,2,4]), np.array([0,1,2])]

>>> print(tablica9)

array([[ 0  1  2  3  4  5  6]
 [ 7  8  9 10 11 12 13]
 [14 15 16 17 18 19 20]
 [21 22 23 24 25 26 27]
 [28 29 30 31 32 33 34]])

>>> print(tablica10)

array([ 0 15 30])
```

Co się stało w powyższym przykładzie?

Stworzyliśmy tablice 35 elementów, ułożyliśmy ją w pięć wierszy i siedem kolumn.

Nastepnie do `tablica10` wpisaliśmy element `{1,1}` element `{3,2}` i element `{5,3}` z `tablica9`.

Skorzystajmy z powyższego przykładu i w `tablica9` wyzerujmy elementy `{1,1}`, `{3,2}`, `{5,3}`:

```python
>>> tablica9[np.array([0,2,4]), np.array([0,1,2])]=0

>>> print(tablica9 )

array[[ 0  1  2  3  4  5  6]
 [ 7  8  9 10 11 12 13]
 [14  0 16 17 18 19 20]
 [21 22 23 24 25 26 27]
 [28 29  0 31 32 33 34]])
```

A teraz wyzerujmy piątą kolumnę:

```python

>>> y[4]=0

>>> print(y)

array[[ 0  1  2  3  4  5  6]
 [ 7  8  9 10 11 12 13]
 [14  0 16 17 18 19 20]
 [21 22 23 24 25 26 27]
 [ 0  0  0  0  0  0  0]])
```

.... i piaty wiersz:

```python

>>> y[:,4]=0

>>> print(y)

array[[ 0  1  2  3  0  5  6]
 [ 7  8  9 10  0 12 13]
 [14  0 16 17  0 19 20]
 [21 22 23 24  0 26 27]
 [ 0  0  0  0  0  0  0]])
```

Do manipulowania na tablicach możemy używać tablic indeksów.

W poniższym przykładzie wyświetlamy odpowiednie kwadraty liczb:

```python
>>> tablica11=np.arange(12)**2
>>> tablica_indeksow = np.array( [0,1,1,2,7,6,11] )
>>> tablica11[tablica_indeksow]

array([  0,   1,   1,   4,  49,  36, 121])

```

### Zmiana kształtu tablic
W tej części skryptu zapoznamy się z kilkoma metodami transformacji kształtu tablic.

```python
>>> tablica12 = np.arange(15)  #zadeklarujmy tablicę piętnastu elementów
print(tablica12)
[ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14]

>>> tablica12.reshape(3,5) # zmieńmy jej kształt

array([[ 0,  1,  2,  3,  4],
       [ 5,  6,  7,  8,  9],
       [10, 11, 12, 13, 14]])

>>> print(tablica12)

[ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14]
```
**Uwaga**: Operacja "reshape" nie zmieni zawartości oryginalnej tablicy, pokaże jedynie jej elementy w zadanej postaci!

Aby w istocie zmienić kształt tablicy możemy postąpić tak:

```python
>>> tablica13 = tablica12.reshape(3,5) # przypiszmy uzyskany widok do nowej tablicy
>>> print(tablica13)

[[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [10 11 12 13 14]]
```

.... lub odwołać się do polecenia `resize`.

```python
>>> tablica12.resize(3,5)
>>> print(tablica12)

[[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [10 11 12 13 14]]

>>> tablica13.shape # sprawdźmy wymiar tablicy

(3, 5)
>>> tablica13.shape[0] # sprawdźmy pierwszy wymiar

3

>>> tablica13.shape[1] # sprawdźmy drugi wymiar

5

>>> tablica13.size # oraz ilość wszystkich elementów w tablicy

15
```

NumPy oferuje polecenia znane z algebry liniowej, takie jak na przykład transpozycja:

```python
>>> print(np.transpose(tablica12))

array([[ 0,  5, 10],
       [ 1,  6, 11],
       [ 2,  7, 12],
       [ 3,  8, 13],
       [ 4,  9, 14]])

>>> print(tablica12)

[[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [10 11 12 13 14]]
```

podobnie jednak jak przy funkcji `reshape`, aby zachować wynik musimy go przypisać do nowej zmiennej. Podobnie jest z poleceniem:

```python
>>> swapaxes(tablica, wymiar1, wymiar2)
```

które wyświetli  zmienione wiersze z kolumnami dla tablicy dwuwymiarowej. Dla wielowymiarowych tablic zmieni ono elementy dla zadanych osi.

```python
>>> print(np.swapaxes(tablica12,0,1))

array([[ 0,  5, 10],
       [ 1,  6, 11],
       [ 2,  7, 12],
       [ 3,  8, 13],
       [ 4,  9, 14]])
```

Aby zmienić tablicę na jednowymiarową, możemy sie odwołać do polecenia "ravel":

```python
>>> tablica14 = np.ravel(tablica12)
>>> print(tablica14)

[ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14]
```

Natomiast aby zmienić jej typ na standardową listę użyjemy polecenia "tolist()"

```python

>>> print(tablica14.tolist())

[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
```

### Podstawowe operacje

Zaprezentujmy teraz podstawowe operacje na elementach tablic i na samych tablicach. Zwróćmy uwagę, że we wszystkich poniżej zaprezentowanych przykładach wszystkie  operacje wykonywane są na elementach tablic.


```python
>>> tablica15 = np.array([10,20,30,40,50])
>>> tablica16 = np.array([1,2,3,4,5])
>>> tablica17=tablica15+tablica16 # przykład sumy
>>> print(tablica17)

array([11, 22, 33, 44, 55])

>>> tablica18=tablica15-tablica16  # przykład dla różnicy
>>> print(tablica18)

[ 9 18 27 36 45]

>>> tablica19=np.sqrt(tablica15) # przykład dla pierwiastków
>>> tablica20 = sqrt(tablica15)
>>> print(tablica19)

[ 3.16227766  4.47213595  5.47722558  6.32455532  7.07106781]

>>> print(tablica20)

[ 3.16227766  4.47213595  5.47722558  6.32455532  7.07106781]

>>> tablica21 = tablica16**2 # kwadrat elementów tablicy
>>> print(tablica21)

[ 1  4  9 16 25]

>>> tablica22=  10*np.cos(tablica16)# cosinus z kolejnych elementów tablicy i mnożenie
                                #wyniku przez skalar
>>> print(tablica22)

[ 5.40302306 -4.16146837 -9.89992497 -6.53643621  2.83662185]
```

##### Porównania elementów tablic:

```python
>>> print(tablica16>tablica15)

array([False, False, False, False, False], dtype=bool)

>>> print(tablica15<tablica16)

array([False, False, False, False, False], dtype=bool)

>>> print(tablica15 < 30)

array([ True,  True, False, False, False], dtype=bool)

>>> print(tablica16 == 1)

array([ True, False, False, False, False], dtype=bool)

>>> print(np.any( tablica15 > 6 )) # prawdziwe, jeśli każdy element z osobna  spełnia warunek

True

>>> print(np.all( tablica15 != tablica16 )) # prawdziwe jeśli wszystkie elementy spełniają warunek

True

>>> i = np.identity( 3 )
>>> print(i)

[[ 1.  0.  0.]
 [ 0.  1.  0.]
 [ 0.  0.  1.]]

>>> print(i+i) # dodawanie dwóch tablic

[[ 2.  0.  0.]
 [ 0.  2.  0.]
 [ 0.  0.  2.]]

print(i+4)     # dodawanie skalara do tablicy, zwróć uwagę, że 4 została
              #  dodana do każdego elementu tablicy.

[[ 5.  4.  4.]
 [ 4.  5.  4.]
 [ 4.  4.  5.]]

>>> k =  (i+4)*2
>>> print(k)

[[ 10.   8.   8.]
 [  8.  10.   8.]
 [  8.   8.  10.]]

print(k*k) # mnożony jest element przez element!

array([[ 100.,   64.,   64.],
       [  64.,  100.,   64.],
       [  64.,   64.,  100.]])
```

**Uwaga**: W odróżnieniu od powyższego przykładu aby pomnożyć tablicę dwuwymiarową tak jak mnoży się macierze musimy użyć polecenia `dot`:

```python
>>> np.dot(k,k)

array([[ 228.,  224.,  224.],
       [ 224.,  228.,  224.],
       [ 224.,  224.,  228.]])
```

Co się stanie, jesli będziemy próbować wykonywać operację na tablicach różniących się rozmiarami? Sprawdźmy to:

```python
>>> a = np.arange(0, 40, 10)
>>> a = a.reshape((4,1))
>>> print(a)
>>> b = np.arange(0, 3)
>>> print(b)

[[ 0]
 [10]
 [20]
 [30]]
[0 1 2]
>>> print(a+b)

[[ 0  1  2]
 [10 11 12]
 [20 21 22]
 [30 31 32]]

```
Jak już zobaczyliśmy, podstawowe operacje (sumowanie, etc.) w NumPy są wykonywane element po elemencie. Wcześniej przekonaliśmy się, że świetnie działa to dla tablic o tych samych wymiarach.

Jak widać z powyższego przykładu, dokonywanie tych samych operacji na tablicach różniących się rozmiarem jest możliwe. NumPy automatycznie przetransformuje je tak, by wymiary się zgadzały.

Takie zachowanie nazywane jest broadcasting-iem.

### Referencje

* https://sage3.icse.us.edu.pl/home/pub/21/
* https://docs.scipy.org/doc/numpy/user/quickstart.html
