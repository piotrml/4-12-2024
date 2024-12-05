# funkcja wewnętrzna
# dekorator - funkcja która jako argument przyjmuje inną funkcję i dodaje nową funkcjonalność

def fun1():
    print("To jest fun1")

    def fun2():
        print("To jest fun2")

    return fun2


fun1()
print(fun1())  # <function fun1.<locals>.fun2 at 0x0000024A08955BC0>
print(type(fun1()))  # <class 'function'>
funkcja = fun1()
funkcja()  # To jest fun2


# arg - zapis, odczyt
def plik(arg):
    print("Sprawdzam czy jest plik")

    def zapis():
        print("Zapisałem plik")

    def odczyt():
        print("Odczytałem z pliku")

    if arg == 'zapis':
        return zapis  # zwraca adres funkcji
    else:
        return odczyt


zapis_pliku = plik("zapis")
zapis_pliku()
zapis_pliku()
odczyt_pliku = plik("odczyt")
odczyt_pliku()

fh = open('test.txt','w')
fh.write("Zapisano\n")
fh.close()