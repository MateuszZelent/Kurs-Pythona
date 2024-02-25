
# zdefiniujmy funkcję, która wypisze daną listę:
def wypisz_liste(lista, nazwa=''):
    if nazwa:
        print('lista ' + nazwa + ':')
    # bardzo przydatna metoda join służąca do łączenia napisów
    # w nawiasie podajemy sekwencję, a jako wynik dostaniemy jej elementy
    # oddzielone napisem str:
    # str.join(seq)
    print(', '.join([str(i) for i in lista]))

a = [3, 1, -4, 5]
wypisz_liste(a, 'a')

# funkcja sum pozwala na sumowanie elementów listy
print('suma elementow w a: ' + str(sum(a)) + '\n')

# metoda sort sortuje listę a
a.sort()
print('po sortowaniu')
wypisz_liste(a, 'a')
print()

# co sie stanie?
reversed(a)
print('po reversed')
wypisz_liste(a, 'a')
print()

# reversed zwraca iterator, ale nie zmienia listy
# aby otrzymać listę a z odwróconą kolejnością, musimy dodać nową zmienną
b = list(reversed(a))
wypisz_liste(b, 'b')

# sorted zwraca posortowaną listę
print()
wypisz_liste(sorted(b), 'posortowana b')

# metoda clear czyści listę
print()
b.clear()
wypisz_liste(b, 'pusta lista b')


# zdefiniujmy następującą listę
miasta = ['   warszawa  ', '     nowy jork ', 'moskwa  ', '  delhi  ']
wypisz_liste(miasta, 'miasta')
print()

# i z każdej nazwy usuńmy zewnętrzne spacje (strip()) oraz pierwsze litery
# każdego wyrazu zamienimy na wielkie (title())

miasta = [(nazwa.strip()).title() for nazwa in miasta]
wypisz_liste(miasta, 'miasta')
print()

# zdefiniujmy teraz listę dwuwymiarową, reprezentującą pewną tabelę
#           imie | nazwisko | wiek
osoby = [['Anna', 'Nowak', 35],
         ['Kamil', 'Kowalski', 55],
         ['Joanna', 'Mil', 40],
         ['Adam', 'Wilk', 30]]
wypisz_liste(osoby, 'osoby')
print()

# i odfiltrujmy osoby powyżej 35 roku życia
osoby_powyzej_35_lat = [osoba for osoba in osoby if osoba[2] > 35]
wypisz_liste(osoby_powyzej_35_lat, 'osoby_powyzej_35_lat')
print()


