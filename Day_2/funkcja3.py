# lambda - skrócony zapis funkcji
# lambda jako funkcja anonimowa (bez nazwy, bez wcześniejszej deklaracji - uzywamy w miejscu deklaracji)
# lambda ma zawsze return

def liczymy(x, y):
    return x * y


print(liczymy(4, 7))  # 28

liczymy2 = lambda x, y: x * y
print(liczymy2(9, 7)) # 63

