from math import sqrt
import statistica

def media(*args):
    somma = 0
    contatore = 0
    for valore in args:
        contatore = int(contatore + 1)
        try:
            valore = float(valore)
        except ValueError:
            if (type(valore) == str):
                raise TypeError(f"Il {contatore}° valore che hai inserito è di tipo {type(valore)}, hai inserito: {valore}")
            if (type(valore) == bool):
                raise TypeError(f"Il {contatore}° valore che hai inserito è di tipo {type(valore)}, hai inserito: {valore}")
        except NameError:
            raise TypeError(f"Il {contatore}° valore che hai inserito è di tipo variabile, hai inserito: {valore}")
        try:
            somma = float(somma+valore)
        except TypeError:
            if (type(valore) == str):
                raise TypeError(f"Il {contatore}° valore che hai inserito è di tipo {type(valore)}, hai inserito: {valore}")
            if (type(valore) == bool):
                raise TypeError(f"Il {contatore}° valore che hai inserito è di tipo {type(valore)}, hai inserito: {valore}")
    media = float(somma/len(args))
    return float(media)

def mediana(*args):
    valori = sorted(args)
    lunghezza = len(valori)
    if (lunghezza%2 == 0): #Se la lista è pari allora si fa la media tra i centrali
        try:
            primo_centrale = int((lunghezza/2) - 0.5)
            secondo_centrale = int(primo_centrale + 1)
        except TypeError:
            pass #Mi rendo conto che in realtà questo errore non possa esistere, lunghezza è una variabile restituita da len()
        try:
            primo_centrale = float(valori[primo_centrale])
            secondo_centrale = float(valori[secondo_centrale])
        except IndexError:
            raise IndexError(f"Per qualche motivo la funzione sorted() del modulo non ha trovato il {lunghezza}° valore. Controlla riga 26 del modulo.")
        mediana = float((primo_centrale + secondo_centrale) /2)
    if (lunghezza%2 == 1): #Se la lista è dispari allora si prende il valore centrale
        try:
            centrale = int((lunghezza/2) - 0.5) #Metto -0.5 e non +0.5 perché il primo valore di una stringa non è valori[1] ma valori[0]
        except ValueError:
            pass #Qui devo scrivere l'errore che sarà restituito se per qualche motivo astruso la lunghezza diviso due e meno 0.5 non fosse un intero
        mediana = valori[centrale]
    return mediana

def moda(*args):
    valori = sorted(args) #Sorted è una built-in function che riordina degli interi e dei decimali in ordine crescente
    contatore = 0
    ripetizioni = 0
    archivio_ripetizioni = 0
    moda = 0
    precedente = 0
    for valore in valori:
        contatore = int(contatore + 1)
        if ((type(valore) == float) or (type(valore) == int)):
            if valore == precedente:
                ripetizioni = int(ripetizioni + 1)
                if ripetizioni >= archivio_ripetizioni:
                    archivio_ripetizioni = ripetizioni
                    moda = valore #Il >= implica che un risultato bimodale restituisca esclusivamente l'ultimo tra i valori modali inseriti
                if ripetizioni < archivio_ripetizioni:
                    continue
            if valore != precedente:
                precedente = valore
                ripetizioni = 1
                if ripetizioni >= archivio_ripetizioni:
                    archivio_ripetizioni = ripetizioni
                    moda = valore
                if ripetizioni < archivio_ripetizioni:
                    continue
        else: #Per tutti i valori che non sono numeri
            raise TypeError(f"Il {contatore}° valore che hai inserito è di tipo {type(valore)}, hai inserito: {valore}")
    return float(moda)

def varianza(*args):
    valori = sorted(args)
    lista = args[0]
    for posizione in range(len(valori)): #Qui dovrei provare ad inserire nella funzione media() i singoli valori uno per volta
        pass
    valore_medio = media(args)
    lunghezza = len(valori)
    scarti_quadratici = 0
    for valore in valori:
        scarto = float(valore - valore_medio)
        scarto_quadratico = float(scarto*scarto)
        scarti_quadratici += scarto_quadratico
        continue
    varianza = float(scarti_quadratici / lunghezza)
    print(f'σ² = {varianza}')
    print(f'σ ² = {varianza}')
    return varianza

def scarto_quadratico_medio(*args):
    scarto_quadratico_medio = sqrt(varianza(args))
    print(f'σ = {scarto_quadratico_medio}')
    return scarto_quadratico_medio
