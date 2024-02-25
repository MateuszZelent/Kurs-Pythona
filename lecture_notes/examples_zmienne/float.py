
a = 34.913
b = 12.64
# float oferuje te same operacje, co int
print('a = ' + str(a))
print('b = ' + str(b))
print('a + b = ' + str(a + b))
print('a / b = ' + str(a / b))
print('a % b = ' + str(a % b))

# funkcja round pozwala zaokraglac liczby
print('\nzaokraglanie: ')
print('a % b = ' + str(round(a % b, 3))) # tu do 3. miejsca po przecinku
print('a / b = ' + str(round(a / b, 1))) # a tu do 1.

# metoda float.as_integer_ratio() zwraca pare liczb typu int:
# licznik i mianownik danej liczby
print('\njako ulamek: ')
print('a = ' + str(a.as_integer_ratio()[0]) + '/' + str(a.as_integer_ratio()[1]))

# float.is_integer() pozwala sprawdzic, czy dana liczba typu float jest liczba
# calkowita
c = 5.00
print('\nc = ' + str(c))
print('c jest liczba calkowita: ' + str(c.is_integer()))
