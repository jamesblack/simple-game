#Import core libs
import os
from core.libs import *

#Import all the items
from items import *
from items.weapons import *

from core import *

from mobiles import *

world = WorldMap([
    [Room([Sword("Gideon's Destroyer"), Dagger("Gideon's Stabber")]), Room([], SlimeMobile("Bobo")), Room([], SlimeMobile("Baba")), Room(), Room(), Room(), Room(), Room(), Room(), Room()],
    [Room(), Room(), Room(), Room(), Room(), Room(), Room(), Room(), Room(), Room()],
    [Room(), Room(), Room(), Room(), Room(), Room(), Room(), Room(), Room(), Room()],
    [Room(), Room(), Room(), Room(), Room(), Room(), Room(), Room(), Room(), Room()],
    [Room(), Room(), Room(), Room(), Room(), Room(), Room(), Room(), Room(), Room()],
    [Room(), Room(), Room(), Room(), Room(), Room(), Room(), Room(), Room(), Room()],
    [Room(), Room(), Room(), Room(), Room(), Room(), Room(), Room(), Room(), Room()],
    [Room(), Room(), Room(), Room(), Room(), Room(), Room(), Room(), Room(), Room()],
    [Room(), Room(), Room(), Room(), Room(), Room(), Room(), Room(), Room(), Room()],
    [Room(), Room(), Room(), Room(), Room(), Room(), Room(), Room(), Room(), Room()],
    ])

player = None

game_running = True

# Game States
# Intro
# Menu
# Inventory
# GameWorld
game_state = "Intro"

while (game_running):

  os.system("clear")
  
  if game_state == "Intro":
    intro_screen()
  elif game_state == "Menu":
    menu_screen(player)
  elif game_state == "Inventory":
    player.draw_inventory()
  elif game_state == "GameWorld":
    if world.rooms[player.x][player.y].monster is not None:
      world.rooms[player.x][player.y].monster.attack(player)
      if player.hits <= 0:
        player = None
        game_state = "Menu"
        continue
    world.draw_room(player)
    player.draw_actions(world.rooms[player.x][player.y])
  else:
    pass
  
  valid_action = False
  
  while not valid_action:
    action = getch()
    
    if action.lower() == "q":
      valid_action = True
      game_running = False
      os.system("clear")
    
    if game_state == "Intro":
      if action.lower() == " ":
        game_state = "Menu"
        valid_action = True
    
    elif game_state == "Menu":
      if action.lower() == "n":
        player = PlayerMobile("Samantha")
        valid_action = True
        game_state = "GameWorld"
      
      elif action.lower() == "r" and player is not None:
        valid_action = True
        game_state = "GameWorld"
    
    elif game_state == "Inventory":
      if action.lower() == "i":
        valid_action = True
        game_state = "GameWorld"
      
      elif len(player.inventory) > 0:
        try:
          if int(action) >= 0 and int(action) < len(player.inventory):
            valid_action = True
            player.equip_item(int(action))
        except:
          pass
    
    elif game_state == "GameWorld":
      if action.lower() == "n" and player.can_move_north():
        valid_action = True
        player.move_north()
        
      elif action.lower() == "s" and player.can_move_south():
        valid_action = True
        player.move_south()
        
      elif action.lower() == "e" and player.can_move_east():
        valid_action = True
        player.move_east()
        
      elif action.lower() == "w" and player.can_move_west():
        valid_action = True
        player.move_west()
        
      elif action.lower() == "g" and len(world.rooms[player.x][player.y].items) > 0:
        valid_action = True
        player.grab_items(world.rooms[player.x][player.y])
        
      elif action.lower() == "u" and world.rooms[player.x][player.y].monster is not None:
        valid_action = True
        monster = world.rooms[player.x][player.y].monster
        player.attack(monster)
        
        if monster.hits <= 0:
          world.rooms[player.x][player.y].monster = None
      
      elif action.lower() == "i":
        valid_action = True
        game_state = "Inventory"
      
      elif action.lower() == "m":
        valid_action = True
        game_state = "Menu"

