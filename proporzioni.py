def Proporzione_eseguendo():
    print("""
0)       EXIT
1)        x:a = b:c
2)       a:x = b:c
3)       a:b = x:c
4)       a:b = c:x
""")
    modalità = input("Opzione:   ")
    try:
        modalità = int(modalità)
    except ValueError:
        print(f"Hai sbagliato a inserire il parametro modalità, doveva essere un intero, invece hai inserito {modalità}")
    except TypeError:
        print(f"Hai sbagliato a inserire il parametro modalità, doveva essere un intero, invece hai inserito {modalità}")
     if modalità == 0:
        return
    if (modalità != 1 and modalità != 2 and modalità != 3 and modalità != 4):
        print("Inserimento non valido")
        print("-----------------------")
        Proporzione_eseguendo()
        return
    a = input("a:  ")
    b = input("b:  ")
    c = input("c:  ")
    try:
        a = float(a)
        b = float(b)
        c = float(c)
    except ValueError:
        print(f"Hai inserito male uno dei tre valori (a, b, c), hai inserito rispettivamente {a}, {b}, {c}")
    if modalità == 1:
        try:
            x = float(a*b/c)
        except ZeroDivisionError:
            print(f"Il valore c è uguale a zero, è insorto uno ZeroDivisionError.")
    if modalità == 2:
        try:
            x = float(a*c/b)
        except ZeroDivisionError:
            print(f"Il valore b è uguale a zero, è insorto uno ZeroDivisionError.")
    if modalità == 3:
        try:
            x = float(a*c/b)
        except ZeroDivisionError:
            print(f"Il valore b è uguale a zero, è insorto uno ZeroDivisionError.")
    if modalità == 4:
        try:
            x = float(b*c/a)
        except ZeroDivisionError:
            print(f"Il valore a è uguale a zero, è insorto uno ZeroDivisionError.")
    return f"x = {x}"

def proporzione(modalità, a, b, c):
    try:
        modalità = int(modalità)
    except ValueError:
        print(f"Hai sbagliato a inserire il parametro modalità, doveva essere un intero, invece hai inserito {modalità}")
    except TypeError:
        print(f"Hai sbagliato a inserire il parametro modalità, doveva essere un intero, invece hai inserito {modalità}")
        
    if (modalità != 1 and modalità != 2 and modalità != 3 and modalità != 4):
        print("Modalità non valid")
        return
    
    try:
        a = float(a)
        b = float(b)
        c = float(c)
    except ValueError:
        print(f"Hai inserito male uno dei tre valori (a, b, c), hai inserito rispettivamente {a}, {b}, {c}")
        
    if modalità == 1:
        try:
            x = float(a*b/c)
        except ZeroDivisionError:
            print(f"Il valore c è uguale a zero, è insorto uno ZeroDivisionError.")
    if modalità == 2:
        try:
            x = float(a*c/b)
        except ZeroDivisionError:
            print(f"Il valore b è uguale a zero, è insorto uno ZeroDivisionError.")
    if modalità == 3:
        try:
            x = float(a*c/b)
        except ZeroDivisionError:
            print(f"Il valore b è uguale a zero, è insorto uno ZeroDivisionError.")
    if modalità == 4:
        try:
            x = float(b*c/a)
        except ZeroDivisionError:
            print(f"Il valore a è uguale a zero, è insorto uno ZeroDivisionError.")
            
    return x
