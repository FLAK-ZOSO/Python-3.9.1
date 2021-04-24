no = ["Niente", "niente", "Nnt", "nnt", "nulla", "Nulla", "no", "No", "NO"]
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
    def __init__(self, nome, cognome, disoccupato, lavoro, reddito, regione, datore_di_lavoro, tasse):
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
    def __init__(self, nome, cognome, lavoro, reddito, regione, azienda):
        super().__init__(nome, cognome, regione, disoccupato)
        self.disoccupato = "No"
        self.lavoro = "Capo d'azienda"
        self.reddito = reddito
        self.azienda = azienda
    def Assumi(cittadino, azienda):
        return f"{cittadino.datore_di_lavoro} era il datore di lavoro di {cittadino.nome} {cittadino.cognome}"
        cittadino.datore_di_lavoro = azienda
        return f"{cittadino.datore_di_lavoro} è ora il datore di lavoro di {cittadino.nome} {cittadino.cognome}"
