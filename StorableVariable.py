from json import load, dump
from os.path import basename

__version__ = 1.0

class StorableVariable():

    def __init__(self, variable) -> None:
        self.name = f"{variable=}".split('=')[0] # Oops it returns the value
        self.path = f"D:\Python\Python\Variables\{basename(__file__).split('.')[0]}\{self.name}.txt"
        self.get_value()

    def store(self) -> None:
        dump(self, open(self.path, 'w'))
    
    def get_value(self) -> None:
        self.value = load(open(self.path, 'r'))