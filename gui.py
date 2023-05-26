#name              Crypstocker-gui
#author            IamKrytas
#language          Python3
#version           0.3.0
#update            26.05.2023
#changelog         Add checkbox and change position of elements in settings chart window
#description       Gui for Crypstocker

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

        label1=tk.Label(root)
        ft = tkFont.Font(family='Times',size=22)
        label1["font"] = ft
        label1["fg"] = "#333333"
        label1["justify"] = "center"
        label1["text"] = "Choose from lists"
        label1.place(x=60,y=10,width=220,height=40)

        label2=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        label2["font"] = ft
        label2["fg"] = "#333333"
        label2["justify"] = "center"
        label2["text"] = "Cryptocurrency"
        label2.place(x=55,y=60,width=100,height=20)

        label3=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        label3["font"] = ft
        label3["fg"] = "#333333"
        label3["justify"] = "center"
        label3["text"] = "Currency"
        label3.place(x=220,y=60,width=60,height=20)

        download=tk.Button(root)
        download["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        download["font"] = ft
        download["fg"] = "#000000"
        download["justify"] = "center"
        download["text"] = "Download"
        download.place(x=90,y=220,width=145,height=56)
        download["command"] = self.download

        list1=tk.Listbox(root)
        list1.cb_value = tk.StringVar()
        list1.combobox = ttk.Combobox(root, textvariable = list1.cb_value)
        list1.combobox.set('wybierz')
        list1.combobox.place(x = 30, y = 80)
        list1.combobox['values'] = ('Bitcoin', 'Litecoin', 'Ethereum')
        list1.combobox.bind("<<ComboboxSelected>>", self.on_select_changed1)

        list2=tk.Listbox(root)
        list2.cb_value = tk.StringVar()
        list2.combobox = ttk.Combobox(root, textvariable = list2.cb_value)
        list2.combobox.set('wybierz')
        list2.combobox.place(x = 180, y = 80)
        list2.combobox['values'] = ('pln', 'usd', 'eur')
        list2.combobox.bind("<<ComboboxSelected>>", self.on_select_changed2)


    def on_select_changed1(self, event):
        self.cryptocurrency = event.widget.get()
        self.cryptocurrency = self.cryptocurrency.lower()
        #print(self.cryptocurrency)

    def on_select_changed2(self, event):
        self.currency = event.widget.get()
        self.currency = self.currency.lower()
        #print(self.currency)


    def download(self):
        if(self.cryptocurrency == '' or self.currency == ''):
            messagebox.showerror("Błąd", "Wybierz kryptowalutę i walutę")
        else:
            crypstocker.insert(self.cryptocurrency, self.currency)
            #new window with settings for chart
            #TODO: Create new class for this window
            newWindow = tk.Toplevel(root)
            newWindow.title("Chart settings")
            newWindow.geometry("300x300")
            newWindow.resizable(width=False, height=False)

            labelofrange=tk.Label(newWindow)
            ft = tkFont.Font(family='Times',size=12)
            labelofrange["font"] = ft
            labelofrange["fg"] = "#333333"
            labelofrange["justify"] = "center"
            labelofrange["text"] = "Insert range (1-10)"
            labelofrange.place(x=20,y=30,width=133,height=42)

            enterbox=tk.Entry(newWindow)
            enterbox["borderwidth"] = "1px"
            ft = tkFont.Font(family='Times',size=12)
            enterbox["font"] = ft
            enterbox["fg"] = "#333333"
            enterbox["justify"] = "center"
            enterbox["text"] = "Entry"
            enterbox.place(x=190,y=30,width=50,height=50)
            self.enterbox = enterbox

            display_chart_btn=tk.Button(newWindow)
            display_chart_btn["bg"] = "#f0f0f0"
            ft = tkFont.Font(family='Times',size=12)
            display_chart_btn["font"] = ft
            display_chart_btn["fg"] = "#000000"
            display_chart_btn["justify"] = "center"
            display_chart_btn["text"] = "Generate chart"
            display_chart_btn.place(x=80,y=200,width=140,height=56)
            display_chart_btn["command"] = self.display_chart_btn_command

            labelifprediction=tk.Label(newWindow)
            ft = tkFont.Font(family='Times',size=12)
            labelifprediction["font"] = ft
            labelifprediction["fg"] = "#333333"
            labelifprediction["justify"] = "center"
            labelifprediction["text"] = "prediction (yes/no)"
            labelifprediction.place(x=20,y=110,width=135,height=36)

            predictbox=tk.Checkbutton(newWindow)
            predictbox["anchor"] = "center"
            ft = tkFont.Font(family='Times',size=18)
            predictbox["font"] = ft
            predictbox["fg"] = "#333333"
            predictbox["justify"] = "center"
            predictbox["text"] = ""
            predictbox.place(x=180,y=100,width=71,height=61)
            predictbox["offvalue"] = "0"
            predictbox["onvalue"] = "1"
            predictbox["command"] = self.predictbox_command
            self.predictbox = tk.IntVar()
            predictbox["variable"] = self.predictbox
            #TODO: Add other labels and events
            

    def predictbox_command(self):
        pass
        #print(self.predictbox.get())
            
    #function checks if the given value is digit and number between 1-10
    def validate_enter(self):
        if self.enterbox.get().isdigit() and 0 < int(self.enterbox.get()) <= 10:
            return self.enterbox.get()
        else:
            messagebox.showerror("Error!", "The number must be in the range of 1-10")
            self.enterbox.delete(0, tk.END)
            return 0
                    
    def display_chart_btn_command(self):
        if(self.validate_enter() != 0):
            crypstocker.chart(self.cryptocurrency, self.currency, self.validate_enter())
        #print(self.validate_enter())
            
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
