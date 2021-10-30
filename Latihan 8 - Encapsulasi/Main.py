class Hero:

    def __init__(self, name, health, attackPower):
        self.__name = name
        self.__health = health
        self.__attPower = attackPower

    # Getter

    def getName(self):
        return self.__name

    def getHealth(self):
        return self.__health
    
    # Setter

    def diserang(self, serangPower):
        self.__health -= serangPower

    def setAttPower(self, nilaiBaru):
        self.__attPower = nilaiBaru


# Awal dari Game

earthshaker = Hero("earthshaker", 50, 5)

# Game Berjalan

print(earthshaker.getName())
print(earthshaker.getHealth())
earthshaker.diserang(5)
print(earthshaker.getHealth())



'''
    NB :
        - Aturan dari encapsulasi :
            - Buat semua variabel menjadi private variable.
            - Gunakan getter untuk mengambil variabelnya dan setter untuk mensetting variabelnya.





'''