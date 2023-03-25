#name              Crypstocker
#author            IamKrytas
#language          Python3
#version           0.4.7
#update            25.03.2023
#changelog         Zmiana funkcji wyświetlania wykresu
#description       Program do obserwowania kursu kryptowalut

import os
import datetime
import sqlite3
import matplotlib.pyplot as plt
from pycoingecko import CoinGeckoAPI

def pobierz(cryptocurrency, currency):
    cg=CoinGeckoAPI()
    value=cg.get_price(ids=cryptocurrency, vs_currencies=currency)
    price = value[cryptocurrency][currency]
    print(price)
    return price

def zapisz_txt(cryptocurrency, currency):
    date=datetime.datetime.now().strftime("%Y"+"-"+"%m"+"-"+"%d"+" "+"%H"+":"+"%M")
    price=str(pobierz())
    plik = open("log.txt","a")
    plik.write(f"{cryptocurrency},{price},{currency},{date}\n")
    if plik.closed==False:
        plik.close()
    #print(cryptocurrency+" "+price+" "+currency+"\n")

def wykres(cryptocurrency, currency, range):
    conn=sqlite3.connect('crypto.db')
    conn.row_factory=sqlite3.Row
    cur=conn.cursor()
    cur.execute(f"SELECT * FROM crypto WHERE Cryptocurrency='{cryptocurrency}' AND Currency='{currency}' ORDER BY id DESC LIMIT {range}")
    conn.commit()
    dane = cur.fetchall()
    x=[]
    y=[]
    for row in dane:
        x.append(row['date'])
        y.append(row['value'])
    x.reverse()
    y.reverse()
    plt.plot(x, y, linewidth=3, marker='o', markersize=5)
    plt.xticks([x[0],x[-1]], visible=True)
    plt.ticklabel_format(style='plain', axis='y')
    plt.xlabel('Daty', fontsize = 10)
    plt.ylabel(f'Wartość w {currency}', fontsize = 10)
    plt.title(f'Wykres {cryptocurrency}', fontsize = 20)
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
    date=datetime.datetime.now().strftime("%Y"+"-"+"%m"+"-"+"%d"+" "+"%H"+":"+"%M")
    value = pobierz(cryptocurrency, currency)
    create_table()
    conn=sqlite3.connect('crypto.db')
    conn.row_factory=sqlite3.Row
    cur=conn.cursor()
    cur.execute('INSERT INTO crypto VALUES (NULL,?,?,?,?)', (cryptocurrency, value, currency, date))
    conn.commit()
    conn.close()

def view_table():
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
    cryptocurrency = input("Podaj pelna nazwe kryptowaluty: ")
    currency = input("Podaj skrot oznaczenie waluty swiatowej: ")
    cryptocurrency = cryptocurrency.lower()
    currency = currency.lower()
    insert(cryptocurrency,currency)
    view_table()
    #zapisz_txt(cryptocurrency, currency)
    wykres(cryptocurrency, currency, 5)
