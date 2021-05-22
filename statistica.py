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
    return media

def mediana(*args):
    valori = sorted(args) #Sorted è una built-in function che riordina degli interi e dei decimali in ordine crescente
    lunghezza = len(valori)
    if (lunghezza%2 == 0): #Se la lista è pari allora si fa la media tra i centrali
        try:
            primo_centrale = int((lunghezza/2) - 0.5)
        secondo_centrale = int(primo_centrale + 1)
        primo_centrale = float(valori[primo_centrale])
        secondo_centrale = float(valori[secondo_centrale])
        media = float((primo_centrale + secondo_centrale) /2)
        return media
    if (lunghezza%2 == 1): #Se la lista è dispari allora si prende il valore centrale
        try:
            centrale = int((lunghezza/2) - 0.5) #Metto -0.5 e non +0.5 perché il primo valore di una stringa non è valori[1] ma valori[0]
        except ValueError:
            pass #Qui devo scrivere l'errore che sarà restituito se per qualche motivo astruso la lunghezza diviso due e meno 0.5 non fosse un intero
        finally: #Finally mi ha sempre dato problemi, non so se funzionerà o se mi toccherà rimuoverlo, lo tengo qui solo per motivi di indentazione
            return valori[centrale]
