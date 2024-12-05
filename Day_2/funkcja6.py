# dekorator - funkcja, która jao argument przyjmuje funkcję
# dodaje, modyfikuje
# wykorzystuje mechanizm funkcji wewnętrznej

def dekor(fun):
    def wew():
        print("Dekorator. Dodatkowy napis")
        return fun()

    return wew

@dekor
def nasza_fun():
    print("Funkcja do udekorowania")

nasza_fun()