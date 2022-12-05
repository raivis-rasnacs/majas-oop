from time import sleep

class Maja():

    def __init__(self, logi = 4, stavi = 2, temp = 16):

        # True - aizslēgtas, False - atslēgtas
        self.durvis = {
            "parādesDurvis":True,
            "sētasDurvis":True
        }
        self.logi = logi
        self.stavi = stavi
        self.temp = temp

    def atslega(self):
        durvis = input("Kuras durvis?")
        self.durvis[durvis] = True if self.durvis[durvis] == False else False
        print(self.durvis)

    def pieliktMalku(self):
        self.temp += 2
        print(self.temp)

manaMaja = Maja()
manaMaja.pieliktMalku()
manaMaja.pieliktMalku()

class Pils(Maja):

    def __init__(self, *args):
        print(args)
        super().__init__(*args)
        self.torni = 4

    def zvanitZvanu(self):
        for _ in range(5):
            print("Ding dong")
            sleep(1)

manaPils = Pils(4, 1, 20)
print(manaPils.torni)


    
