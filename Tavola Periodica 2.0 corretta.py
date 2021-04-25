class Elemento: #Classe Elemento
    def __init__(self, nome, simbolo, numero, periodo, gruppo, raggio, ppm = None, anno = None, Lantanide = None, Attinide = None): #ppm e anno di scoperta sono opzionali
        self.nome = nome
        self.simbolo = simbolo 
        self.numero = int(numero)
        self.periodo = int(periodo)
        self.gruppo = gruppo
        self.raggio = float(raggio)
        if ppm == None:
            pass
        else:
            self.ppm = float(ppm)
        if anno == None:
            pass
        else:
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
            # print("Lantanide")
            gruppo.sesto_elemento = "15 Lantanidi, lista dei Lantanidi nella lista Lantanidi"
            self.Lantanide = bool(True)
        if periodo == 7 and gruppo == "Terzo":
            # print("Attinide")
            self.Attinide = bool(True)
            gruppo.settimo_elemento = "15 Attinidi, lista degli Attinidi nella lista Attinidi"
        if periodo == 1 or periodo == 2 or periodo == 3:
            if periodo == 1 and (gruppo == "Secondo" or gruppo == "Terzo" or gruppo == "Quarto" or gruppo == "Quinto" or gruppo == "Sesto" or gruppo == "Settimo" or gruppo == "Ottavo" or gruppo == "Nono" or gruppo == "Decimo" or gruppo == "Undicesimo" or gruppo == "Dodicesimo" or gruppo == "Tredicesimo" or gruppo == "Quattordicesimo" or gruppo == "Quindicesimo" or gruppo == "Sedicesimo" or gruppo == "Diciassettesimo"):
                print("Questo elemento non esiste.")
                self.nome = "ELEMENTO INESISTENTE"
            elif periodo == 2 and (gruppo == "Terzo" or gruppo == "Quarto" or gruppo == "Quinto" or gruppo == "Sesto" or gruppo == "Settimo" or gruppo == "Ottavo" or gruppo == "Nono" or gruppo == "Decimo" or gruppo == "Undicesimo" or gruppo == "Dodicesimo"):
                print("Questo elemento non esiste.")
                self.nome = "ELEMENTO INESISTENTE"
            elif periodo == 3 and (gruppo == "Terzo" or gruppo == "Quarto" or gruppo == "Quinto" or gruppo == "Sesto" or gruppo == "Settimo" or gruppo == "Ottavo" or gruppo == "Nono" or gruppo == "Decimo" or gruppo == "Undicesimo" or gruppo == "Dodicesimo"):
                print("Questo elemento non esiste.")
                self.nome = "ELEMENTO INESISTENTE"

class Gruppo:
    def __init__(self, quanti_elementi, primo_elemento = None, secondo_elemento = None, terzo_elemento = None, quarto_elemento = None, quinto_elemento = None, sesto_elemento = None, settimo_elemento = None):
        self.quanti_elementi = int(quanti_elementi)

Primo = Gruppo(7)
Secondo = Gruppo(6)
Terzo = Gruppo(4) # I Lantanidi e gli Attinidi contano come un solo elemento a testa
Quarto = Gruppo(4)
Quinto = Gruppo(4)
Sesto = Gruppo(4)
Settimo = Gruppo(4)
Ottavo = Gruppo(4)
Nono = Gruppo(4)
Decimo = Gruppo(4)
Undicesimo = Gruppo(4)
Dodicesimo = Gruppo(4)
Tredicesimo = Gruppo(6)
Quattordicesimo = Gruppo(6)
Quindicesimo = Gruppo(6)
Sedicesimo = Gruppo(6)
Diciassettesimo = Gruppo(6)
Diciottesimo = Gruppo(7)

Idrogeno = Elemento("Idrogeno", "H", 1, 1, Primo, 0.30, 8700, 1766)
Elio = Elemento("Elio", "He", 2, 1, Diciottesimo, 0.93, 3000, 1895)
Litio = Elemento("Litio", "Li", 3, 2, Primo, 1.55, 65, 1817)
Berilio = Elemento("Berilio", "Be", 4, 2, Secondo, 1.12, 6, 1798)
Boro = Elemento("Boro", "B", 5, 2, Tredicesimo, 0.98, 3, 1808)
Carbonio = Elemento("Carbonio", "C", 6, 2, Quattordicesimo, 0.91, 800)
Azoto = Elemento("Azoto", "N", 7, 2, Quindicesimo, 0.92, 300, 1772)
Ossigeno = Elemento("Ossigeno", "O", 8, 2, Sedicesimo, 0.66, 495000, 1774)
Fluoro = Elemento("Fluoro", "F", 9, 2, Diciassettesimo, 0.64, 270, 1771)
Neon = Elemento("Neon", "Ne", 10, 2, Diciottesimo, 1.60, anno = 1898)
#Qui ci vanno tutti gli altri elementi
