import tkinter as tk
from okviri.framemanager import FrameManager

import sqlalchemy as db
from sqlalchemy.orm import sessionmaker

from db.dbManager import Tvrtka, Zaposlenik, db_engine

Session = sessionmaker(bind=db_engine)
session = Session()

class OkvirNovaFirma(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master
        self.create_widgets()# master)

    def create_widgets(self):#, master):
        
        def spremi_tvrtku():
            naziv = entry_naziv.get()
            adresa = entry_adresa.get()
            oib = entry_oib.get()
            if naziv and oib and adresa:
                tvrtka = Tvrtka(naziv, adresa, oib)
                session.add(tvrtka)
                session.commit()
                entry_naziv.delete(0, "end")
                entry_adresa.delete(0, "end")
                entry_oib.delete(0, "end")
                FrameManager.okviri.get("okvir_firme").prikazi_sve_firme()
            else:
                print("Nema podataka pri kreiranju nove tvrtke")




        self.grid(row=1, column=0, sticky="we")
        self.grid_propagate(False)

        self.grid_columnconfigure(0, weight=1)

        lbl_naziv = tk.Label(self, text="Naziv tvrtke:")
        lbl_naziv.grid(row=1, column=0, sticky="w")
        entry_naziv = tk.Entry(self)
        entry_naziv.grid(row=1, column=1)

        lbl_adresa = tk.Label(self, text="Adresa tvrtke:")
        lbl_adresa.grid(row=2, column=0, sticky="w")
        entry_adresa = tk.Entry(self)
        entry_adresa.grid(row=2, column=1)

        lbl_oib = tk.Label(self, text="OIB tvrtke:")
        lbl_oib.grid(row=3, column=0, sticky="w")
        entry_oib = tk.Entry(self)
        entry_oib.grid(row=3, column=1)

        btn_spremi_tvrtku = tk.Button(self, text="Spremi tvrtku", command= spremi_tvrtku)
        btn_spremi_tvrtku.grid(row=4, column=0, columnspan=2) 