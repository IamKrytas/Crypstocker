#name              Crypstocker
#author            IamKrytas
#language          Python3
#version           0.2.3
#update            17.11.2022
#changelog         Zmiana wartosci wyswietlanych i zapisywanych
#description       Program pobierajacy kursy kryptowalut z zapiem do pliku wraz z data i godzina

import os
import time
import datetime
from pycoingecko import CoinGeckoAPI

def pobieranie():
    czas=datetime.datetime.now()
    data=czas.strftime("%Y"+"-"+"%m"+"-"+"%d"+" "+"%H"+":"+"%M")
    cg=CoinGeckoAPI()
    dane=cg.get_price(ids=Kwaluta, vs_currencies=Rwaluta)
    cena = dane[Kwaluta][Rwaluta]
    wynik = str(cena)
    plik.write(str(wynik+","+data+"\n"))
    print(Kwaluta+" "+wynik+" "+Rwaluta+"\n")

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
