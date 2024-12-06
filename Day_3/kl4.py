# wielodziedziczenie
class A:
    def metod(self):
        print('Metoda z klasy A')


class B:
    def metod(self):
        print('Metoda z klasy B')


class C(B, A):
    """
    Klasa dziedziczy po A i B
    """


a = A()
a.metod()  # Metoda z klasy A
b = B()
b.metod()  # Metoda z klasy B
c = C()
c.metod()  # Metoda z klasy B
print(C.__mro__)


# (<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
# przeszukuje pokoleii poszczególne klasy czy w niej isnieją

class D(A, B):
    """
    Dziedziczenie po A i B
    """


d = D()
d.metod()  # Metoda z klasy A
print(D.__mro__)


# (<class '__main__.D'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)

class E(A, B):
    def metod(self):
        print('Metoda z klasy E')


e = E()
e.metod()  # Metoda z klasy E


class F(A, B):
    def metod(self):
        B.metod(self)


f = F()
f.metod()  # Metoda z klasy B


class G(A, B):
    def metod(self):
        super().metod()
        print("Dopisane")


g = G()
g.metod()


# Metoda z klasy A
# Dopisane

class H(A, B):
    def metod(self):
        # super zawsze bierze z pierwszej narzędnej - wskazuje __mro__
        super().metod()

    def metod_B(self):
        B.metod(self)
        print("dopisane")

h = H()
h.metod_B()
h.metod()
# Metoda z klasy B
# dopisane
# Metoda z klasy A
