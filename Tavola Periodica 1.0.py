class Elemento:
    def __init__(self, nome, simbolo, numero, periodo, gruppo, raggio, ppm = None, anno = None):
        self.nome = nome
        self.simbolo = simbolo
        self.numero = int(numero)
        self.raggio = float(raggio)
        self.ppm = float(ppm)
        self.anno = int(anno)
        if periodo == 1:
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
        if periodo == 8:
            gruppo.ottavo_elemento = self.nome
        if periodo == 9:
            gruppo.nono_elemento = self.nome
        if periodo == 10:
            gruppo.decimo_elemento = self.nome
        if periodo == 11:
            gruppo.undicesimo_elemento = self.nome
        if periodo == 12:
            gruppo.dodicesimo_elemento = self.nome
        if periodo == 13:
            gruppo.tredicesimo_elemento = self.nome
        if periodo == 14: #DIO PORCO SEI UN DEFICIENTE MATTIA E CHE CAZZO DI PERIODI CE NE STANNO 7 E NON 18 CAZZO ORA DEVI RIFARE TUTTO
            gruppo.quattordicesimo_elemento = self.nome
        if periodo == 15:
            gruppo.quindicesimo_elemento = self.nome
        if periodo == 16:
            gruppo.sedicesimo_elemento = self.nome
        if periodo == 17:
            gruppo.diciassettesimo_elemento = self.nome
        if periodo == 18:
            gruppo.diciottesimo_elemento = self.nome
        if periodo ==

class Gruppo:
    def __init__(self, primo_elemento = None, secondo_elemento = None, terzo_elemento = None)
