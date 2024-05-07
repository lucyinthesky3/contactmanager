import tkinter as tk
from okviri.framemanager import FrameManager

import sqlalchemy as db
from sqlalchemy.orm import sessionmaker

from db.dbManager import Tvrtka, Zaposlenik, db_engine

Session = sessionmaker(bind=db_engine)
session = Session()

class OkvirZaposlenici(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        #self.master = master
        self.create_widgets()

    def create_widgets(self):

        self.grid(row=1, column=0, sticky="we")
        self.grid_propagate(False)

        # Konfigurira tri jednako široka stupca
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)


        # Oznaka naslova postavljena u čeliju 0,0 ali širine tri čelije (columnspan)
        lbl_naslov_A = tk.Label(self, text="Popis svih zaposlenika firme:")
        lbl_naslov_A.grid(row=0, column=0, padx=15, pady=25, columnspan=3)

        self.prikazi_sve_zaposlenike()

    
    def prikazi_sve_zaposlenike(self):

        for widget in self.winfo_children():
            #print("Klasa widgeta:", widget.winfo_class())
            #print("Ime widgeta:", widget.winfo_name())
            if widget.winfo_name()[:10] == "lbl_zaposl" or widget.winfo_name()[:10] == "btn_zaposl":
                widget.destroy()
                #print("BRISEM lbl_tvrtka ili btn_tvrtka")

        if Tvrtka.odabrana_tvrtka:
            zaposlenici = Tvrtka.odabrana_tvrtka.vrati_sve_zaposlenike_tvrtke()

            brojac = 4

            for zaposlenik in zaposlenici:
                opis_zaposlenika = str(zaposlenik.id) + " " + zaposlenik.ime + " " + zaposlenik.prezime  + ", " + zaposlenik.adresa + ", " + zaposlenik.oib

                lbl_zaposlenik = tk.Label(self, text=opis_zaposlenika, name="lbl_zaposlenik"+str(zaposlenik.id))
                lbl_zaposlenik.grid(row=brojac, column=0, sticky="w")

                if Zaposlenik.odabrani_zaposlenik and Zaposlenik.odabrani_zaposlenik.id == zaposlenik.id:
                    print("ZAPOSLENIK ID", Zaposlenik.odabrani_zaposlenik.id)
                    lbl_zaposlenik.configure(bg=FrameManager.boja_aktivnog_zapisa)

                #brisanje
                #btn_tvrtka_brisi = tk.Button(self, text="Brisanje", name="btn_tvrtka"+str(tvrtka.id), command=lambda id=tvrtka.id: Tvrtka.izbrisi_tvrtku(id))
                #btn_tvrtka_brisi.grid(row=brojac, column=1, sticky="w")
                
                # ili odabir tvrtke
                btn_tvrtka_odaberi = tk.Button(self, text="Odaberi", name="btn_zaposl"+str(zaposlenik.id))#, command=lambda id=zaposlenik.id: Zaposlenik.odaberi_zaposlenika(id))
                btn_tvrtka_odaberi.grid(row=brojac, column=1, sticky="w")
                brojac += 1