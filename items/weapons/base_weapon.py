from ..base_item import BaseItem

class BaseWeapon(BaseItem):

    def __init__(self, name = "DefaultWeapon", hit_chance = .5, damage = 1):
        self.name = name
        self.hit_chance = hit_chance
        self.damage = damage