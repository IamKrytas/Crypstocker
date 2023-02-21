#name              Crypstocker
#author            IamKrytas
#language          Python3
#version           0.3.2
#update            08.12.2022
#changelog         Dodanie warunku dla zamkniecia pliku
#description       Program pobierajacy kursy kryptowalut z zapiem do pliku wraz z data i godzina oraz tworzeniem wykresu

import os
import time
import datetime
from pycoingecko import CoinGeckoAPI
import matplotlib.pyplot as plt

def pobieranie():
    czas=datetime.datetime.now()
    data=czas.strftime("%Y"+"-"+"%m"+"-"+"%d"+" "+"%H"+":"+"%M")
    cg=CoinGeckoAPI()
    dane=cg.get_price(ids=Kwaluta, vs_currencies=Rwaluta)
    cena = dane[Kwaluta][Rwaluta]
    wynik = str(cena)
    plik.write(str(wynik+","+data+"\n"))
    if plik.closed==False:
        plik.close()
    print(Kwaluta+" "+wynik+" "+Rwaluta+"\n")
    wartosc=[]
    daty=[]
    otworz = open("log.txt", "r")
    for row in otworz:
        row=row.split(",")
        wartosc.append(int(row[0]))
        daty.append(str(row[1]))
    plt.plot(daty, wartosc)
    plt.xlabel('Daty', fontsize = 12)
    plt.ylabel('Wartość', fontsize = 12)
    plt.title('Wykres '+Kwaluta, fontsize = 20)
    plt.savefig("fig1.jpg", dpi = 72)   
    plt.show()
    if otworz.closed==False:
        otworz.close()

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
