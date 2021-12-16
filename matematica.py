from math import sqrt
from math import pi
from math import radians, degrees
from math import cos, sin, tan
from math import acos, asin, atan

def pitagora(primo_cateto, secondo_cateto):
    ipotenusa = float(sqrt(primo_cateto * primo_cateto + secondo_cateto * secondo_cateto))
    return ipotenusa

def pitagora_cateto_ipotenusa(primo_cateto, ipotenusa):
    secondo_cateto = float(sqrt(primo_cateto * primo_cateto - ipotenusa * ipotenusa))
    return secondo_cateto

def coseno(angolo):
    try:
        angolo = float(angolo)
    except TypeError:
        raise TypeError(f'Errore di inserimento per il parametro angolo, hai inserito: {angolo}')
    eseguibile = bool(type(angolo) == float)
    if eseguibile:
        try:
            angolo_radianti = float(angolo*pi/180)
        except ValueError:
            raise ValueError(f'Errore di inserimento per il parametro angolo, hai inserito: {angolo}')
        coseno = cos(angolo_radianti)
        return coseno

def seno(angolo):
    try:
        angolo = float(angolo)
    except TypeError:
        raise TypeError(f'Errore di inserimento per il parametro angolo, hai inserito: {angolo}')
    eseguibile = bool(type(angolo) == float)
    if eseguibile:
        try:
            angolo_radianti = float(angolo*pi/180)
        except ValueError:
            raise ValueError(f'Errore di inserimento per il parametro angolo, hai inserito: {angolo}')
        seno = sin(angolo_radianti)
        return seno

def angolo_opposto(cateto, ipotenusa):
    try:
        ipotenusa = float(ipotenusa)
    except TypeError:
        raise TypeError(f"Errore di inserimento per il parametro ipotenusa, hai inserito: {ipotenusa}")
    except NameError:
        raise NameError(f"Errore di inserimento per il parametro ipotenusa, hai inserito una variabile non esistente.")
    try:
        cateto = float(cateto)
    except TypeError:
        raise TypeError(f"Errore di inserimento per il parametro cateto, hai inserito: {cateto}")
    except NameError:
        raise NameError(f"Errore di inserimento per il parametro cateto, hai inserito una variabile non esistente.")
    try:
        seno_angolo_opposto = cateto/ipotenusa
    except ZeroDivisionError:
        raise ZeroDivisionError(f"Errore di inserimento per il parametro ipotenusa, il tuo è un triangolo che non può essere in alcun modo rettangolo, perché hai fornito il valore {ipotenusa} per l'ipotenusa.")
    try:
        seno_angolo_opposto = float(seno_angolo_opposto)
        if (seno_angolo_opposto == 0):
            raise ValueError(f"Errore di inserimento per il parametro cateto, il tuo è un triangolo che non può essere in alcun modo rettangolo, perché hai fornito il valore {cateto} per il cateto noto.")
        if (seno_angolo_opposto < 0):
            if (cateto < 0):
                raise ValueError(f"Errore di inserimento per il parametro cateto, il tuo è un triangolo che non può esistere, perché hai fornito un valore negativo ({cateto}) per il cateto noto.")
            if (ipotenusa < 0):
                raise ValueError(f"Errore di inserimento per il parametro ipotenusa, il tuo è un triangolo che non può esistere, perché hai fornito un valore negativo ({cateto}) per l'ipotenusa.")
        if (seno_angolo_opposto > 0):
            if (cateto < 0):
                raise ValueError(f"Entrambi i valori da te inseriti come parametri sono negativi.")
            else:
                pass
    except OverflowError:
        seno_angolo_opposto = float(round(seno_angolo_opposto))
    try:
        seno_angolo_opposto = float(seno_angolo_opposto)
    except OverflowError:
        seno_angolo_opposto = float(round(seno_angolo_opposto))
    try:
        angolo = float(asin(seno_angolo_opposto))
        angolo = degrees(angolo)
    except ImportError:
        angolo = float(asin(seno_angolo_opposto))
        angolo = degrees(angolo)
        raise ImportError(f"Errore nell'importazione del modulo math, in particolare riguardo la funzione asin(), da parte di matematica.py.")
    return angolo

def aiuto(funzione):
    pass
