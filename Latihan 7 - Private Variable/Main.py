class Hero:

    # Class Variable
    
    jumlah = 0
    __privateJumlah = 0

    def __init__(self, name, health):
        self.name = name
        self.health = health

        # Variable Instance Private
        self.__private = "private"

        # Variable Instance Protected
        self._protected = "protected"


lina = Hero("Lina", 100)

print(lina.__dict__)
print()

print(lina._protected)
lina._protected = "testing"

print(lina.__dict__)
print()

print(lina._protected)

print()
print("--------------------------------------------")
print()

print(lina.__dict__)
print()

print(Hero.__dict__)
print()
# print(Hero.__privateJumlah)



'''
    NB :
    - Private variable		~> Berfungsi untuk encapsulasi suatu variabel.

    - Private variable di python :
        <nama object>.__<nama private variable> = <isi private variable>

    - Protected variable di python :
        <nama object>._<nama protected variable> = <isi protected variable>

    - Protected variable bisa diakses & diubah, biasanya dipakai di dalam class saja.



'''
