#Import all the items
from items import *
from items.weapons import *

base_weapon = BaseWeapon()
sword = Sword()
dagger = Dagger()

print "Base Weapon"
print "======================="
print base_weapon.name
print base_weapon.hit_chance
print base_weapon.damage

print "Sword Weapon"
print "======================="
print sword.name
print sword.hit_chance
print sword.damage

print "Dagger Weapon"
print "======================="
print dagger.name
print dagger.hit_chance
print dagger.damage
