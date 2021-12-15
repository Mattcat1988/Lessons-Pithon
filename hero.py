class Hero:
    """Class to create Hero for our Game"""

    def __init__(self, name, level, race):
        """initiate our hero"""
        self.name = name
        self.level = level
        self.race = race
        self.heath = 100

    def show_hero(self):
        """print all parameters of this hero"""
        discrition = (self.name + " Level is: " + str(self.level) + " Race is: " + self.race + " Healt is " + str(
            self.heath)).title()
        print(discrition)

    def level_up(self):
        """Upgrade level of Hero"""
        self.level += 1

    def move(self):
        """Start moving Hero"""
        print("Hero" + self.name + "Start moving....")

    def set_health(self, new_health):
        self.heath = new_health


class SuperHero(Hero):
    """Class to create super hero"""

    def __init__(self, name, level, race, magiclevel):
        """Initiate our Super Hero"""
        super().__init__(name, level, race)
        self.magiclevel = magiclevel
        self.magic = 100

    def makemagic(self):
        """User magic"""
        self.magic -= 10

    def show_hero(self):
        discrition = (self.name + " Level is: " + str(self.level) + " Race is: " + self.race + " Healt is " + str(
            self.heath) + " Magic is: " + str(self.magic)).title()
        print(discrition)
