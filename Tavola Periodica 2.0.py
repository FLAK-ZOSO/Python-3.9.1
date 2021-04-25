class Elemento: #Classe Elemento
    def __init__(self, nome, simbolo, numero, periodo, gruppo, raggio, ppm = None, anno = None): #ppm e anno di scoperta sono opzionali
        self.nome = nome
        self.simbolo = simbolo 
        self.numero = int(numero)
        self.periodo = int(periodo)
        self.gruppo = gruppo
        self.raggio = float(raggio)
        self.ppm = float(ppm)
        self.anno = int(anno)
        if periodo == 1: #A partire da questa IF si piazzano i nomi degli elementi dichiarati negli attributi dei gruppi, classe definita in seguito
            gruppo.primo_elemento = self.nome
        if periodo == 2:
            gruppo.secondo_elemento = self.nome
        if periodo == 3:
            gruppo.terzo_elemento = self.nome
        if periodo == 4:
            gruppo.quarto_elemento = self.nome
        if periodo == 5:
            gruppo.quinto_elemento = self.nome
        if periodo == 6:
            gruppo.sesto_elemento = self.nome
        if periodo == 7:
            gruppo.settimo_elemento = self.nome
        if periodo == 6 and gruppo == "Terzo":
            print("Lantanide")
            gruppo.sesto_elemento = "15 Lantanidi, lista dei Lantanidi nella lista Lantanidi"
        if periodo == 7 and gruppo == "Terzo":
            print("Attinide")
            gruppo.settimo_elemento = "15 Attinidi, lista degli Attinidi nella lista Attinidi"
        if periodo == 1 or periodo == 2 or periodo == 3:
            if periodo == 1 and (gruppo == "Secondo", gruppo == "Terzo" or gruppo == "Quarto" or gruppo == "Quinto" or gruppo == "Sesto" or gruppo == "Settimo" or gruppo == "Ottavo" or gruppo == "Nono" or gruppo == "Decimo" or gruppo == "Undicesimo" or gruppo == "Dodicesimo", gruppo == "Tredicesimo", gruppo == "Quattordicesimo", gruppo == "Quindicesimo", gruppo == "Sedicesimo", gruppo == "Diciassettesimo"):
                print("Questo elemento non esiste.")
                self.nome = "Error 1" # i tre errori mi servono per capire quale errore c'è
                # Il risultato è stato che sia Idrogeno che Elio danno Error 1
            elif periodo == 2 and (gruppo == "Terzo" or gruppo == "Quarto" or gruppo == "Quinto" or gruppo == "Sesto" or gruppo == "Settimo" or gruppo == "Ottavo" or gruppo == "Nono" or gruppo == "Decimo" or gruppo == "Undicesimo" or gruppo == "Dodicesimo"):
                print("Questo elemento non esiste.")
                self.nome = "Error 2"
            elif periodo == 3 and (gruppo == "Terzo" or gruppo == "Quarto" or gruppo == "Quinto" or gruppo == "Sesto" or gruppo == "Settimo" or gruppo == "Ottavo" or gruppo == "Nono" or gruppo == "Decimo" or gruppo == "Undicesimo" or gruppo == "Dodicesimo"):
                print("Questo elemento non esiste.")
                self.nome = "Error 3"

class Gruppo:
    def __init__(self, primo_elemento = None, secondo_elemento = None, terzo_elemento = None, quarto_elemento = None, quinto_elemento = None, sesto_elemento = None, settimo_elemento = None):
        print(self)

Primo = Gruppo()
Secondo = Gruppo()
Terzo = Gruppo()
Quarto = Gruppo()
Quinto = Gruppo()
Sesto = Gruppo()
Settimo = Gruppo()
Ottavo = Gruppo()
Nono = Gruppo()
Decimo = Gruppo()
Undicesimo = Gruppo()
Dodicesimo = Gruppo()
Tredicesimo = Gruppo()
Quattordicesimo = Gruppo()
Quindicesimo = Gruppo()
Sedicesimo = Gruppo()
Diciassettesimo = Gruppo()
Diciottesimo = Gruppo()

Idrogeno = Elemento("Idrogeno", "H", 1, 1, Primo, 0.30, 8700, 1766)
Elio = Elemento("Elio", "He", 2, 1, Diciottesimo, 0.93, 3000, 1895)
Litio = Elemento("Litio", "Li", 3, 2, Primo, 1.55, 65, 1817)
Berilio = Elemento("Berilio", "Be", 4, 2, Secondo, 1.12, 6, 1798)
#Qui ci vanno tutti gli altri elementi
