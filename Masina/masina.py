class Masina:
    def __init__(self, marca, model, tokenMasina, pretAchizitie, pretVanzare):
        self.__marca = marca
        self.__model = model
        self.__tokenMasina = tokenMasina
        self.__pretAchizitie = pretAchizitie
        self.__pretVanzare = pretVanzare

    @staticmethod
    def comparator_profit(masina1, masina2):
        return masina1.pretVanzare - masina1.pretAchizitie > masina2.pretVanzare - masina2.pretAchizitie

    @staticmethod
    def comparator_token(masina1, masina2):
        return masina1.tokenMasina < masina2.tokenMasina

    @staticmethod
    def comparator_marca_model(masina1, masina2):
        if masina1.marca != masina2.marca:
            return masina1.marca < masina2.marca
        else:
            if masina1.model != masina2.model:
                return masina1.model < masina2.model
            return True

    @staticmethod
    def comparator_marca_model_token(masina1, masina2):
        if masina1.marca != masina2.marca:
            return masina1.marca < masina2.marca
        else:
            if masina1.model != masina2.model:
                return masina1.model < masina2.model
            else:
                return masina1.tokenMasina < masina2.tokenMasina

    @property
    def marca(self):
        return self.__marca

    @property
    def model(self):
        return self.__model

    @property
    def tokenMasina(self):
        return self.__tokenMasina

    @property
    def pretAchizitie(self):
        return self.__pretAchizitie

    @property
    def pretVanzare(self):
        return self.__pretVanzare

    def __str__(self):
        return f"{self.__marca},{self.__model},{self.__tokenMasina},{self.__pretAchizitie},{self.__pretVanzare}"