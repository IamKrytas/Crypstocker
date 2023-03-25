#name              Crypstocker-gui
#author            IamKrytas
#language          Python3
#version           0.2.0
#update            25.03.2023
#changelog         Dodanie nowego okna z ustawieniami wykresu (wstepna wersja)
#description       Interfejs graficzny crypstocker

import crypstocker
import tkinter as tk
import tkinter.font as tkFont
import tkinter.ttk as ttk
from tkinter import messagebox

class App:
    def __init__(self, root):
        self.cryptocurrency = ''
        self.currency = ''

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
        lista1.combobox.set('wybierz')
        lista1.combobox.place(x = 30, y = 80)
        lista1.combobox['values'] = ('Bitcoin', 'Litecoin', 'Ethereum')
        lista1.combobox.bind("<<ComboboxSelected>>", self.on_select_changed1)

        lista2=tk.Listbox(root)
        lista2.cb_value = tk.StringVar()
        lista2.combobox = ttk.Combobox(root, textvariable = lista2.cb_value)
        lista2.combobox.set('wybierz')
        lista2.combobox.place(x = 180, y = 80)
        lista2.combobox['values'] = ('pln', 'usd', 'eur')
        lista2.combobox.bind("<<ComboboxSelected>>", self.on_select_changed2)


    def on_select_changed1(self, event):
        self.cryptocurrency = event.widget.get()
        self.cryptocurrency = self.cryptocurrency.lower()
        #print(self.cryptocurrency)

    def on_select_changed2(self, event):
        self.currency = event.widget.get()
        self.currency = self.currency.lower()
        #print(self.currency)


    def pobierz(self):
        if(self.cryptocurrency == '' or self.currency == ''):
            messagebox.showerror("Błąd", "Wybierz kryptowalutę i walutę")
        else:
            crypstocker.insert(self.cryptocurrency, self.currency)
            #new window with settings for chart
            #TODO: Create new class for this window
            newWindow = tk.Toplevel(root)
            newWindow.title("Ustawienia wykresu")
            newWindow.geometry("300x200")
            newWindow.resizable(width=False, height=False)
            newLabel = tk.Label(newWindow, text="Wybierz zakres")

            enterbox=tk.Entry(newWindow)
            enterbox["borderwidth"] = "1px"
            ft = tkFont.Font(family='Times',size=10)
            enterbox["font"] = ft
            enterbox["fg"] = "#333333"
            enterbox["justify"] = "center"
            enterbox["text"] = "Entry"
            enterbox.place(x=120,y=50,width=50,height=50)
            self.enterbox = enterbox

            display_chart_btn=tk.Button(newWindow)
            display_chart_btn["bg"] = "#f0f0f0"
            ft = tkFont.Font(family='Times',size=10)
            display_chart_btn["font"] = ft
            display_chart_btn["fg"] = "#000000"
            display_chart_btn["justify"] = "center"
            display_chart_btn["text"] = "Button"
            display_chart_btn.place(x=140,y=150,width=50,height=50)
            display_chart_btn["command"] = self.display_chart_btn_command
            #TODO: Add other labels and events

    #funkcja sprawdza czy podana wartosc to liczba dwucyfrowa z przedzialu 1-10
    def validate_enter(self):
        if self.enterbox.get().isdigit() and 0 < int(self.enterbox.get()) <= 10:
            return self.enterbox.get()
        else:
            messagebox.showerror("Błąd", "Liczba musi być w zakresie 1-10")
            self.enterbox.delete(0, tk.END)
            return 0
                    
    def display_chart_btn_command(self):
        if(self.validate_enter() != 0):
            crypstocker.wykres(self.cryptocurrency, self.currency, self.validate_enter())
        #print(self.validate_enter())
            
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
