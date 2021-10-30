from Hero import HeroIntelligent, HeroStrength

print()

lina = HeroIntelligent('Lina')
slardar = HeroStrength('Slardar')

lina.showInfo()
slardar.showInfo()

print()
print("--------------------------------------------")
print()

lina.gainExp = 200
slardar.gainExp = 250

lina.showInfo()
slardar.showInfo()