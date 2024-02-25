### Typ logiczny (bool)

# funkcja wbudowana (built-in function) str() pozwala na
# kowersje wartosci do napisu
to_be = True
print('to_be or not to_be: ' + str(to_be or not to_be)) # True
print() # wypisze pusta linie

# operatory porownania
a = 10
b = 15
print('a == 10 and b == 15: ' + str(a == 10 and b == 15))
# W przypadku wielokrotnego porównania jednej zmiennej
# mozemy pominac operatory logiczne - w tym przypadku and
print('8 < a < 12: ' + str(8 < a < 12)) # zamiast a > 8 and a < 12
print()

# niezerowe wartosci liczbowe daja True
# bool() - konwersja (rzutowanie) do typu logicznego
print('bool(0): ' + str(bool(0))) # False
print('bool(123): ' + str(bool(123))) # True
print()

# analogicznie napisy
print('pusty napis: ' + str(bool(''))) # False
print('niepusty: ' + str(bool('sama prawda'))) # True
print()

# operatory porownania
print('15 >= 13 ' + str(15 >= 13))
print('4 <= 3: ' + str(4 <= 3) + '\n') # '\n' - znak nowej linii
                                     # to samo co print()

# roznica miedzy operatorem porownania =
# a operatorem identycznosci is
print('1000000 is 100**3: ' + str(1000000 is 100**3)) # False
print('1000000 == 100**3: ' + str(1000000 == 100**3)) # True
