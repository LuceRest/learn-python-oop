class Hero:     #template

    def __init__(self, inputName, inputHealth, inputPower,inputArmor):
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor


hero1 = Hero("sniper", 100, 10, 4)
hero2 = Hero("mirana", 100, 15, 1)
hero3 = Hero("Evory", 1000, 100, 0)

print()
print(hero1.__dict__)
print("\n------------------------------------------------------------------")

print(hero2.__dict__)
print("\n------------------------------------------------------------------")

print(hero3.__dict__)
print()



'''
    NB :
        - def __init__(self):	~> Function yg pertama kali akan dijalankan ketika object dari suatu class dibuat.
            - self	-> Object dari suatu class yg bersangkutan.


'''