from base_mobile import BaseMobile

import random

random.seed()

class PlayerMobile(BaseMobile):
  
    equipped = None
  
    def __init__(self, name = "John", x = 0, y = 0, inventory = []):
        super(PlayerMobile, self).__init__(name)
        
        self.x = x
        self.y = y
        
        self.inventory = []
        
    def move_north(self):
      self.x = self.x - 1
    
    def move_south(self):
      self.x = self.x + 1
    
    def move_west(self):
      self.y = self.y - 1
    
    def move_east(self):
      self.y = self.y + 1
        
    def can_move_north(self):
      return self.x > 0
    
    def can_move_south(self):
      return self.x < 9
    
    def can_move_east(self):
      return self.y < 9
    
    def can_move_west(self):
      return self.y > 0
    
    def draw_actions(self, room):
      print "Available Options"
      print "================="
      print ""
      if self.can_move_north():
        print "[N]orth"
      if self.can_move_south():
        print "[S]outh"  
      if self.can_move_east():
        print "[E]ast"
      if self.can_move_west():
        print "[W]est"
      if len(room.items) > 0 or room.monster is not None:
        print ""
        if len(room.items) > 0:
          print "[G]rab Items"
        if room.monster is not None:
          print "[U]se Weapon On Mob"
      print ""
      print "[I]nventory"
      print "[M]enu"
    
    def grab_items(self, room):
      self.inventory.extend(room.items)
      room.items = []
      
    def draw_inventory(self):
      print "Currently Equipped"
      print "================================="
      print ""
      if self.equipped is not None:
        print "[{0} ({1} hit chance | {2} damage)".format(self.equipped.name, self.equipped.hit_chance, self.equipped.damage)
      else:
        print "You have no equipped weapon"
      print ""
      print "---------------------------------"
      print ""
      print "What item would you like to equip"
      print "================================="
      print ""
      if len(self.inventory) == 0:
        print "You have no items to equip"
      else:
        for (index, item) in enumerate(self.inventory):
          print "[{0}] - {1} ({2} hit chance | {3} damage)".format(index, item.name, item.hit_chance, item.damage)
      print ""
      print "Close [I]nventory"
    
    def equip_item(self, index):
      if self.equipped is not None:
        self.inventory.append(self.equipped)
      
      self.equipped = self.inventory[index]
      
      del self.inventory[index]
    
    def attack(self, target):
      print self.name + " attacks!"
      if random.random() <= self.equipped.hit_chance:
        target.hits = target.hits - self.equipped.damage
        print self.name + " hits for " + str(self.equipped.damage) + " damage!"
      else:
        print self.name + " misses like an idiot!"