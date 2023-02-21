#name              Crypstocker
#author            IamKrytas
#language          Python3
#version           0.1.0
#update            12.09.2022
#changelog         Dodanie możliwości wprowadzania przez użytkownika kryptowaluty do pobrania
#description       Program pobierajacy kursy kryptowalut z zapiem do pliku wraz z data i godzina

import os
import time
import datetime
from pycoingecko import CoinGeckoAPI

os.system("cls")
plik = open("log.txt","a")
Kwaluta = input("Podaj pelna nazwe kryptowaluty: ")
Rwaluta = input("Podaj skrot oznaczenie waluty swiatowej: ")
ilosc = int(input("Podaj ilosc pobran: "))
sekundy = int(input("Podaj ilosc sekund pomiedzy pobraniami: "))

krok = 1
while krok<=ilosc:
    czas=datetime.datetime.now()
    plik.write(str(czas) + "\n")
    cg=CoinGeckoAPI()
    x=cg.get_price(ids=Kwaluta, vs_currencies=Rwaluta)
    print(x)
    plik.write(str(x) + "\n"+ "\n")
    time.sleep(sekundy)
    krok=krok+1
