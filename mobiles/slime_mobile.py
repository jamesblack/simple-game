from base_mobile import BaseMobile

import random

random.seed()

class SlimeMobile(BaseMobile):
  
  hit_chance = .25
  damage = 2
  
  def __init__(self, name = "Default Slime"):
    super(SlimeMobile, self).__init__(name, 4)
  
  
  def attack(self, target):
    print self.name + " attacks!"
    if random.random() <= self.hit_chance:
      target.hits = target.hits - self.damage
      print self.name + " hits for " + str(self.damage) + " damage!"
    else:
      print self.name + " misses like an idiot!"