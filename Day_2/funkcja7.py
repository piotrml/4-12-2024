# przyklady dekoratorów

def dekor_wielka(fun):

    def wielka():
        wynik = fun().upper()
        return wynik
    return wielka


def red_dec(fun):
    def wrapper(*args, **kwargs):
        result = fun(*args, **kwargs)
        return "\033[91m" + result +  "\033[0m"
    return wrapper

@dekor_wielka
@ red_dec
def greeting():
    return "Hello World!!!"
print(greeting())


