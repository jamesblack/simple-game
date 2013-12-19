from base_weapon import BaseWeapon

class Sword(BaseWeapon):

    def __init__(self, name = "DefaultSword"):
        super(Sword, self).__init__(name, .75, 4)
