class Team:
    def setTeam(self, team):
        self.team = team

    def showTeam(self):
        print(self.team)


class Tipe_Hero:
    def setTipe(self, tipe):
        self.tipe = tipe

    def showTipe(self):
        print(self.tipe)


class Hero(Team, Tipe_Hero):
    def __init__(self, name, health):
        self.name = name
        self.health = health


evory = Hero('Evory', 100)
evory.setTeam("Merah")
evory.setTipe("Duelist")

evory.showTeam()
evory.showTipe()