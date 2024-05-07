import tkinter as tk
from okviri.framemanager import FrameManager

import sqlalchemy as db
from sqlalchemy.orm import sessionmaker

from db.dbManager import Tvrtka, Zaposlenik, db_engine

Session = sessionmaker(bind=db_engine)
session = Session()

class OkvirNoviZaposlenik(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master
        self.create_widgets()# master)

    def create_widgets(self):#, master):
        
        def spremi_zaposlenika():
            ime = entry_ime.get()
            prezime = entry_prezime.get()
            adresa = entry_adresa.get()
            oib = entry_oib.get()
            if ime and prezime:
                zaposlenik = Zaposlenik(ime, prezime, adresa, oib, Tvrtka.odabrana_tvrtka.id)
                session.add(zaposlenik)
                session.commit()
                entry_ime.delete(0, "end")
                entry_prezime.delete(0, "end")
                entry_adresa.delete(0, "end")
                entry_oib.delete(0, "end")
                FrameManager.okviri.get("okvir_zaposlenici").prikazi_sve_zaposlenike()
            else:
                print("Nema podataka pri kreiranju nove tvrtke")




        self.grid(row=1, column=0, sticky="we")
        self.grid_propagate(False)

        self.grid_columnconfigure(0, weight=1)

        lbl_ime = tk.Label(self, text="Ime zaposlenika:")
        lbl_ime.grid(row=1, column=0, sticky="w")
        entry_ime = tk.Entry(self)
        entry_ime.grid(row=1, column=1)

        lbl_prezime = tk.Label(self, text="Prezime zaposlenika:")
        lbl_prezime.grid(row=2, column=0, sticky="w")
        entry_prezime = tk.Entry(self)
        entry_prezime.grid(row=2, column=1)

        lbl_adresa = tk.Label(self, text="Adresa zaposlenika:")
        lbl_adresa.grid(row=3, column=0, sticky="w")
        entry_adresa = tk.Entry(self)
        entry_adresa.grid(row=3, column=1)

        lbl_oib = tk.Label(self, text="OIB zaposlenika:")
        lbl_oib.grid(row=4, column=0, sticky="w")
        entry_oib = tk.Entry(self)
        entry_oib.grid(row=4, column=1)

        btn_spremi_tvrtku = tk.Button(self, text="Spremi zaposlenika", command= spremi_zaposlenika)
        btn_spremi_tvrtku.grid(row=4, column=0, columnspan=2) 