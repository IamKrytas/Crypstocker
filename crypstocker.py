#name              Crypstocker
#author            IamKrytas
#language          Python3
#version           0.4.3
#update            19.02.2023
#changelog         Zmiana wyswietlania wykresu
#description       Program do obserwowania kursu kryptowalut

import os
import datetime
import sqlite3
import matplotlib.pyplot as plt
from pycoingecko import CoinGeckoAPI

def pobierz():
    cg=CoinGeckoAPI()
    dane=cg.get_price(ids=Kwaluta, vs_currencies=Rwaluta)
    cena = dane[Kwaluta][Rwaluta]
    #print(cena)
    return cena

def zapisz_txt():
    czas=datetime.datetime.now()
    data=czas.strftime("%Y"+"-"+"%m"+"-"+"%d"+" "+"%H"+":"+"%M")
    cena=str(pobierz())
    plik = open("log.txt","a")
    plik.write(str(cena+","+data+"\n"))
    if plik.closed==False:
        plik.close()
    #print(Kwaluta+" "+cena+" "+Rwaluta+"\n")

def wykres():
    conn=sqlite3.connect('crypto.db')
    conn.row_factory=sqlite3.Row
    cur=conn.cursor()
    cur.execute(f"SELECT * FROM crypto WHERE Cryptocurrency='{Kwaluta}' AND Currency='{Rwaluta}' ORDER BY id DESC LIMIT 4")
    conn.commit()
    dane = cur.fetchall()
    x=[]
    y=[]
    for row in dane:
        x.append(row['date'])
        y.append(row['value'])
    x.reverse()
    y.reverse()
    plt.plot(x,y)
    plt.ticklabel_format(style='plain', axis='y')
    plt.xlabel('Daty', fontsize = 10)
    plt.ylabel(f'Wartość w {Rwaluta}', fontsize = 10)
    plt.title(f'Wykres {Kwaluta}', fontsize = 20)
    plt.savefig("fig1.jpg", dpi = 72) 
    plt.show()
    conn.close()

def create_table():
    conn=sqlite3.connect('crypto.db')
    conn.row_factory=sqlite3.Row
    cur=conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS crypto (id INTEGER PRIMARY KEY, Cryptocurrency TEXT, value FLOAT, Currency TEXT, date TEXT)')
    conn.commit()
    conn.close()

def drop_table():
    conn=sqlite3.connect('crypto.db')
    conn.row_factory=sqlite3.Row
    cur=conn.cursor()
    cur.execute('DROP TABLE crypto')
    conn.commit()
    conn.close()

def insert(cryptocurrency, currency):
    data=datetime.datetime.now().strftime("%Y"+"-"+"%m"+"-"+"%d"+" "+"%H"+":"+"%M")
    value = pobierz()
    conn=sqlite3.connect('crypto.db')
    conn.row_factory=sqlite3.Row
    cur=conn.cursor()
    cur.execute('INSERT INTO crypto VALUES (NULL,?,?,?,?)', (cryptocurrency, value, currency, data))
    conn.commit()
    conn.close()
    print("DATABASE UPDATED!")

def view():
    conn=sqlite3.connect('crypto.db')
    conn.row_factory=sqlite3.Row
    cur=conn.cursor()
    cur.execute('SELECT * FROM crypto')
    conn.commit()
    dane = cur.fetchall()
    for row in dane:
        print(row['id'], row['Cryptocurrency'], row['value'], row['Currency'], row['date'])
    conn.close()

if __name__ == '__main__':
    os.system('cls')
    Kwaluta = input("Podaj pelna nazwe kryptowaluty: ")
    Rwaluta = input("Podaj skrot oznaczenie waluty swiatowej: ")
    create_table()
    insert(Kwaluta,Rwaluta)
    view()
    #zapisz_txt()
    wykres()
