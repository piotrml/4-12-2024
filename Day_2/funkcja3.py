# lambda - skrócony zapis funkcji
# lambda jako funkcja anonimowa (bez nazwy, bez wcześniejszej deklaracji - uzywamy w miejscu deklaracji)
# lambda ma zawsze return

from funtools import reduce

def liczymy(x, y):
    return x * y


print(liczymy(4, 7))  # 28

liczymy2 = lambda x, y: x * y
print(liczymy2(9, 7))  # 63

# mapowanie danych

lista = [1, 2, 6, 15, 67, 90]
lista_wyn = []
for x in lista:
    lista_wyn.append(x * 2)
print(lista_wyn)  # [2, 4, 12, 30, 134, 180]

print([i * 2 for i in lista])  # [2, 4, 12, 30, 134, 180]


def zmien(x):
    return x * 2


lista_wyn1 = []

for i in lista:
    lista_wyn1.append(zmien(i))
print(lista_wyn1)

print(f"Zastosowanie map: {list(map(zmien, lista))}")
# Zastosowanie map: [2, 4, 12, 30, 134, 180]

print(f"Zastosowanie map i lambda: {list(map(lambda x: x * 2, lista))}")
# Zastosowanie map i lambda: [2, 4, 12, 30, 134, 180]
print(f"Zastosowanie map i lambda: {list(map(lambda x: x * 3, lista))}")
# Zastosowanie map i lambda: [3, 6, 18, 45, 201, 270]


# filtrowanie danych
for i in lista:
    if i < 10:
        print(i)

print(f'Uzycie filtr() {list(filter(lambda x: x < 10, lista))}')
#Uzycie filtr() [1, 2, 6]
print(f'Uzycie filtr() {list(filter(lambda x: x < 50, lista))}')
# Uzycie filtr() [1, 2, 6, 15]
print(f'Uzycie filtr() {list(filter(lambda x: 10 < x < 50, lista))}')
# Uzycie filtr() [15]

# reduce
