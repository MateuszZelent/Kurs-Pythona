
kilka_linii = """Raz
dwa
trzy
...
kryjesz
Ty!"""
print(kilka_linii)
print()

imie = 'Jan'
nazwisko = "Kowalski"
tekst_z_cytatem = "'Na brodę Merlina' - wykrzyknął Silnoręki"
# zmienne typu str i napisy (w ' ' lub " ") laczymy operatorem +
print(imie + ' ' + nazwisko)
print(tekst_z_cytatem + '\n')

# same napisy (tzw. literały) mozna laczyc, po prostu zestawiajac je obok siebie
a = 'kto tam?...' ' hipopotam\n' 
print(a)

# wycinki tekstu (slice)
alfabet = 'abcdefghijklmnopqrstuvwxyz'
print ('alfabet = ' + alfabet)
print('alfabet[3:7] = ' + alfabet[3:7]) # 'defg'
print('alfabet[-1] = ' + alfabet[-1]) # 'z'

# napisow nie mozna zmieniac (immutable)
# to nie zadziala
# alfabet[3] = 'w'

# kilka metod
print(alfabet.center(50, '-') + '\n') # wypelnienie do 50 znakow (myslnikami) i wycentrowanie

tytul = 'gotowe na wszystko'
print(tytul.title()) # wersja "tytulowa" - wielka litera 
                     # na poczatku kazdego wyrazu
print()

litery_cyfry = 'abcdef012345'
print(str(litery_cyfry.isalnum())) # czy w napisie wystepuja
                                   # tylko znaki alfanumeryczne

inne = 'halo, halo\n'
print(str(inne.isalnum())) # False ze wzgledu na znak nowej linii '\n'
print()

# tablica ASCII
# konwersja liczby na znak
print(chr(100)) # d
# kod litery 'Z'
print(ord('Z')) # 90
