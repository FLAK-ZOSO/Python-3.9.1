# (23/06/2021-)

global maiuscole, maiuscole_per_mesi
maiuscole = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'Z']
maiuscole_per_mesi = ['A', 'B', 'C', 'D', 'E', 'H', 'L', 'M', 'P', 'R', 'S', 'T']

def lettera_da_numero_con_zero(numero):
    return maiuscole[int(numero)]

def lettera_da_numero_senza_zero(numero):
    return maiuscole[int(numero)-1]

def lettera_da_mese(mese):

    if (type(mese) == int):
        if mese > 12 or mese < 1:
            raise ValueError('Hai inserito un valore non valido per un mese, riprova con un numero tra 1 e 12')
        numero = mese

    try:
        mese = int(mese)
    except TypeError:
        pass
    except ValueError:
        pass

    if mese == "Gennaio" or mese == "gennaio" or mese == "Gen" or mese == "gen":
        numero = 1

    if mese == "Febbraio" or mese == "febbraio" or mese == "Feb" or mese == "feb":
        numero = 2

    if mese == "Marzo" or mese == "marzo" or mese == "Mar" or mese == "mar":
        numero = 3

    if mese == "Aprile" or mese == "aprile" or mese == "Apr" or mese == "apr":
        numero = 4
    
    if mese == "Maggio" or mese == "maggio" or mese == "Mag" or mese == "mag":
        numero = 5

    if mese == "Giugno" or mese == "giugno" or mese == "Giu" or mese == "giu":
        numero = 6
        
    if mese == 'Luglio' or mese == "luglio" or mese == 'Lug' or mese == 'lug':
        numero = 7

    if mese == "Agosto" or mese == "agosto" or mese == "Ago" or mese == "ago":
        numero = 8

    if mese == "Settembre" or mese == "settembre" or mese == "Set" or mese == "set":
        numero = 9

    if mese == "Ottobre" or mese == "ottobre" or mese == "Ott" or mese == "ott":
        numero = 10

    if mese == "Novembre" or mese == "novembre" or mese == "Nov" or mese == "nov":
        numero = 11

    if mese == "Dicembre" or mese == "dicembre" or mese == "Dic" or mese == "dic":
        numero = 12

    return maiuscole_per_mesi[numero-1]

def numero_da_lettera_codice_fiscale_dispari(lettera):
    if lettera == 'A':
        return 1
    if lettera == 'B':
        return 0
    if lettera == 'C':
        return 5
    if lettera == 'D':
        return 7
    if lettera == 'E':
        return 9
    if lettera == 'F':
        return 13
    if lettera == 'G':
        return 15
    if lettera == 'H':
        return 17
    if lettera == 'I':
        return 19
    if lettera == 'J':
        return 21
    if lettera == 'K':
        return 2
    if lettera == 'L':
        return 4
    if lettera == 'M':
        return 18
    if lettera == 'N':
        return 20
    if lettera == 'O':
        return 11
    if lettera == 'P':
        return 3
    if lettera == 'Q':
        return 6
    if lettera == 'R':
        return 8
    if lettera == 'S':
        return 12
    if lettera == 'T':
        return 14
    if lettera == 'U':
        return 16
    if lettera == 'V':
        return 10
    if lettera == 'W':
        return 22
    if lettera == 'X':
        return 25
    if lettera == 'Y':
        return 24
    if lettera == 'Z':
        return 23
