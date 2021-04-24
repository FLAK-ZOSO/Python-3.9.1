class azienda:
    def __init__(self, nome, fondazione, proprietario, dipendenti, fatturato):
        self.nome = nome
        self.fondazione = input("Giorno di fondazione: ")
        if proprietario in cittadino:
            self.proprietario = proprietario
        else:
            return "L'utente {proprietario} non esiste."
        self.dipendenti = dipendenti
        self.fatturato = fatturato
