class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def showInfo(self):
        print("showInfo di class Hero")
        print("{} health : {}".format(
            self.name,
            self.health
            )
        )

class Hero_inttelligent(Hero):
    def __init__(self, name):
        super().__init__(name, 100)

    # Override Method
    def showInfo(self):
        print("showInfo di subclass Hero_intelligent")
        print("{} \n\tTipe : intelligent \n\thealth : {}".format(
            self.name,
            self.health
            )
        )

class Hero_strength(Hero):
    def __init__(self, name):
        super().__init__(name, 200)        


lina = Hero_inttelligent('Lina')
axe = Hero_strength('Axe')

print()

lina.showInfo()
print()

axe.showInfo()
print()



'''
    NB :
        - Override	~> Berfungsi untuk menimpa/mengganti method yg ada di superclass dengan cara memberi nama dan argument yg sama di subclass.
    
    
'''


