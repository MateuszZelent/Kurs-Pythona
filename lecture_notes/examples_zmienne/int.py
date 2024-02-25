print('typ calkowitoliczbowy - int')
print('312 + 5343 = ' + str(312 + 5343)) # 5655
print('35 % 6 = ' + str(35 % 6)) # 5 (bo 35 = 6 * 5 + 5)
print('14 / 10 = ' + str(14 / 10)) # 1.2
print('14 // 10 = ' + str(14 // 10)) # 1, dzielenie calkowitoliczbowe
print()

# wbudowane funkcje bin, oct, hex, konwertujace
# liczby zapisane w systemie dziesietnym na liczby w systemach, odpowiednio,
# dwojkowym, osemkowym i szesnastkowym (trzy podstawowe w informatyce)
# liczba w nawiasie oznacza podstawe systemu, w ktorym zapisana jest liczba
# (zauwaz, ze Python pozwala je rozroznic, dodajac przyrostki 0b, 0o oraz 0x)
# domyslnie przyjmujemy za podstawe 10
print('konwersje miedzy systemami liczbowymi')
print('142(10) = ' + str(bin(142)) + '(2)') # 0b10001110(2)
print('54(10) = ' + str(oct(54)) + '(8)') # 0o66(8)
print('255(10) = ' + str(hex(255)) + '(16)') # 0xff(16)
print()

# by dokonac konwersji w druga strone, wykorzystujemy wbudowana funkcje int()
# ktorej przekazujemy podstawe systemu podanej liczby
# (podajemy ja w formie napisu, chocby ze wzgledu na wystepowanie liter
# w systemach o podstawie wiekszej od 10)
print('110101(2) = ' + str(int('110101', 2)) + '(10)')
print('3213(4) = ' + str(int('3213', 4)) + '(10)')
print('555(7) = ' + str(int('555', 7)) + '(10)')
print()

print('operacje bitowe')
a = 27
b = 35
c = 66
print('a = ' + str(bin(a)))
print('b = ' + str(bin(b)))
print('c = ' + str(bin(c)))
print('a & b = ' + str(bin(a & b)) + ' = ' + str(a & b))
print('a | c = ' + str(bin(a | c)) + ' = ' + str(a | c))

