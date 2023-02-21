#name              Crypstocker
#author            IamKrytas
#language          Python3
#version           0.2.2
#update            28.10.2022
#changelog         Wyswietlanie wartosci i nazwy danej kryptowaluty w formie tekstu czytanego
#description       Program pobierajacy kursy kryptowalut z zapiem do pliku wraz z data i godzina

import os
import time
import datetime
from pycoingecko import CoinGeckoAPI

def pobieranie():
    czas=datetime.datetime.now()
    plik.write(str(czas) + "\n")
    cg=CoinGeckoAPI()
    dane=cg.get_price(ids=Kwaluta, vs_currencies=Rwaluta)
    tablica = [dane]
    wyniktemp = dane[Kwaluta][Rwaluta]
    wynik = str(wyniktemp)
    print("Kryptowaluta " + Kwaluta + " kosztuje " + wynik + " " + Rwaluta)
    plik.write(str(tablica) + "\n"+ "\n")

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

if __name__ == '__main__':
    os.system("cls")
    plik = open("log.txt","a")
    Kwaluta = input("Podaj pelna nazwe kryptowaluty: ")
    Rwaluta = input("Podaj skrot oznaczenie waluty swiatowej: ")
    ilosc = int(input("Podaj ilosc pobran: "))
    sekundy = int(input("Podaj ilosc sekund pomiedzy pobraniami: "))
    wykonanie()
