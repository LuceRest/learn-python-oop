class Hero:

    def __init__(self, name, health, attackPower, armorNumer):
        self.name = name
        self.health = health
        self.attackPower = attackPower
        self.armorNumber = armorNumer

    def serang(self, lawan):
        print(self.name + " menyerang " + lawan.name)
        lawan.diserang(self, self.attackPower)

    def diserang(self, lawan, attackPower_lawan):
        print(self.name + ' diserang ' + lawan.name)
        attack_diterima = attackPower_lawan/self.armorNumber
        print('Serangan terasa : ' +str(attack_diterima))
        self.health -= attack_diterima
        print("Darah " + self.name + ' tersisa ' + str(self.health))


sniper = Hero("Sniper", 100, 10, 5)
rikimaru = Hero("Rikimaru", 100, 20, 10)

sniper.serang(rikimaru)
print()

rikimaru.serang(sniper)
print()

        
        
