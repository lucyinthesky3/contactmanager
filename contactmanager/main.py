import tkinter as tk

from okviri.framemanager import FrameManager
from okviri.okvir_firme import OkvirFirme
from okviri.okvir_nova_firma import OkvirNovaFirma
from okviri.okvir_zaglavlje import OkvirZaglavlje
from okviri.okvir_zaposlenici import OkvirZaposlenici
from okviri.okvir_novi_zaposlenik import OkvirNoviZaposlenik



root = tk.Tk()
root.geometry("1200x600+300+100")
root.title("Contact Manager")
root.grid_columnconfigure(0, weight=1)


###################################################
# Kreiranje okvira 

frm_zaglavlje = OkvirZaglavlje(root, height=120, padx=15, pady=15)#, bg="green")
FrameManager.dodaj_okvir("okvir_zaglavlje", frm_zaglavlje)

frm_firme = OkvirFirme(root, height=480, padx=15, pady=15)#, bg="blue")
FrameManager.dodaj_okvir("okvir_firme", frm_firme)

frm_nova_firma = OkvirNovaFirma(root, height=480, padx=15, pady=15)#, bg="red")
FrameManager.dodaj_okvir("okvir_nova_firma", frm_nova_firma)

frm_zaposlenici = OkvirZaposlenici(root, height=480, padx=15, pady=15)#, bg="blue")
FrameManager.dodaj_okvir("okvir_zaposlenici", frm_zaposlenici)

frm_novi_zaposlenik = OkvirNoviZaposlenik(root, height=480, padx=15, pady=15)#, bg="red")
FrameManager.dodaj_okvir("okvir_novi_zaposlenik", frm_novi_zaposlenik)

#print(FrameManager.okviri)

#prebacuje inicijalno u prvi plan početni okvir
FrameManager.prikazi_okvir("okvir_firme")

root.mainloop()