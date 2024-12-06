class MyException(Exception):
    def __init__(self,message):
        super().__init__(message)

# raise KeyError # KeyError

try:
    x = int(input("Podaj liczbę całkowitą "))
    if x<=0:
        raise MyException("Liczba musi być większa od zera")
except MyException as e:
    print("Wartość musi być większa od zera", e)
except Exception as e:
    print("Błąd, e")
else:
    print("Podana wartość prawidłowa:", x)
finally:
    print("Koniec")

# Podaj liczbę całkowitą 2.3
# Błąd, e
# Podaj liczbę całkowitą 3
# Podana wartość prawidłowa: 3
# Koniec
# Podaj liczbę całkowitą -2
# Wartość musi być większa od zera Liczba musi być większa od zera
# Koniec
