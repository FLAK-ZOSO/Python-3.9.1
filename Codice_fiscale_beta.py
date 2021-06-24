global maiuscole, consonanti, vocali, cifre
maiuscole = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'Z']
consonanti = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'Z', 'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'z']
vocali = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
cifre = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#-------------------------------------------------------------------------------------------------------------------------------------------------------------
import Conversioni_tipi
from Conversioni_tipi import lettera_da_mese
from Conversioni_tipi import lettera_da_numero_con_zero
from Conversioni_tipi import numero_da_lettera_codice_fiscale_dispari
#-------------------------------------------------------------------------------------------------------------------------------------------------------------
def cognome(cognome):
    cognome = str(cognome).upper()
    lunghezza = len(cognome)

    if (lunghezza < 3):
        raise ValueError(f"Hai inserito '{cognome}' un cognome lungo {lunghezza} caratteri. Servono almeno 3 lettere per il codice fiscale.")
    if (lunghezza == 3):
        return cognome

    if (lunghezza > 3):
        sigla = str('')
        for lettera in cognome:
            if lettera in consonanti:
                sigla += lettera
            if lettera in vocali:
                pass
            #else:
                #raise ValueError(f"Hai inserito '{lettera}' tra le lettere del tuo cognome, ma questa non compare tra i caratteri convenzionali.")

        lunghezza = len(sigla)
        if (lunghezza > 3):
            sigla = str(sigla[:3])
            return sigla

        if (lunghezza < 3):
            for lettera in cognome:
                if lettera in vocali:
                    sigla += lettera
                    lunghezza = len(sigla)
                    if (lunghezza == 3):
                        return sigla

        if (lunghezza == 3):
            return sigla
#-------------------------------------------------------------------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------------------------------------------------------------------------
def nome(nome): #Per il cognome Marchese restituisce solo MC
    nome = str(nome)
    nome = nome.upper()

    if (nome == 'XXX'):
        return nome
    lunghezza = len(nome)

    if (lunghezza < 3):
        if (lunghezza == 0):
            raise ValueError(f"Hai inserito una stringa vuota per il tuo cognome, se sei senza cognome inserisci XXX.")
        if (lunghezza == 1):
            sigla = str(nome + 'XX')
        if (lunghezza == 2):
            sigla = str(nome + 'X')

    if (lunghezza == 3):
        return nome

    if (lunghezza > 3):
        sigla = str('')
        for lettera in nome:
            if lettera in consonanti:
                sigla += lettera
            if lettera in vocali:
                pass
            #else:
                #raise ValueError(f"Hai inserito '{lettera}' tra le lettere del tuo nome, ma questa non compare tra i caratteri convenzionali.")

        if (len(sigla) < 3):
            for lettera in nome:
                if lettera in vocali:
                    sigla += lettera
                if (len(sigla) == 3):
                    return sigla
        
        lunghezza = len(sigla)

        if (lunghezza > 3):
            sigla = str(sigla[:2]+sigla[3])
            return sigla

        if (lunghezza < 3):
            for lettera in nome:
                if lettera in vocali:
                    sigla += lettera
                    lunghezza = len(sigla)
                    if (lunghezza == 3):
                        return sigla

        if (lunghezza == 3):
            return sigla
#-------------------------------------------------------------------------------------------------------------------------------------------------------------
def data(sesso, giorno, mese, anno):
    anno = str(anno)
    data = anno[2:]

    data += lettera_da_mese(mese)
    
    if sesso == "Maschio":
        data += str(giorno)
    if sesso == "Femmina":
        data += str(giorno+40)
    if sesso == "Non binario":
        data += str(giorno)

    if (len(data) == 5):
        pass
    else:
        raise ValueError("Qualcosa non funziona nella funzione data")
    
    if (len(str(giorno)) == 2):
        pass
    else:
        raise ValueError("Qualcosa non funziona nella funzione data nel parametro giorno")

    if (len(anno) == 4):
        pass
    else:
        raise ValueError("Qualcosa non funziona nella funzione data nel parametro anno")

    return data
#-------------------------------------------------------------------------------------------------------------------------------------------------------------
def carattere_di_controllo(codice):
    dividendo = 0

    for lettera in codice:
        if lettera in cifre:
            codice = codice.replace(lettera, lettera_da_numero_con_zero(lettera))
    
    for lettera in codice:
        if (codice.find(lettera)%2 == 1): #In realtà se è divisibile per due si trova in posizione dispari
            dividendo += (maiuscole.index(lettera))
        if (codice.find(lettera)%2 == 0):
            dividendo += int(numero_da_lettera_codice_fiscale_dispari(lettera)) #Questa funzione non funziona con gli interi ma solo con le stringhe
        #else:
            #raise TypeError("Hai inserito un codice che contiene valori impossibile")

    numero = int(dividendo%26)
    carattere = lettera_da_numero_con_zero(numero)
    return carattere
#-------------------------------------------------------------------------------------------------------------------------------------------------------------
def codice_fiscale(Nome, Cognome, sesso, giorno, mese, anno, codice_comune_o_stato_estero):
    codice_fiscale = cognome(Cognome)
    codice_fiscale += nome(Nome)
    codice_fiscale += data(sesso, giorno, mese, anno)
    codice_fiscale += codice_comune_o_stato_estero #Qui mi aspetto che si inserisca direttamente il codice del comune, per malfunzionamenti di Selenium.py dovrò rimandare una funzione che lo estrapoli da sé
    codice_fiscale += carattere_di_controllo(codice_fiscale.upper())
    return codice_fiscale
