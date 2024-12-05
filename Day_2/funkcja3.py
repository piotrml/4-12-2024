# lambda - skrócony zapis funkcji
# lambda jako funkcja anonimowa (bez nazwy, bez wcześniejszej deklaracji - uzywamy w miejscu deklaracji)
# lambda ma zawsze return

def liczymy(x, y):
    return x * y


print(liczymy(4, 7))  # 28

liczymy2 = lambda x, y: x * y
print(liczymy2(9, 7))  # 63

lista = [1, 2, 6, 15, 67, 90]
lista_wyn = []
for x in lista:
    lista_wyn.append(x * 2)
print(lista_wyn)  # [2, 4, 12, 30, 134, 180]

print([i * 2 for i in lista])  # [2, 4, 12, 30, 134, 180]
# moznenie_przez2 = lambada lista: for x in lista: x * 2
