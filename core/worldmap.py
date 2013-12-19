class WorldMap(object):
    
    rooms = []
    
    def __init__(self, rooms = []):
        self.rooms = rooms
    
    
    def draw_room(self, player):
      print "Player is currently located at {0}, {1}".format(player.x, player.y)
      print "Player currently has {0} hits left".format(player.hits)
        
      room = self.rooms[player.x][player.y].describe()
      
      print "Items"
      print "=================="
      
      if len(room[0]) > 0:
        for item in room[0]:
          print item.name
      else:
        print "None"
      
      print "------------------"
      
      print "Monster"
      print "=================="
      
      if room[1] is not None:
        print room[1].name
      else:
        print "None"
      
      print "-----------------"
  