Lantanidi = []
Attinidi = []
class Elemento: #Classe Elemento
    def __init__(self, nome, simbolo, numero, periodo, gruppo, raggio, ppm = None, anno = None): #ppm e anno di scoperta sono opzionali (l'anno dovrà essere non opzionale)
        self.nome = nome
        self.simbolo = simbolo 
        self.numero = int(numero)
        self.periodo = int(periodo)
        self.gruppo = gruppo
        self.raggio = float(raggio) #Dovrò fare in modo che si spieghi che il raggio atomico è calcolato in picometri (m*10^-12)
        if ppm == None:
            self.ppm = "La concentrazione di questo elemento sulla terra è inferiore a 0.003ppm"
        else:
            self.ppm = float(ppm)
        if anno == None: #Qui dovrò invece aggiungere qualcosa che preveda anche la possibilità che anno sia una stringa, come per esempio "noto sin dall'antichità"
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
        if self.gruppo == Primo and periodo != 1: #Da qui iniziano le divisioni per categorie (classi) di elementi, sulla base dei dati di questo link: https://tavolaperiodica.zanichelli.it/it
            self.metallo_alcalino = bool(True)
        else:
            self.metallo_alcalino = bool(False)
        if self.gruppo == Secondo: 
            self.metallo_alcalino_terroso = bool(True)
        else:
            self.metallo_alcalino_terroso = bool(False)
        if self.gruppo == Diciottesimo:
            self.gas_nobile = bool(True)
        else:
            self.gas_nobile = bool(False)
        if periodo == 6 and gruppo == "Terzo": #Discriminazione per i Lantanidi
            Lantanidi.append(self.nome)
            self.Lantanide = bool(True)
            gruppo.sesto_elemento = "15 Lantanidi, lista dei Lantanidi nella lista Lantanidi"
        if periodo == 7 and gruppo == "Terzo": #Discriminazione per gli Attinidi
            Attinidi.append(self.nome)
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
         numero = Numero(self) #Un tentativo probabilmente destinato a fallire.

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

class Numero:
    def __init__(self, elemento):
        self.elemento = elemento
        
_1 = Numero(Idrogeno) 
_2 = Numero(Elio)
_3 = Numero(Litio)
_4 = Numero(Berilio)
_5 = Numero(Boro)
_6 = Numero(Carbonio)
_7 = Numero(Azoto)
_8 = Numero(Ossigeno) #Se a riga 63 non funziona, mi tocca fare così per altri 110 elementi mi sa...

#ASSEGNAZIONE OGGETTI ELEMENTO

#Primo periodo
Idrogeno = Elemento("Idrogeno", "H", 1, 1, Primo, 0.30, 8700, 1766)
Elio = Elemento("Elio", "He", 2, 1, Diciottesimo, 0.93, 3000, 1895)

#Secondo periodo
Litio = Elemento("Litio", "Li", 3, 2, Primo, 1.55, 65, 1817)
Berilio = Elemento("Berilio", "Be", 4, 2, Secondo, 1.12, 6, 1798)
Boro = Elemento("Boro", "B", 5, 2, Tredicesimo, 0.98, 3, 1808)
Carbonio = Elemento("Carbonio", "C", 6, 2, Quattordicesimo, 0.91, 800)
Azoto = Elemento("Azoto", "N", 7, 2, Quindicesimo, 0.92, 300, 1772)
Ossigeno = Elemento("Ossigeno", "O", 8, 2, Sedicesimo, 0.66, 495000, 1774)
Fluoro = Elemento("Fluoro", "F", 9, 2, Diciassettesimo, 0.64, 270, 1771)
Neon = Elemento("Neon", "Ne", 10, 2, Diciottesimo, 1.60, anno = 1898)

#Terzo periodo
Sodio = Elemento("Sodio", "Na", 11, 3, Primo, 1.90, 26000, 1807)
Magnesio = Elemento("Magnesio", "K", 12, 3, Secondo, 1.60, 19000, 1755)
Alluminio = Elemento("Alluminio", "Al", 13, 3, Tredicesimo, 1.43, 75000, 1827)
Silicio = Elemento("Silicio", "Si", 14, 3, Quattordicesimo, 1.32, 257000, 1823)
Fosforo = Elemento("Fosforo", "P", 15, 3, Quindicesimo, 1.28, 1200)
Zolfo = Elemento("Zolfo", "S", 16, 3, Sedicesimo, 1.04, 600)
Cloro = Elemento("Cloro", "Cl", 17, 3, Diciassettesimo, 0.99, 1900, 1774)
Argon = Elemento("Argon", "Ar", 18, 3, Diciottesimo, 1.91, 400, 1894)

#Quarto periodo
Potassio = Elemento("Potassio", "K", 19, 4, Primo, 2.35, 24000, 1807)
Calcio = Elemento("Calcio", "Ca", 20, 4, Secondo, 1.97, 34000, 1808)
Scandio = Elemento("Scandio", "Sc", 21, 4, Terzo, 1.60, 5, 1879)
Titanio = Elemento("Titanio", "Ti", 22, 4, Quarto, 1.46, 5800, 1791)
Vanadio = Elemento("Vanadio", "V", 23, 4, Quinto, 1.34, 150, 1830)
Cromo = Elemento("Cromo", "Cr", 24, 4, Sesto, 1.27, 200, 1797)
Manganese = Elemento("Manganese", "Mn", 25, 4, Settimo, 1.26, 1000, 1774)
Ferro = Elemento("Ferro", "Fe", 26, 4, Ottavo, 1.26, 47000)
Cobalto = Elemento("Cobalto", "Co", 27, 4, Nono, 1.25, 23, 1735)
Nichel = Elemento("Nichel", "Ni", 28, 4, Decimo, 1.24, 80, 1751)
Rame = Elemento("Rame", "Cu", 29, 4, Undicesimo, 1.28, 70)
Zinco = Elemento("Zinco", "Zn", 30, 4, Dodicesimo, 1.33, 132, 1746)
Gallio = Elemento("Gallio", "Ga", 31, 4, Tredicesimo, 1.41, 15, 1875)
Germanio = Elemento("Germanio", "Ge", 32, 4, Quattordicesimo, 1.37, 7, 1886)
Arsenico = Elemento("Arsenico", "As", 33, 4, Quindicesimo, 1.39, 5)
Selenio = Elemento("Selenio", "Se", 34, 4, Sedicesimo, 1.40, 0.09, 1817)
Bromo = Elemento("Bromo", "Br", 35, 4, Diciassettesimo, 1.14, 1.62, 1826)
Cripton = Elemento("Cripton", "Kr", 36, 4, Diciottesimo, 2.0, 1894)

#Quinto periodo
Rubidio = Elemento("Rubidio", "Rb", 37, 5, Primo, 2.48, 310, 1861)
Stronzio = Elemento("Stronzio", "Sr", 38, 5, Secondo, 2.15, 300, 1790)
Ittirio = Elemento("Ittirio", "Y", 39, 5, Terzo, 1.79, 28, 1794)
Zirconio = Elemento("Zirconio", "Zr", 40, 5, Quarto, 1.60, 220, 1789)
Niobio = Elemento("Niobio", "Nb", 41, 5, Quinto, 1.46, 24, 1801)
Molibdeno = Elemento("Molibdeno", "Mo", 42, 5, Sesto, 1.39, 8, 1778)
Tecnezio = Elemento("Tecnezio", "Tc", 43, 5, Settimo, 1.36, anno = 1937)
Rutenio = Elemento("Rutenio", "Ru", 44, 5, Ottavo, 1.33, anno = 1844)
Rodio = Elemento("Rodio", "Rh", 45, 5, Nono, 1.34, anno = 1803)
Palladio = Elemento("Palladio", "Pd", 46, 5, Decimo, 1.38, 0.01, 1803)
Argento = Elemento("Argento", "Ag", 47, 5, Undicesimo, 1.44, 0.1)
Cadmio = Elemento("Cadmio", "Cd", 48, 5, Dodicesimo, 1.54, 0.15, 1817)
Indio = Elemento("Indio", "In", 49, 5, Tredicesimo, 1.66, 0.1, 1863)
Stagno = Elemento("Stagno", "Sn", 50, 5, Quattordicesimo, 1.62)
Antimonio = Elemento("Antimonio", "Sb", 51, 5, Quindicesimo, 1.59, 1)
Tellurio = Elemento("Tellurio", "Te", 52, 5, Sedicesimo, 1.60, anno = 1782)
Iodio = Elemento("Iodio", "I", 53, 5, Diciassettesimo, 1.33, 0.3, 1811)
Xenon = Elemento("Xenon", "Xe", 54, 5, Diciottesimo, 2.20, anno = 1898)

#Sesto periodo
Cesio = Elemento("Cesio", "Cs", 55, 6, Primo, 2.67, 7, 1860)
