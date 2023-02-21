#name              Crypstocker
#author            IamKrytas
#language          Python3
#version           0.2.0
#update            19.09.2022
#changelog         Dodanie osobnych funkcji i poprawienie funkcjonowania programu
#description       Program pobierajacy kursy kryptowalut z zapiem do pliku wraz z data i godzina

import os
import time
import datetime
from pycoingecko import CoinGeckoAPI

def pobieranie():
    czas=datetime.datetime.now()
    plik.write(str(czas) + "\n")
    cg=CoinGeckoAPI()
    x=cg.get_price(ids=Kwaluta, vs_currencies=Rwaluta)
    print(x)
    plik.write(str(x) + "\n"+ "\n")

def spanie():
    time.sleep(sekundy)

def wykonanie():
    krok = 1
    spij=ilosc-1
    while krok<=ilosc:
        pobieranie()
        while(krok<=spij):
            spanie()
            break
        krok=krok+1

os.system("cls")
plik = open("log.txt","a")
Kwaluta = input("Podaj pelna nazwe kryptowaluty: ")
Rwaluta = input("Podaj skrot oznaczenie waluty swiatowej: ")
ilosc = int(input("Podaj ilosc pobran: "))
sekundy = int(input("Podaj ilosc sekund pomiedzy pobraniami: "))
wykonanie()
