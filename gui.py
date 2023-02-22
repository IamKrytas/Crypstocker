#name              Crypstocker-gui
#author            IamKrytas
#language          Python3
#version           0.1.1
#update            22.02.2023
#changelog         Zaimplementowanie funkcji i 
#description       Interfejs graficzny crypstocker

import crypstocker
import tkinter as tk
import tkinter.font as tkFont
import tkinter.ttk as ttk
from tkinter import messagebox

class App:
    def __init__(self, root):
        self.Kwaluta = ''
        self.Rwaluta = ''

        root.title("Crypstocker")
        width=350
        height=320
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        napis=tk.Label(root)
        ft = tkFont.Font(family='Times',size=22)
        napis["font"] = ft
        napis["fg"] = "#333333"
        napis["justify"] = "center"
        napis["text"] = "Wybierz z list"
        napis.place(x=60,y=10,width=220,height=40)

        napis1=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        napis1["font"] = ft
        napis1["fg"] = "#333333"
        napis1["justify"] = "center"
        napis1["text"] = "Kryptowaluta"
        napis1.place(x=65,y=60,width=80,height=20)

        napis2=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        napis2["font"] = ft
        napis2["fg"] = "#333333"
        napis2["justify"] = "center"
        napis2["text"] = "Waluta"
        napis2.place(x=220,y=60,width=60,height=20)

        pobierz=tk.Button(root)
        pobierz["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        pobierz["font"] = ft
        pobierz["fg"] = "#000000"
        pobierz["justify"] = "center"
        pobierz["text"] = "Pobierz"
        pobierz.place(x=90,y=220,width=145,height=56)
        pobierz["command"] = self.pobierz

        lista1=tk.Listbox(root)
        lista1.cb_value = tk.StringVar()
        lista1.combobox = ttk.Combobox(root, textvariable = lista1.cb_value)
        lista1.combobox.place(x = 30, y = 80)
        lista1.combobox['values'] = ('Bitcoin', 'Litecoin', 'Ethereum')
        lista1.combobox.current(0)
        lista1.combobox.bind("<<ComboboxSelected>>", self.on_select_changed1)

        lista2=tk.Listbox(root)
        lista2.cb_value = tk.StringVar()
        lista2.combobox = ttk.Combobox(root, textvariable = lista2.cb_value)
        lista2.combobox.place(x = 180, y = 80)
        lista2.combobox['values'] = ('pln', 'usd', 'eur')
        lista2.combobox.current(0)
        lista2.combobox.bind("<<ComboboxSelected>>", self.on_select_changed2)


    def przycisk_command(self):
        print("Pobrano dane")


    def on_select_changed1(self, event):
        self.Kwaluta = event.widget.get() # zwraca wartość zaznaczenia
        self.Kwaluta = self.Kwaluta.lower()
        print(self.Kwaluta)

    def on_select_changed2(self, event):
        self.Rwaluta = event.widget.get() # zwraca wartość zaznaczenia
        self.Rwaluta = self.Rwaluta.lower()
        print(self.Rwaluta)

    def pobierz(self):
        if(self.Kwaluta == '' or self.Rwaluta == ''):
            messagebox.showerror("Błąd", "Wybierz kryptowalutę i walutę")
        else:
            print(f"Pobrano dane dla {self.Kwaluta} w {self.Rwaluta}")
            crypstocker.insert(self.Kwaluta, self.Rwaluta)
            crypstocker.wykres(self.Kwaluta, self.Rwaluta)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
