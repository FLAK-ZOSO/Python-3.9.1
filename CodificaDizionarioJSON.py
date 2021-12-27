from json import load, dumps

def CreaFile(File_path:str):
    try:
        File = open(File_path, 'w')
    except PermissionError:
        raise PermissionError(f"Python CodificaDizionarioJSON.py doesn't have the permission to create a file into this directory.")
    File.close()

def CodificaDizionario(File_path:str, Dizionario:dict):
    CreaFile(File_path)
    File = open(File_path, "w+")
    File.write(dumps(Dizionario))
    File.close()
    File = open(File_path, "r+")
    return File.read()

def DecodificaDizionario(File_path:str):
    try:
        File = open(File_path, "r+")
    except FileNotFoundError:
        raise FileNotFoundError(f"File at directory {File_path} doesn't exist.")
    Dizionario = load(File)
    File.close()
    return Dizionario

from os import remove
def EliminaFileSe(File_path:str):
    try:
        remove(File_path)
    except FileNotFoundError:
        raise FileNotFoundError(f"File at directory {File_path} doesn't exist.")
    except PermissionError:
        raise PermissionError(f"Python CodificaDizionario.py doesn't have the permission to delete a file into this directory.")

def EliminaFile(File_path:str):
    try:
        remove(File_path)
    except FileNotFoundError:
        return
    except PermissionError:
        return

def CreaCodifica(File_path, Dizionario):
    CreaFile(File_path)
    CodificaDizionario(File_path, Dizionario)

def DecodificaElimina(File_path):
    DecodificaDizionario(File_path)
    EliminaFile(File_path)
