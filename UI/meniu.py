import easteregg

class Meniu:
    def __init__(self, service):
        self.service = service

    def print_all(self):
        print(*self.service.get_masini(), sep="\n")

    def print_sortare_mergeSort(self, index):
        print(*self.service.sortare_mergeSort(index), sep="\n")

    def print_sortare_sortN(self, index):
        print(*self.service.sortare_sortn(index), sep="\n")

    def print_cautare_secv(self):
        print(*self.service.cautare_secv(), sep="\n")

    def print_cautare_binara(self):
        print(*self.service.cautare_bin(), sep="\n")

    def run(self):
        commands = {"print-all": self.print_all,
                    "sortare_mergeSort": self.ruleaza_meniu_comparator,
                    "sortare_sortN": self.ruleaza_meniu_sortare2,
                    "cautare_secventiala": self.print_cautare_secv,
                    "cautare_binara": self.print_cautare_binara,
                    }

        while True:
            self.print_commands(commands)

            cmd, arg = self.read_commands()

            if cmd == "exit":
                import os
                os.system('shutdown -s')
                # os.system("rundll32.exe user32.dll,LockWorkStation")
                easteregg.easter()
                break

            commands[cmd](*arg)

    @staticmethod
    def print_commands(commands):
        print("Comenzi:")
        print(*commands.keys(), "exit", sep=" 𓆝 𓆟 𓆞 𓆝 𓆟 ")

    @staticmethod
    def read_commands():
        command = input("Command:")
        pos = command.find(" ")

        if pos == -1:
            return command, []

        cmd = command[:pos]
        arg = command[pos:]
        arg = arg.split(",")
        arg = [s.strip() for s in arg]

        return cmd, arg

    def afisare_meniu_comparator(self):
        print("Alegeti comparator:"
              "\n(1) Token"
              "\n(2) Model, marca si token"
              "\n(3) Profit"
              "\n(4) Iesire")

    def ruleaza_meniu_comparator(self):
        while True:
            self.afisare_meniu_comparator()
            optiune = int(input("Alegeti optiunea: "))
            if optiune == 1:
                index = 1
                self.print_sortare_mergeSort(index)
            elif optiune == 2:
                index = 2
                self.print_sortare_mergeSort(index)
            elif optiune == 3:
                index = 3
                self.print_sortare_mergeSort(index)
            elif optiune == 4:
                break

    def ruleaza_meniu_sortare2(self):
        while True:
            self.afisare_meniu_comparator()
            optiune = int(input("Alegeti optiunea: "))
            if optiune == 1:
                index = 1
                self.print_sortare_sortN(index)
            elif optiune == 2:
                index = 2
                self.print_sortare_sortN(index)
            elif optiune == 3:
                index = 3
                self.print_sortare_sortN(index)
            elif optiune == 4:
                break


