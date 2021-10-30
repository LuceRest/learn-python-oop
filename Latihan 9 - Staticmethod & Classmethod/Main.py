class Hero:

    # Private Class Variable
    __jumlah = 0

    def __init__(self, name):
        self.__name = name
        Hero.__jumlah += 1

    # Method ini hanya berlaku untuk object
    def getJumlah(self):
        return Hero.__jumlah

    # Method ini tidak berlaku untuk object, tapi berlaku untuk class
    def getJumlah1():
        return Hero.__jumlah

    # Method Static (Decorator) (Nempel ke object dan class)
    @staticmethod
    def getJumlah2():
        return Hero.__jumlah

    @classmethod
    def getJumlah3(cls):
        return cls.__jumlah


sniper = Hero('Sniper')
print(Hero.getJumlah2())
print()

rikimaru = Hero('Rikimaru')
print(sniper.getJumlah2())
print()

drowranger = Hero('Drowranger')
print(Hero.getJumlah3())
print()



'''
    NB :
        - Method dengan argument self hanya berlaku untuk object.
        - Method tanpa argument self hanya berlaku untuk class.
        - Method static dapat berlaku untuk object dan class (nempel ke object & class) tanpa mengambil argument.
        - Method class dapat berlaku untuk object dan class (nempel ke class) dengan mengambil argument.

        - Method static (decorator) di python :
            @staticmethod
            def <nama function/method>():
                <action>

        - Method static class (decorator) di python :
            @classmethod
            def <nama function/method>(<argument>):
                <action>


'''
    