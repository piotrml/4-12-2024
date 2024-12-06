from http.client import responses

import requests

url = "https://api.nbp.pl/api/exchangerates/rates/A/USD/"

response = requests.get(url)
print(response)
print(response.text)

# <Response [200]>
# {"table":"A","currency":"dolar amerykański","code":"USD","rates":[{"no":"237/A/NBP/2024","effectiveDate":"2024-12-06","mid":4.0341}]}
data = response.json()
print(data)
# {'table': 'A', 'currency': 'dolar amerykański', 'code': 'USD', 'rates': [{'no': '237/A/NBP/2024', 'effectiveDate': '2024-12-06', 'mid': 4.0341}]}
print(data['rates'])
# [{'no': '237/A/NBP/2024', 'effectiveDate': '2024-12-06', 'mid': 4.0341}]
print(data['rates'][0])
# bo to lista wobec czego wybrać pierwszy element listy
# {'no': '237/A/NBP/2024', 'effectiveDate': '2024-12-06', 'mid': 4.0341}
print(data['rates'][0]['mid'])
# i pobieramy klucz mid
# 4.0341