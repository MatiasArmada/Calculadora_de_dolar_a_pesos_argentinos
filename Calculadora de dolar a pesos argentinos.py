from tkinter import *
from tkinter import ttk, messagebox
import requests
class Aplicacion():
    __ventana=None
    __pulgadas=None
    __centimetros=None
    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.geometry('290x115')
        self.__ventana.title('Conversor Pulgadas a Centímetros')
        mainframe = ttk.Frame(self.__ventana, padding="5 5 12 5")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)
        mainframe['borderwidth'] = 2
        mainframe['relief'] = 'sunken'
        self.__dolares = DoubleVar()
        self.__argentinos = DoubleVar()
        self.__dolares.trace('w', self.calcular)
        self.dolaresEntry = ttk.Entry(mainframe, width=7, textvariable=self.__dolares)
        self.dolaresEntry.grid(column=2, row=1, sticky=(W, E))
        ttk.Label(mainframe, textvariable=self.__argentinos).grid(column=2, row=2, sticky=(W, E))
        ttk.Button(mainframe, text='Salir', command=self.__ventana.destroy).grid(column=3, row=3, sticky=W)
        ttk.Label(mainframe, text="dolares").grid(column=3, row=1, sticky=W)
        ttk.Label(mainframe, text="es equivalente a").grid(column=1, row=2, sticky=E)
        ttk.Label(mainframe, text="argentinos").grid(column=3, row=2, sticky=W)
        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)
        self.dolaresEntry.focus()
        self.__ventana.mainloop()
    def calcular(self, *args):
        complete_url = 'https://www.dolarsi.com/api/api.php?type=dolar'
        r = requests.get(complete_url)
        dic= r.json()
        try:
            i= 0
            while (i <= len(dic) and dic[i]['casa']['nombre'].lower() != 'oficial'):
                i+=1
            if i <= len(dic):
                valDolarF= float(str(dic[i]['casa']['venta']).replace(",","."))            
                d= float(self.__dolares.get())
                arg= float(d * valDolarF)
                self.__argentinos.set(arg)
        except IndexError:
            messagebox.showerror(title='Error', message='Valor no encontrado')
            self.__dolares.set('0')
            self.dolarEntry.focus()
        
def testAPP():
    mi_app = Aplicacion()
if __name__ == '__main__':
    testAPP()