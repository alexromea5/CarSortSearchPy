from Repository.repo import Repo
from Service.service import Service
from UI.meniu import Meniu
from test import Tests

if __name__ == '__main__':
    repository = Repo()
    service = Service(repository)

    # teste = Tests(service)
    # teste.teste()

    meniu = Meniu(service)
    meniu.run()