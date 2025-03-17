from Masina.masina import Masina
import time


class Service:
    def __init__(self, repository):
        self.repository = repository

    def get_masini(self):
        return self.repository.save()

    def sortare_sortn(self, index):
        list_nesort = self.repository.save()
        list_sort = []
        if index == 1:
            list_sort = self.sortn(list_nesort, Masina.comparator_token)
        elif index == 2:
            list_sort = self.sortn(list_nesort, Masina.comparator_marca_model)
        elif index == 3:
            list_sort = self.sortn(list_nesort, Masina.comparator_profit)
        return list_sort

    def sortn(self, lista, comparator):
        count_comparatii = 0
        count_operatii = 0
        start_time = time.time()
        for i in range(len(lista)):
            for j in range(i + 1, len(lista)):
                count_comparatii += 1
                if comparator(lista[i], lista[j]) == 0:
                    lista[i], lista[j] = lista[j], lista[i]
                    count_operatii += 1
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Timpul de executie: {execution_time} secunde")
        return lista # , count_comparatii, count_operatii, count_comparatii, count_operatii

    def sortare_mergeSort(self, index):
        list_nesort = self.repository.save()
        list_sort = []
        if index == 1:
            list_sort = self.mergeSort(list_nesort, Masina.comparator_token)
        elif index == 2:
            list_sort = self.mergeSort(list_nesort, Masina.comparator_marca_model)
        elif index == 3:
            list_sort = self.mergeSort(list_nesort, Masina.comparator_profit)
        return list_sort

    def mergeSort(self, lista, comparator):
        count_comparatii = 0
        count_operatii = 0

        if len(lista) > 1:
            mid = len(lista) // 2
            L = lista[:mid]
            R = lista[mid:]

            L = self.mergeSort(L, comparator)
            R = self.mergeSort(R, comparator)

            # count_comparatii += comp_L + comp_R
            # count_operatii += op_L + op_R

            i = j = k = 0
            while i < len(L) and j < len(R):
                count_comparatii += 1
                if comparator(L[i], R[j]):
                    lista[k] = L[i]
                    i += 1
                else:
                    lista[k] = R[j]
                    j += 1
                k += 1
                count_operatii += 1

            while i < len(L):
                lista[k] = L[i]
                i += 1
                k += 1
                count_operatii += 1

            while j < len(R):
                lista[k] = R[j]
                j += 1
                k += 1
                count_operatii += 1

        return lista  # , count_comparatii, count_operatii

    def cautare_secventiala(self, lista, criteriu):
        count_comparatii = 0
        count_operatii = 0
        lista_noua = []
        for i in range(len(lista)):
            count_comparatii += 1
            if lista[i].tokenMasina == criteriu:
                lista_noua.append(lista[i])
                count_operatii += 1
        # print(f"Numarul de comparatii: {count_comparatii}")
        # print(f"Numarul de operatii: {count_operatii}")
        return lista_noua

    def cautare_secv(self):
        token = input("Alege token:")
        # start_time = time.time()
        lista_cautata = self.cautare_secventiala(self.repository.save(), token)
        # end_time = time.time()
        # execution_time = end_time - start_time
        # print(f"Timpul de executie: {execution_time} secunde")
        return lista_cautata

    def cautare_binara(self, lista, criteriu):
        # sortam lista de la inceput
        lista.sort(key=lambda x: x.tokenMasina)

        stanga = 0
        dreapta = len(lista) - 1
        lista_noua = []

        count_comparatii = 0
        count_operatii = 0

        # start_time = time.time()

        while stanga <= dreapta:
            mijloc = (stanga + dreapta) // 2
            midpoint = lista[mijloc].tokenMasina

            count_comparatii += 1

            if midpoint == criteriu:
                lista_noua.append(lista[mijloc])
                count_operatii += 1
                break
            elif midpoint > criteriu:
                dreapta = mijloc - 1
            else:
                stanga = mijloc + 1

            count_operatii += 1

        # end_time = time.time()
        # execution_time = end_time - start_time
        # print(f"Numarul de comparatii: {count_comparatii}")
        # print(f"Numarul de operatii: {count_operatii}")
        # print(f"Timpul de executie: {execution_time} secunde")

        return lista_noua

    def cautare_bin(self):
        token = input("Alege token:")
        lista_cautata = self.cautare_binara(self.repository.save(), token)
        return lista_cautata
