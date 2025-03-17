class Tests:
    def __init__(self, service):
        self.service = service

    def test_cautare_secventiala(self):
        lista = self.service.get_masini()
        lista_noua = self.service.cautare_secventiala(lista, "a0a07khqts")
        assert (lista_noua[0].tokenMasina == "a0a07khqts")

    def test_cautare_binara(self):
        lista = self.service.get_masini()
        lista_noua = self.service.cautare_binara(lista, "efy9nlvfcs")
        assert (lista_noua[0].tokenMasina == "efy9nlvfcs")

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
            else:
                return masina1.tokenMasina < masina2.tokenMasina

    def test_sortare_sortn(self):
        lista_nesortata1 = self.service.get_masini()
        lista_nesortata2 = self.service.get_masini()
        lista_nesortata3 = self.service.get_masini()

        lista_sortata1 = self.service.sortn(lista_nesortata1, self.comparator_token)
        lista_sortata2 = self.service.sortn(lista_nesortata2, self.comparator_marca_model)
        lista_sortata3 = self.service.sortn(lista_nesortata3, self.comparator_profit)

        assert lista_sortata1[0].tokenMasina == "a0a07khqts"
        assert lista_sortata2[0].marca == "Audi"
        assert lista_sortata3[0].pretVanzare == 17631

    def test_sortare_mergesort(self):
        lista_nesortata1 = self.service.get_masini()
        lista_nesortata2 = self.service.get_masini()
        lista_nesortata3 = self.service.get_masini()
        lista_sortata1 = self.service.mergeSort(lista_nesortata1, self.comparator_token)
        lista_sortata2 = self.service.mergeSort(lista_nesortata2, self.comparator_marca_model)
        lista_sortata3 = self.service.mergeSort(lista_nesortata3, self.comparator_profit)
        assert lista_sortata1[0].tokenMasina == "a0a07khqts"
        assert lista_sortata2[0].marca == "Audi"
        assert lista_sortata3[0].pretVanzare == 17631

    def teste(self):
        self.test_cautare_secventiala()
        self.test_cautare_binara()
        self.test_sortare_sortn()
        self.test_sortare_mergesort()
