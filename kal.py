
class Kalkulator:

    def __init__(self):
        self.__typy = (int,float)        

    def dodaj(self, liczba1, liczba2):
        if isinstance(liczba1, self.__typy):
            if isinstance(liczba2, self.__typy):
                return liczba1 + liczba2

    def odejmij(self, liczba1, liczba2):
        if isinstance(liczba1, self.__typy): 
             if isinstance(liczba1, self.__typy):        
                return liczba1 - liczba2

    def pomnoz(self, liczba1, liczba2):
        if isinstance(liczba1, self.__typy): 
             if isinstance(liczba1, self.__typy):        
                return liczba1 * liczba2

    def dziel(self, liczba1, liczba2):
        if liczba2 == 0:
            raise ValueError("nie można dzielić przez 0") 
        if isinstance(liczba1, self.__typy): 
             if isinstance(liczba1, self.__typy):        
                return liczba1 / liczba2
