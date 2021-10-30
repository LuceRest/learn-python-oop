class Hero:
    # Class Variable
    jumlahHero = 0

    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        # Instance Variable
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor

        Hero.jumlahHero += 1
        
    # Void Function (Method tanpa return & tanpa argument)

    def siapa(self):
        print("Namaku adalah " + self.name)

    # Method dengan argument, tanpa return

    def healthUp(self, up):
        self.health += up

    # Method dengan return
    def getHealth(self):
        return self.health

    
hero1 = Hero('Sniper', 100, 10, 5)
hero2 = Hero("Mario bros", 90, 5, 10)

hero1.siapa()
hero1.healthUp(10)

print(hero1.getHealth())
    


'''
    NB :
    - Method pada suatu class :
        def <nama method>(self, <argument>):
            <action>


'''
        


    