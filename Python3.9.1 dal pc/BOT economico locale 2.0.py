import time

No = ["Niente", "niente", "Nnt", "nnt", "nulla", "Nulla", "no", "No", "NO"]
Sì = ["Sì", "sì", "si", "Si", "SI", "ok", "Ok", "OK"]
cittadini = 0
Giorno = 0

class cittadino:
    def __init__(self, nome, cognome, regione, disoccupato):
        self.nome = nome
        self.cognome = cognome
        self.regione = regione
        self.disoccupato = disoccupato
    def scheda_cittadino(self):
        if self.disoccupato in Sì:
            return f"{self.nome} {self.cognome} vive in {self.regione} ed è disoccupato"
        if self.disoccupato in No:
            return f"{self.nome} {self.cognome}: lavora come {self.lavoro} per conto di {self.datore_di_lavoro} con lo stipendio di {self.reddito}€ al mese, residente in {self.regione}"

class operaio(cittadino):
    def __init__(self, nome, cognome, regione, disoccupato, lavoro, reddito, datore_di_lavoro, tasse):
        super().__init__(nome, cognome, regione, disoccupato)
        self.disoccupato = "No"
        self.lavoro = "operaio"
        self.reddito = reddito
        self.datore_di_lavoro = datore_di_lavoro
        self.tasse = tasse
    def Capo(self):
        print(self.datore_di_lavoro)
        self.datore_di_lavoro = input("Nuovo datore di lavoro: ")
        print(self.datore_di_lavoro)

class capo_di_azienda(cittadino):
    def __init__(self, nome, cognome, regione, disoccupato, lavoro, reddito, azienda):
        super().__init__(nome, cognome, regione, disoccupato)
        self.disoccupato = "No"
        self.lavoro = "Capo d'azienda"
        self.reddito = reddito
        self.azienda = azienda
    def Assumi(cittadino, azienda):
        return f"{cittadino.datore_di_lavoro} era il datore di lavoro di {cittadino.nome} {cittadino.cognome}"
        cittadino.datore_di_lavoro = azienda
        return f"{cittadino.datore_di_lavoro} è ora il datore di lavoro di {cittadino.nome} {cittadino.cognome}"
    def Aumento(dipendente):
        print(dipendente.reddito)
        modifica = input()
        if modifica == 0 or modifica is str:
            pass
        else:
            dipendente.reddito += round(modifica)
        print(dipendente.reddito)
    
class azienda:
    def __init__(self, nome, fondazione, proprietario, dipendenti, fatturato):
        self.nome = nome
        self.fondazione = input("Giorno di fondazione: ")
        if proprietario.lavoro == "Capo d'azienda":
            self.proprietario = proprietario
        else:
            return "L'utente {proprietario} non esiste."
        self.dipendenti = dipendenti
        self.fatturato = fatturato
        
def Benvenuto(username):
    print("Benvenuto in Italia!" + str(username))
def Buongiorno():
    Giorno = Giorno+1
    
def Bilancio(username):
    if username in cittadino:
        print(username.patrimonio)
def Paga(username):
    if username in users:
        username.patrimonio += username.reddito
def Stipendio(username):
    print(username.reddito)
def Patrimonio(username):
    print(username.patrimonio)
def Tasse(cittadino):
    if cittadino.reddito <= 1250:
        tasse = round(cittadino.reddito*0.23)
        cittadino.tasse = tasse
        print(tasse)
    if cittadino.reddito > 1250:
        tasse = round(1250*0.23)
        reddito_residuo = round(cittadino.reddito-1250)
        if cittadino.reddito  <= 2333:
            tasse = round(tasse + reddito_residuo*0.27)
            cittadino.tasse = tasse
            print(tasse)
        if cittadino.reddito > 2333:
            tasse = round(tasse + 1083*0.27)
            reddito_residuo = round(reddito_residuo - 1083)
            if cittadino.reddito  <= 4583:
                tasse = round(tasse + reddito_residuo*0.38)
                cittadino.tasse = tasse
                print(tasse)
            if cittadino.reddito > 4583:
                tasse = round(tasse + 2250*0.38)
                reddito_residuo = round(reddito_residuo - 2250)
                if cittadino.reddito  <= 6250:
                    tasse = round(tasse + reddito_residuo*0.41)
                    cittadino.tasse = tasse
                    print(tasse)
                if cittadino.reddito > 6250:
                    tasse = round(tasse + 1667*0.41)
                    reddito_residuo = round(reddito_residuo - 1667)
                    tasse = round(reddito_residuo*0.43)
                    cittadino.tasse = tasse
                    print(tasse)
def Contribuzione(username):
    if Giorno%30 != 0:
        "Non è ancora il momento di pagare le tasse."
    if Giorno%30 == 0:
        Tasse(username)
        print(username.tasse)
        username.patrimonio = round(username.patrimonio-username.tasse)
