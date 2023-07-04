#name              Crypstocker
#author            IamKrytas
#language          Python3
#version           0.5.1
#update            04.07.2023
#changelog         Add annotations to all functions
#description       Cryptocurrency tracking program

import os
import datetime
import sqlite3
import matplotlib.pyplot as plt
from pycoingecko import CoinGeckoAPI
from sklearn.linear_model import LinearRegression

def main():
    """
    os.system('cls')
    cryptocurrency = input("Enter the full name of the cryptocurrency: ").lower()
    currency = input("Enter the short form of the world currency: ").lower()
    insert(cryptocurrency,currency
    #save_txt(cryptocurrency, currency)""
    """

def download(cryptocurrency: str, currency: str) -> int:
    try:
        cg=CoinGeckoAPI()
        value=cg.get_price(ids=cryptocurrency, vs_currencies=currency)
        price = value[cryptocurrency][currency]
        print(price)
        return price
    except:
        print("Error! Check your internet connection or try again later")

def save_txt(cryptocurrency: str, currency: str):
    date=datetime.datetime.now().strftime(f"%Y-%m-%d %H:%M")
    price=str(download())
    with open("crypto.txt", "a") as file:
        file.write(f"{cryptocurrency},{price},{currency},{date}\n")
    #print(f"{cryptocurrency},{price},{currency},{date}\n")

def chart(cryptocurrency: str, currency: str, range: int, ifprediction: int):
    conn=sqlite3.connect('crypto.db')
    conn.row_factory=sqlite3.Row
    cur=conn.cursor()
    cur.execute(f"SELECT * FROM crypto WHERE Cryptocurrency='{cryptocurrency}' AND Currency='{currency}' ORDER BY id DESC LIMIT {range}")
    conn.commit()
    dane = cur.fetchall()
    x=[]
    y=[]
    prediction = predict(cryptocurrency, currency)
    for row in dane:
        x.append(row['date'])
        y.append(row['value'])
    x.reverse()
    y.reverse()
    x.append(prediction[1])
    y.append(prediction[0])

    plt.scatter(x[:-2], y[:-2], marker='o', s=50, color='blue')
    plt.scatter(x[-2], y[-2], marker='o', s=50, color='blue')
    if ifprediction == 1:
        plt.scatter(x[-1], y[-1], marker='o', s=50, color='red')
        plt.plot(x, y, 'k-', linewidth=2)
    else:
        plt.plot(x[:-1], y[:-1], 'k-', linewidth=2)
    plt.xticks([x[0],x[-2]], visible=True)
    plt.xlabel('Date', fontsize=10)
    plt.ylabel(f'Value in {currency}', fontsize=10)
    plt.title(f'Chart {cryptocurrency}', fontsize=20)
    plt.savefig("fig1.jpg", dpi=72)
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

def insert(cryptocurrency: str, currency: str):
    date=datetime.datetime.now().strftime(f"%Y-%m-%d %H:%M")
    value = download(cryptocurrency, currency)
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
    cur.execute(f"SELECT * FROM crypto")
    conn.commit()
    data = cur.fetchall()
    for row in data:
        print(row['id'], row['Cryptocurrency'], row['value'], row['Currency'], row['date'])
    conn.close()

def predict(cryptocurrency: str, currency: str) -> list:
        conn=sqlite3.connect('crypto.db')
        conn.row_factory=sqlite3.Row
        cur=conn.cursor()
        cur.execute(f"SELECT * FROM crypto WHERE Cryptocurrency='{cryptocurrency}' AND Currency='{currency}' ORDER BY id DESC")
        conn.commit()
        dane = cur.fetchall()
        x=[]
        for row in dane:
            x.append(row['value'])
        x.reverse()
        print(x)
        model = LinearRegression()
        model.fit([[i] for i in range(len(x))], x)
        result = model.predict([[len(x) + 1]])[0].round(0)
        print(f"Predicted price for {cryptocurrency} in {currency} is {result}")
        conn.close()
        date=datetime.datetime.now().strftime(f"%Y-%m-%d %H:%M:%S")
        return [result, date]

if __name__ == '__main__':
    main()
