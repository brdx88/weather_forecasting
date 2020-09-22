# -*- coding: utf-8 -*-
"""prakiraan_cuaca_brianic.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Vz13uHoJH_SAMTyF2wfeEychne6nXvlD
"""

import requests

api = "f577921cfdc4c6945545b4cfb08e7cae"
host = "api.openweathermap.org"
city_name = input("Masukkan nama kota: ")

url = f"http://{host}/data/2.5/weather?q={city_name}&appid={api}"
data = requests.get(url)
cuaca = data.json()
print('\n')
print(f"===== PRAKIRAAN CUACA HARI INI DI {city_name.upper()} =====")
# print(len(cuaca))
# kalau error, jmlh 'key' cuma ada 2. normalnya ada 13 'key'.
if len(cuaca) == 13:
  print(f"Kota yang Anda pilih: {cuaca['name']}")
  print(f"Suhu: {(cuaca['main']['temp'] - 273.15):.1f} Celcius")
  print(f"Keadaan cuaca: {cuaca['weather'][0]['main']}")
  print(f"Koordinat kota Anda: {cuaca['coord']['lat']}, {cuaca['coord']['lon']}")
  print(f"Tingkat kelembapan: {cuaca['main']['humidity']}%")
  print(f"Kecepatan angin: {cuaca['wind']['speed']} km/h")
else:
  print("Kota yang Anda masukkan tidak terdaftar.")