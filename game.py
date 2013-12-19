#Import core libs
import os
from core.libs import *

#Import all the items
from items import *
from items.weapons import *



base_weapon = BaseWeapon()
sword = Sword()
dagger = Dagger()

running = True

while (running):

  os.system("clear")

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

  action = getch()

  if action.lower() == "q":
    os.system("clear")
    running = False
