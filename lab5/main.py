# import requests



# def prelicz(kwota:float, waluta_z:str, waluta_na:str, ) -> float:
#     url = f"https://v6.exchangerate-api.com/v6/563075f9e11695fd9ef35c70/latest/{waluta_z}"
#     response = requests.get(url)
#     lista_walut = response.json()['conversion_rates']
#     wynik = kwota * lista_walut[waluta_na]
#     return wynik


# print(prelicz(100, 'USD', 'PLN'))

# import random



# print(random.randint(1,100))


# fruits = ['apple', 'banana', 'orange']
# print(random.choice(fruits))


# numbers = [1, 2, 3, 4, 5]
# random.shuffle(numbers)
# print(numbers)


import time 
print(time.time())

import datetime
now = datetime.datetime.now()
print(now)


todays_date = datetime.date.today()
print(todays_date)


print(datetime.date.fromtimestamp(10000000).year)

a = datetime.datetime(2022, 12, 28, 23, 55, 59, 342380)
print(a)


# import os
# for file in os.listdir():
#     print(file)

# file_path = "main.py"
# if os.path.exists(file_path):
#     print('file already exists')

# print(os.path.isfile(file_path))

#print(os.listdir('test'))

#os.rename(file_path, file_path + "nowy_plik.txt")

# os.mkdir("nowy_katalog")
# time.sleep(5)
# os.rmdir("nowy_katalog")







