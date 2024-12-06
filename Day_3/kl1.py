# klasy

import math


class MyFirstClass:
    """
    Klasa w Pythonie opisujące punkty w przestrzeni x i y
    """

    def __init__(self, x=0, y=0):
        """
        Metoda inicjalizująca (konstruktor)
        :param x:
        :param y:
        """
        self.x = x
        self.y = y

    def move(self, x: int, y: int) -> None:
        """
        Metoda przesunięcie punkt w miejsce
        :param x:
        :param y:
        :return:
        """
        self.x = x
        self.y = y

    def reset(self):
        """
        Reset ustawień
        :param x:
        :param y:
        :return:
        """
        self.move(0, 0)

    def calculate(self, other: "MyFirstClass") -> float:
        return math.hypot(self.x - other.x, self.y - other.y)

    def __str__(self):
        return f'{self.x, self.y}'

    def __repr__(self): # reprezentacja obiektu
        return f'Point({self.x, self.y}'


print(MyFirstClass.__doc__)
# Klasa w Pythonie opisujące punkty w przestrzeni x i y

ob1 = MyFirstClass()
print(ob1.x)  # 0
print(ob1)  # <__main__.MyFirstClass object at 0x000002975EC180B0>
# po dopisaniu metody __str__
# print(ob1) daje (0, 0)
ob1.move(100, 456)
print(ob1)
ob1.reset()
print(ob1)
ob2 = MyFirstClass(45, 89)
print(ob2)
print(ob1.calculate(ob2))  # 99.72963451251589

lista = [ob1, ob2]
for i in lista:
    print(i)

print(lista)
# [<__main__.MyFirstClass object at 0x0000016DB7E2A1E0>, <__main__.MyFirstClass object at 0x0000016DB7E2AC30>]
# po dopisaniu metody repr
# print wyświetla już wartości [Point((0, 0), Point((45, 89)]