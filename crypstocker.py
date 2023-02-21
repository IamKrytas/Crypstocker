#Temp_name         Crypstocker
#author            IamKrytas
#version           0.0.1
#description       Program pobierajacy kursy kryptowalut z zapiem do pliku wraz z data i godzina

import os
import time
import datetime
from pycoingecko import CoinGeckoAPI
os.system("cls")
plik=open("log.txt","a")

ilosc = int(input("Podaj ilosc: "))
sekundy = int(input("Podaj ilosc sekund: "))

krok=0
while krok<ilosc:
    czas=datetime.datetime.now()
    plik.write(str(czas) + "\n")
    cg=CoinGeckoAPI()
    x=cg.get_price(ids=['bitcoin', 'ethereum', 'ripple',], vs_currencies='pln')
    plik.write(str(x) + "\n"+ "\n")
    time.sleep(sekundy)
    krok=krok+1
