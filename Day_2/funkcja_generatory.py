# generator - generuje wartości w momencie kiedy je potrzebujemy

def kwadrat(n):
    for x in range(n):
        print(x ** 2)


kwadrat(5)


def kwadrat2(n):
    for x in range(n):
        yield x ** 2

kwa = kwadrat2(5)
print(kwa) # <generator object kwadrat2 at 0x000002CF3C7A3510>
print(type(kwa)) # <class 'generator'>

print(next(kwa))
print(next(kwa))
print(next(kwa))

kwa2 = kwadrat2(5)
kwa3 = kwadrat2(5)

print(next(kwa2))
print(next(kwa2))
print(next(kwa3))
print(next(kwa2))
print(next(kwa3))
print(next(kwa))

for i in kwadrat2(10):
    print(i)
# nie zostanie wygenerowany błąd jak zakończy się lista generatora