import tkinter as tk
from okviri.framemanager import FrameManager

from db.dbManager import Tvrtka, Zaposlenik, db_engine

class OkvirZaglavlje(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        #self.master = master
        self.create_widgets()

    def create_widgets(self):
        
        self.grid(row=0, column=0, sticky="we")
        self.grid_propagate(False)

        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)
        self.grid_columnconfigure(4, weight=1)
        self.grid_columnconfigure(5, weight=1)
        self.grid_columnconfigure(6, weight=1)


        lbl_poc_prazan = tk.Label(self, height="2", text="CONTACT MANAGER")
        lbl_poc_prazan.grid(row=1, column=1, columnspan=6)

        btn_zaglav_tvrtke = tk.Button(self, text="TVRTKE", command=lambda: FrameManager.prikazi_okvir("okvir_firme"))
        btn_zaglav_tvrtke.grid(row=2, column=2)

        btn_zaglav_nova_tvrtka = tk.Button(self, text="Nova tvrtka", command=lambda: FrameManager.prikazi_okvir("okvir_nova_firma"))
        btn_zaglav_nova_tvrtka.grid(row=3, column=1)

        if Tvrtka.odabrana_tvrtka:
            id_tvrtke = Tvrtka.odabrana_tvrtka.id
        else:
            id_tvrtke = 0
        btn_zaglavlje_tvrtka_brisanje = tk.Button(self, text="Brisanje tvrtke", name="btn_zaglavlje_tvrtka_brisanje", command=Tvrtka.izbrisi_odabranu_tvrtku)
        btn_zaglavlje_tvrtka_brisanje.grid(row=3, column=2)
        btn_zaglavlje_tvrtka_brisanje.grid_remove()

        btn_zaglavlje_tvrtka_promjena = tk.Button(self, text="Promjena tvrtke", name="btn_zaglavlje_tvrtka_promjena")#, command=lambda: FrameManager.prikazi_okvir("..."))
        btn_zaglavlje_tvrtka_promjena.grid(row=3, column=3)
        btn_zaglavlje_tvrtka_promjena.grid_remove()

        btn_zaglavlje_zaposlenici = tk.Button(self, text="ZAPOSLENICI", name="btn_zaglavlje_zaposlenici", command=lambda: FrameManager.prikazi_okvir("okvir_zaposlenici"))
        btn_zaglavlje_zaposlenici.grid(row=2, column=5)
        btn_zaglavlje_zaposlenici.grid_remove()

        btn_zaglavlje_zaposlenik_novi = tk.Button(self, text="Novi zaposlenik", name="btn_zaglavlje_zaposlenik_novi", command=lambda: FrameManager.prikazi_okvir("okvir_novi_zaposlenik"))
        btn_zaglavlje_zaposlenik_novi.grid(row=3, column=4)
        btn_zaglavlje_zaposlenik_novi.grid_remove()

        btn_zaglavlje_zaposlenik_brisanje = tk.Button(self, text="Brisanje zaposlenika", name="btn_zaglavlje_zaposlenik_brisanje")#, command=lambda: FrameManager.prikazi_okvir("..."))
        btn_zaglavlje_zaposlenik_brisanje.grid(row=3, column=5)
        btn_zaglavlje_zaposlenik_brisanje.grid_remove()

        btn_zaglavlje_zaposlenik_promjena = tk.Button(self, text="Promjena zaposlenika", name="btn_zaglavlje_zaposlenik_promjena")#, command=lambda: FrameManager.prikazi_okvir("..."))
        btn_zaglavlje_zaposlenik_promjena.grid(row=3, column=6)
        btn_zaglavlje_zaposlenik_promjena.grid_remove()