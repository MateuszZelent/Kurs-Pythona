## Moduł matplotlib (matplotlib.org)

Matplotlib słuzy do wizualizacji wszelkiego rodzaju danych. Jego zaletami jest prostota, ogromne mozliwości, wieloplatformowość oraz łatwa integracja z graficznymi interfejsami użytkownika.

MatPlotLib jest częścią pakietu PyLab, który warto zaimportować w całości aby mieć dostęp do wielu dodatkowych, bardzo użytecznych funkcji:

```python
#!/ usr / bin / env python
# -*- coding : utf -8 -*-
from pylab import *

```
## Przykłady

### Wykres jednej zmiennej
```python
# tablica liczb o równomiernym rozkładzie
x = linspace(-10, 10, 100)
# funkcja do wyrysowania
y = sin(x)* cos(x / 2)
plot(x, y) # rysowanie funkcji y(x)
# kolejna funkcja
z = sin(x)/ x
plot(x, z)
# wyświetlenie wykresu
show()
```

### Wiele funkcji, jeden wykres

```python
x = linspace(-10, 10, 100)
y = sin(x)* cos(x / 2)
z = sin(x) / x
p = exp(-x**2)
# wiele funkcji w jednym plocie
plot(x, y, x, z, x, p)
show()
```

### Parametry linii i opis wykresu

```python
x = linspace(-10, 10, 100)
y = sin(x)*cos(x / 2)
z = sin(x) / x
# grubość linii (`lw`), kolor (`c`), opis (`label`)
plot(x, y, lw=3, c="red", label="funkcja 1")
# rodzaj linii (`ls`)
plot(x, z, ls ="--", c="g", label="funkcja 2")
# opis wykresu
title(u" Tytul") # "u" na początku oznacza kodowanie utf -8
xlabel(u"x")
ylabel(u"y")
# legenda
legend(loc=2) # loc - numer rogu wykresu
show()
```

### Rozmiar, rozdzielczość i rysowanie punktów

```python
# rozmiar okna i rozdzielczość
figure(figsize=(12, 8) , dpi=100) # 1200x800 pikseli
x = linspace(-10, 10, 100)
y = sin(x) * cos(x / 2)
z = sin(x) / x
# punkt(marker) zamiast linii
plot(x, y, ls ="", marker ="o", markersize =5 , c="brown")
plot(x, z, ls ="", marker ="+", markersize =15 , c="orange")
title(u" Title")
xlabel(u"x")
ylabel(u"y")
show()
```

### Jeden wykres w jednym oknie

```python
figure(figsize =(12, 8), dpi=100) # 1200 x800 pikseli
x = linspace (-2*pi, 2*pi, 100)
# subplot czyli siatka wykresów
# opcje : liczba wierszy i kolumn oraz numer aktualnego wykresu
subplot(2 , 2, 1)
plot(x, sin (x ))
subplot(2, 2, 2)
plot(x, sin (x )/ x)
subplot(2, 2, 3)
plot(x, exp (-x **2))
subplot(2, 2, 4) # można podać parametry bez przecinków!
plot(x, sqrt(1 - x**2))
show()
```

### Gotowy przykład - filtr górnoprzepustowy

```python
import matplotlib.pyplot as plt
import numpy as np
from scipy import ndimage
from skimage.io import imread
from PIL import Image
import scipy.fftpack as fp


def do_plot(data, title, gray=False):
    do_plot.id += 1
    plt.subplot(2, 2, do_plot.id)
    plt.imshow(data)
    if gray:
        plt.imshow(data, cmap=plt.cm.gray)
    else:
        plt.imshow(data)
    plt.title(title)


file_name = 'pic_01.jpg' # Zdjęcie powinno być kwadratowe. Tylko dla takiego transformata Fouriera zadziała.

try:
    image = imread(file_name)
except:
    raise ValueError('Nie ma takiego pliku w katalogu, w ktorym pracujesz')

# Sprawdź, czy obrazek jest kwadratowy. Jeśli nie wytnij z niego kwadrat
if image.shape[0] != image.shape[1]:
    image = image[:min(image.shape[0:1]), :min(image.shape[0:1]), :]

do_plot.id = 0

# Pierwszy wykres zawiera orginalne zdjęcie
do_plot(image, 'Original')

# Drugi wykres wyświetli nam FFT
average_colors = np.mean(image, axis=2)
F = np.fft.fftshift(np.fft.fft2((average_colors)))
do_plot(np.log10( 0.1 + abs(F)), 'Fourier Transform', True) # Stosujemy skalę logarytmiczną

# Trzeci wykres wyświetli nam FFT z filtrem górnoprzepustowym
w, h = average_colors.shape
half_w, half_h = w//2, h//2
n = 25 # Określa wilkość kwadratu
F[half_w-n:half_w+n+1,half_h-n:half_h+n+1] = 0 # współczynniki Fouriera dla kwadratu zerujemy
do_plot(np.log10( 0.1 + abs(F)), 'Fourier Transform with highpass filter', True)

# Czwarty wykres to odwrotna transformata Fouriera. Zdjęcie wynikowe po nałożeniu filtra górnoprzepustowego
do_plot(np.fft.ifft2(np.fft.ifftshift(F)).real, 'Output', True)

plt.show()
```
### Gotowy przykład - całkowanie metodą trapezów

```python
import numpy as np
from math import sin
import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig, ax = plt.subplots()

zakres = [0, 2]
el = 20

def func(value):
    return np.exp(value**2) - 3*value - 3

x = np.linspace(*zakres, el)
y = np.array([func(i) for i in x])

for pos in np.linspace(*zakres, el/2):
    val = func(pos)
    if val >= 0:
        ax.add_artist(patches.Rectangle((pos - zakres[1]/el, 0), zakres[1]/el*2, val, alpha=0.5, color='g'))
    else:
        ax.add_artist(patches.Rectangle((pos - zakres[1]/el, 0), zakres[1]/el*2, val, alpha=0.5, color='r'))
plt.plot(x, y)
plt.grid()
plt.title(r'$\int( \exp(x^2) -3x -3 )dx = $' + str(np.trapz(y)))
plt.xlabel(r'$x$')
plt.ylabel(r'$y$')
plt.show()
```

### Gotowy przykład - dwie funkcje na wykresie

```python
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')

x = np.linspace(0, 1)
y = 13 + x**4 + x**2 - np.sin(5*x)
z = 13*x + np.log10(y)


fig, ax1 = plt.subplots()
ax1.set_title(r'$Title$')
ax1.set_xlabel(r'$x$')
ax1.set_ylabel(r'$y$', color='C1')
ax1.tick_params('y', colors='C1')
ax1.plot(x, y, c='C1')

for i in ax1.get_ygridlines():
    i.set_color('C1')


ax2 = ax1.twinx()
ax2.set_ylabel(r'$z$', color='C0')
ax2.tick_params('y', colors='C0')
ax2.plot(x, z, c='C0')
ax2.grid(color='C0', alpha=0.5)
fig.tight_layout()
plt.show()
```
