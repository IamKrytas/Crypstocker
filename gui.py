#name              Crypstocker-gui
#author            IamKrytas
#language          Python3
#version           0.1.0
#update            21.02.2023
#changelog         Zainicjowanie wstepnej wersji gui
#description       Interfejs graficzny crypstocker


import tkinter as tk
import tkinter.font as tkFont
import tkinter.ttk as ttk

class App:
    def __init__(self, root):
        self.Wartosc1 = ''
        self.Wartosc2 = ''
        root.title("xxxxxxxxx")
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
        napis.place(x=60,y=10,width=200,height=40)

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

        przycisk=tk.Button(root)
        przycisk["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        przycisk["font"] = ft
        przycisk["fg"] = "#000000"
        przycisk["justify"] = "center"
        przycisk["text"] = "Pobierz"
        przycisk.place(x=90,y=220,width=145,height=56)
        przycisk["command"] = self.pobierz

        przyciskDB=tk.Button(root)
        przyciskDB["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        przyciskDB["font"] = ft
        przyciskDB["fg"] = "#000000"
        przyciskDB["justify"] = "center"
        przyciskDB["text"] = "DB"
        przyciskDB.place(x=280,y=10,width=50,height=50)
        przyciskDB["command"] = self.przyciskDB_command 

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


    def przyciskDB_command(self):
        print("Dodano do bazy")

    def przycisk_command(self):
        print("Pobrano dane")

    def on_select_changed1(self, event):
        pass

    def on_select_changed2(self, event):
        pass

    def pobierz(self):
        pass
    
#event.widget.get() # zwraca wartość zaznaczenia
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
