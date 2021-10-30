class Hero:     # Template
    pass


hero1 = Hero()  # Object / instance (instansiate)
hero2 = Hero()
hero3 = Hero()

hero1.name = "sniper"
hero1.health = 500

hero2.name = "sven"
hero2.health = 200

hero3.name = "ucup"
hero3.health = 1000

print(hero1)
print(hero1.__dict__)
print(hero1.name)



'''
    NB :
        - Class/template di python :
            class <nama class>:
                pass

        - Object/instance (instansiate) di python :
            <nama object> = <nama class>()

        - <nama object>.<attribute> = <isi attribute>	~> Berfungsi untuk memberi attribute pada suatu object.

        - print(<nama object>.__dict__)			        ~> Berfungsi untuk menampilkan semua attribute dan isinya dari suatu object.


'''