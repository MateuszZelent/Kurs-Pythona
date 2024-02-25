
a = 3 + 2.1j # zmienna typu complex
b = complex(3, 2.1) # inny sposob inicjalizjacji - jawne wywolanie konstruktora
print('a == b: ' + str(a == b))

# czesc rzeczywista i urojona
print('a = ' + str(a.real) + '+' + str(a.imag) + 'i')

# c = sprzezenie
c = a.conjugate()
print('c = ' + str(c.real) + '+' + str(c.imag) + 'i')

# mozna wypisywac i tak
d = 1+0.7j
print('d = ' + str(d))

# podstawowe dzialania
print ('a * d = ' + str(a * d))
print ('a + c = ' + str(a + c))
