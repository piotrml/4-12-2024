a = 10
b = 90


def dodaj():
    print(a + b)


def dodaj2(a, b):
    print(a + b)


def odejmij(a, b, c=0):
    print(a - b - c)


# to jest podpowiedz typów a nie typowanie
def mnozenie(a: int, b: int) -> int:
    """
    te int są podpowiedziami
    :param a:
    :param b:
    :return:
    """
    return a, b, a * b


dodaj()
dodaj2(23, 12)
odejmij(3, 1)
odejmij(3, 1, 4)

print(mnozenie(2.5, 6))  # 15.0 # po zmianie (2.5, 6, 15.0)
x, y, z = mnozenie(6, 9)
# wynikiem jest krotka
print(f'Wynik działania {x} * {y} = {z}')
# Wynik działania 6 * 9 = 54

# argumenty po nazwie
odejmij(b=9, c=8, a=12)  # -5

# argumenty mieszane
odejmij(1, c=9, b=89)  # -97
# najpierw muszą być pozycyjne
# odejmij(a=1,9,b89)  # SyntaxError: positional argument follows keyword argument

