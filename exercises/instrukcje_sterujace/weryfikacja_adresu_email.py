
"""
Odrobina historii...
Internet sięga swymi korzeniami lat sześćdziesiątych, gdy naukowcy, głównie
amerykańscy, starali się stworzyć sieć odporną na uszkodzenia, łatwo
rozbudowywalną oraz umożliwiającą komunikację ośrodków obronnych i naukowych z
całego kraju. Wreszcie w 1969 roku - bardzo istotnym też z innych względów:
wylądowaliśmy na Księżycu, powstał jezyk C i system Unix, miał miejsce Festiwal
Woodstock i urodził się Linus Torvalds, twórca Linuksa - powstała sieć ARPANET,
która z biegiem czasu przekształciła się w znany nam Internet. Przy tworzeniu
sieci ARPANET, Steve Crocker wpadł na pomysł dokumentacji jej rozwoju w
dokumentach o nazwie Request for Comments (RFC), które z czasem stały się
dokumentacją rozwoju Internetu, zawierającą m.in. specyfikacje wykorzystywanych
protokołów. Przez lata dokumenty te tworzone były przez osoby zajmujące się
rozwojem Sieci, głównie naukowców i inżynierów. Warto tu wspomnieć o jednym z
nich, Jonie Postelu, który nazywany jest jednym z ojców Internetu. Po
jego śmierci Vint Cerf (druga ważna postać) napisał RFC 2468
(https://tools.ietf.org/html/rfc2468), notatkę na temat Jona Postela. Aktualnie
publikacją dokumentów RFC zajmuje się Internet Engineering Task Force.

Twoim zadaniem jest napisanie programu, który będzie sprawdzał poprawność
danego adresu e-mail (właściwie: funkcji zwracającej wartość logiczną, mówiącą,
czy dany adres jest poprawny). Dokładne reguły opisane są w trzech dokumentach RFC:

RFC 5322 - Internet Message Format
https://tools.ietf.org/html/rfc5322

RFC 3696 - Application Techniques for Checking and Transformation of Names
https://tools.ietf.org/html/rfc3696

RFC 5321 - Simple Mail Transfer Protocol
https://tools.ietf.org/html/rfc5321

Zasad jest mnóstwo, na potrzeby naszego zadania jednak znacznie je zawęzimy.

Poprawny adres dla nas:
 - składa się z części lokalnej i domenowej, oddzielonych jednym znakiem @,
 - składa się z maksymalnie 254 znaków,
 - nie zawiera podwójnych kropek,
 - nie zaczyna ani nie kończy się kropką,
 - nie zawiera spacji.

Część lokalna (przed '@'):
 - składa się tylko z angielskich liter (a-z, A-Z), cyfr (0-9) i tych znaków
   specjalnych: ! # $ % & ' * + - / = ? ^ _ ` { | } ~ ` '
 - składa sie maksymalnie z 64 znaków.

Część domenowa (za '@'):
 - składa się tylko z angielskich liter (a-z, A-Z), kropek (.) i myślników (-),
 - składa się maksymalnie z 253 znaków.

Oczywiście zasady po "Poprawny adres..." stosują się również do obu części,
np. w nazwie domenowej nie może być dwóch kropek bezpośrednio jedna po
drugiej.

"""

import unittest

def sprawdz_adres(email):
    pass

class TestWeryfikacjaAdresuEmail(unittest.TestCase):
    def test_poprawne(self):
        self.assertTrue(sprawdz_adres('adam@gmail.com'))
        self.assertTrue(sprawdz_adres('katarzyna@example.com.pl'))
        self.assertTrue(sprawdz_adres('ludw!cze|{@ppp-ad.com'))
        self.assertTrue(sprawdz_adres('!#$%*_^&+-~`\'@papa.org'))
        self.assertTrue(sprawdz_adres('ala-ma-kota@gmial.com'))
        self.assertTrue(sprawdz_adres('kota_ma_Ale=False@wp.pl'))
        self.assertTrue(sprawdz_adres('$@b.c'))

    def test_niepoprawne(self):
        self.assertFalse(sprawdz_adres('@@'))
        self.assertFalse(sprawdz_adres('a@@c.c'))
        self.assertFalse(sprawdz_adres('a..b@c'))
        self.assertFalse(sprawdz_adres('.ala@gmail.com'))
        self.assertFalse(sprawdz_adres('ala@gmail.com.'))
        self.assertFalse(sprawdz_adres('a;s@wp.pl'))
        self.assertFalse(sprawdz_adres('a a@c.c'))
        self.assertFalse(sprawdz_adres('ó@c.c'))
        self.assertFalse(sprawdz_adres('ł@c.c'))
        self.assertFalse(sprawdz_adres('l@ą.c'))
        self.assertFalse(sprawdz_adres('a@c!#$%&*+-/=?^_`{|}~`\'c'))
        self.assertFalse(sprawdz_adres('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
                                     + 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa@c.c'))
        self.assertFalse(sprawdz_adres('a@zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz.'\
                                     + 'cccccccccccccccccccccccccccccccccccc'\
                                     + 'cccccccccccccccccccccccccccccccccccc'\
                                     + 'cccccccccccccccccccccccccccccccccccc'\
                                     + 'cccccccccccccccccccccccccccccccccccc'\
                                     + 'cccccccccccccccccccccccccccccccccccc'\
                                     + 'cccccccccccccccccccccccccccccccccccc'\
                                     + 'cccccccccccccccccccccccccccccccccccc'\
                                     + 'cccccccccccccccccccccccccccccccccccc'\
                                     + 'cccccccccccccccccccccccccccccccccccc'))


if __name__ == '__main__':
    unittest.main()
