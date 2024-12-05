import sys

# ctrl + alt + l - formatuje do POP8

print("Tekst")
print('drugi tekst')
# komentarzz
# ctrl / - komentarz
print(type('Typ_String'))

print(39)
print(type(39))
print(sys.int_info)

# podpowiedzi typów jest falka jeżeli coś nie się nie zgadza
name: str = "Tomek"
print(name)  # Tomek
name = 90
print(name)  # 90

print(0.1 + 0.5)  # 0.6
print(0.1 + 0.7)  # 0.7999999999999999
print(0.1 + 0.2)  # 0.30000000000000004

# decimal - typ danych do przechowywania pięniędzy, omija problem zaokrąglania

wersja = 3.90001
# f - fstring, sformatowany tekst
print(f"wersja Pythona {wersja}")  # wersja Pythona 3.90001
print(f"wersja Pythona {wersja:.1f}")  # wersja Pythona 3.9
print(f"wersja Pythona {wersja:.2f}")  # wersja Pythona 3.90
print(f"wersja Pythona {wersja:.0f}")  # wersja Pythona 4

liczba = 3.8676
print(round(liczba, 2))  # 3.87

print(f"wersja Pythona {wersja:.^25}")  # wyśrodkuj wersja Pythona .........3.90001.........
print(f"wersja Pythona {wersja:.<25}")  # wyrównaj do lewej wersja Pythona 3.90001..................
print(f"wersja Pythona {wersja:.>25}")  # wyrównaj do prawej wersja Pythona ..................3.90001
print(f"wersja Pythona {wersja:^25}")  # wyśrodkuj wersja Pythona          3.90001
print(f"wersja Pythona {wersja:>25}")  # wyrównaj do prawej wersja Pythona                   3.90001

liczba1 = 35459045094
print(f"wersja Pythona {liczba1:_}")  # wersja Pythona 35_459_045_094
print(f"wersja Pythona {liczba1:_}".replace('_', " "))  # wersja Pythona 35 459 045 094

