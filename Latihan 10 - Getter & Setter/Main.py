class Hero:

    def __init__(self, name, health, armor):
        self.name = name
        self.__health = health
        self.__armor = armor
        # self.info = "Name {} : \nHealth : {}".format(self.name, self.__health)

    @property
    def info(self):
        return "Name \t: {}  \nHealth \t: {}".format(self.name, self.__health)

    @property
    def armor(self):
        pass

    @armor.getter
    def armor(self):
        return self.__armor

    @armor.setter
    def armor(self, input):
        self.__armor = input

    @armor.deleter
    def armor(self):
        print("Armor didelete")
        self.__armor = None


sniper = Hero("Sniper", 100, 10)

print()

print('Merubah info')
print(sniper.info)
print()
sniper.name = 'Evory'
print(sniper.info)

print()
print("---------------------------------")
print()

print("Getter & Setter untuk __armor")
print(sniper.armor)
print()
sniper.armor = 50
print(sniper.armor)

print()
print("---------------------------------")
print()

print("Delete Armor")
del sniper.armor
print(sniper.__dict__)
print()



'''
    NB :
        - @property	~> Berfungsi untuk mengubah suatu method menjadi seperti variabel.

        - Penggunaan @property di python :
            @property
            def <nama method yg ingin dianggap seperti variabel>(<argument>):
                <action>

        - Getter di python :
            @<nama method>.getter
            def <nama method>(self):
                return self.<private variable>
            <nama object>.<nama method>

        - Setter di python :
            @<nama method>.setter
            def <nama method>(self, <argument>):
                <action>
            <nama object>.<nama method> = <isi private variable yg baru>

        - Deleter di python :
            @<nama method>.deleter
            def <nama method>(self):
                self.<private variable yg ingin didelete> = None
            del <nama object>.<nama method>


'''

