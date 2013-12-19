from base_weapon import BaseWeapon

class Dagger(BaseWeapon):

    def __init__(self, name = "DefaultDagger"):
        super(Dagger, self).__init__(name, .90, 2)
