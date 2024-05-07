import sqlalchemy as db
from sqlalchemy.orm import sessionmaker, declarative_base

from okviri.framemanager import FrameManager

Base = declarative_base()

# otvara koenkciju prema bazi podataka
db_engine = db.create_engine('sqlite:///Baza.db')#, echo=True)
Session = sessionmaker(bind=db_engine)
session = Session()

class Tvrtka(Base):
    __tablename__ = "tvrtke"

    id = db.Column(db.Integer, primary_key=True)
    naziv = db.Column(db.String)
    adresa = db.Column(db.String)
    oib = db.Column(db.String)

    odabrana_tvrtka = None

    def __init__(self, naziv, adresa, oib):
        self.naziv = naziv
        self.adresa = adresa
        self.oib = oib

    def __str__(self):
        return("TVRTKA: " + " " + str(self.id) + " " + self.naziv + " " + self.adresa + " " + self.oib)
    
    def azuriraj_tvrtku(self):
        novo_ime = input("Unesi novi naziv (ostavi prazno za preskočiti): ")
        nova_adresa = input("Unesi novu adresu (ostavi prazno za preskočiti): ")
        novi_oib = input("Unesi novi OIB (ostavi prazno za preskočiti): ")

        if novo_ime:
            self.naziv = novo_ime
        if nova_adresa:
            self.adresa = nova_adresa
        if novi_oib:
            self.oib = novi_oib

        session.commit()


    @classmethod
    def ispisi_sve_tvrtke(cls):
        for tvrtka in session.query(cls).all():
            print(tvrtka)

    @classmethod
    def vrati_sve_tvrtke(cls):
        return session.query(cls).all()
                
    @classmethod
    def odaberi_tvrtku(cls, id_tvrtke):
        odabrana_tvrtka = session.query(Tvrtka).filter_by(id=id_tvrtke).one_or_none()
        if odabrana_tvrtka:
            cls.odabrana_tvrtka = odabrana_tvrtka

            # promjena boje labela u GUI-u
            FrameManager.postavi_bg_boju_grupe_widgeta("okvir_firme", "lbl_tvrtka")# Treci parametar je boja a ako ga nema postavlja se na default
            FrameManager.postavi_bg_boju_widgeta("okvir_firme", "lbl_tvrtka"+str(id_tvrtke), FrameManager.boja_aktivnog_zapisa)# Treci parametar je boja a ako ga nema postavlja se na default

            FrameManager.prikazi_grupu_widgeta("okvir_zaglavlje", "btn_zaglavlje_")# Ako je treci parametar False widget se skriva a ako ga nema prikazuje

            FrameManager.dohvati_okvir("okvir_zaposlenici").prikazi_sve_zaposlenike()
            

        

    @classmethod
    def izbrisi_tvrtku(cls, id_tvrtke):
        print(id_tvrtke)
        session.query(cls).filter_by(id=id_tvrtke).delete()
        session.commit()
        FrameManager.okviri.get("okvir_firme").prikazi_sve_firme()

    @classmethod
    def izbrisi_odabranu_tvrtku(cls):
        session.query(cls).filter_by(id=Tvrtka.odabrana_tvrtka.id).delete()
        session.commit()
        FrameManager.prikazi_grupu_widgeta("okvir_zaglavlje", "btn_zaglavlje_", False)# Ako je treci parametar False widget se skriva a ako ga nema prikazuje
        #FrameManager.okviri.get("okvir_firme").prikazi_sve_firme()
        FrameManager.dohvati_okvir("okvir_firme").prikazi_sve_firme()
        #Tvrtka.odabrana_tvrtka = None
                

    @classmethod
    def ispisi_sve_zaposlenike(cls):
        for tvrtka, zaposlenik in session.query(cls, Zaposlenik).filter(cls.id == Zaposlenik.VK_id_tvrtke).filter(cls.id == cls.odabrana_tvrtka.id).all():
            print(zaposlenik)

    @classmethod
    def vrati_sve_zaposlenike_tvrtke(cls):
        return session.query(Zaposlenik).filter(cls.odabrana_tvrtka.id == Zaposlenik.VK_id_tvrtke).all()
        
    
class Zaposlenik(Base):
    __tablename__ = "zaposlenici"

    id = db.Column(db.Integer, primary_key=True)
    ime = db.Column(db.String)
    prezime = db.Column(db.String)
    adresa = db.Column(db.String)
    oib = db.Column(db.String)
    VK_id_tvrtke = db.Column(db.Integer, db.ForeignKey("tvrtke.id"))

    odabrani_zaposlenik = None

    def __init__(self, ime, prezime, adresa, oib, id_tvrtke):
        self.ime = ime
        self.prezime = prezime
        self.adresa = adresa
        self.oib = oib
        self.VK_id_tvrtke = id_tvrtke

    def __str__(self):
        return("ZAPOSLENIK: " + " " + str(self.id) + " " + self.ime + " " + self.prezime + " " + self.adresa + " " + self.oib)

# sve objekte koji nasljeđuju Base kreira u bazi podataka
Base.metadata.create_all(bind=db_engine)