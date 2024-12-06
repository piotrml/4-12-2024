class DefaultDict(dict):
    def __missing__(self, key):
        return "default"


class AutoKeyDict(dict):
    """
    doda nam klucz jeżeli go nie ma
    """

    def __missing__(self, key):
        self[key] = 0
        return key


class CaseInsensitiveDict(dict):
    def __missing__(self, key):
        return self.get(key.casefold())


d_python = {}
d1 = DefaultDict()
print(d1)  # {}
print(type(d1))  # <class '__main__.DefaultDict'>
print(d1['name'])  # default

d2 = AutoKeyDict()
print(d2['name'])  # name
print(d2)  # {'name': 0}
print(d2['name'])  # 0
print(d2['name'])  # 0
cid = CaseInsensitiveDict()
cid['name'] = "Radek"
print(cid['Name'])  # Radek
cid['Name'] = "Tomek"
print(cid['Name'])  # Tomek
print(cid)  # {'name': 'Radek', 'Name': 'Tomek'}
