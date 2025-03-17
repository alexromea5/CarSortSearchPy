from Masina.masina import Masina

class Repo:
    def __init__(self, file="masini"):
        self.__file = file
        self.__masini = self.save()

    def save(self):
        masini = []
        with open(self.__file, "r") as f:
            for line in f:
                arr = line.split(",")
                masina = Masina(arr[0], arr[1], arr[2], int(arr[3]), int(arr[4]))
                masini.append(masina)
        return masini
