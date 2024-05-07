class FrameManager:

    boja_aktivnog_zapisa = "lightgreen"

    okviri = {} # dictionary svih kreiranih okvira
    
    @staticmethod # slicno kao i classmethod dekorator ali se ne prenosi instanca klase (nema cls kao parametar)
    def dodaj_okvir(naziv, okvir):
        FrameManager.okviri.update({naziv: okvir})
        
    @staticmethod
    def prikazi_okvir(naziv_okvira):
        okvir = FrameManager.okviri.get(naziv_okvira)
        okvir.tkraise()

    @staticmethod
    def dohvati_okvir(naziv_okvira):
        return FrameManager.okviri.get(naziv_okvira)
        
    @staticmethod
    def dohvati_widget_iz_okvira(naziv_okvira, naziv_widgeta):
        dohvaceni_okvir = FrameManager.dohvati_okvir(naziv_okvira)
        for widget in dohvaceni_okvir.winfo_children():
            if widget.winfo_name() == naziv_widgeta:
                return widget
            
    @staticmethod
    def postavi_bg_boju_widgeta(naziv_okvira, naziv_widgeta, boja=None):
        dohvaceni_okvir = FrameManager.dohvati_okvir(naziv_okvira)
        for widget in dohvaceni_okvir.winfo_children():
            if widget.winfo_name() == naziv_widgeta:
                if boja:
                    widget.configure(bg=boja)
                else:
                    widget.configure(bg=widget.master.cget('bg'))
                    
    @staticmethod
    def postavi_bg_boju_grupe_widgeta(naziv_okvira, prefiks_grupe_widgeta, boja=None):
        dohvaceni_okvir = FrameManager.dohvati_okvir(naziv_okvira)
        for widget in dohvaceni_okvir.winfo_children():
            if widget.winfo_name()[:len(prefiks_grupe_widgeta)] == prefiks_grupe_widgeta:
                if boja:
                    widget.configure(bg=boja)
                else:
                    widget.configure(bg=widget.master.cget('bg'))

    @staticmethod
    def prikazi_grupu_widgeta(naziv_okvira, prefiks_grupe_widgeta, prikaz=True):
        dohvaceni_okvir = FrameManager.dohvati_okvir(naziv_okvira)
        for widget in dohvaceni_okvir.winfo_children():
            if widget.winfo_name()[:len(prefiks_grupe_widgeta)] == prefiks_grupe_widgeta:
                if prikaz:
                    widget.grid()
                else:
                    widget.grid_remove()

    