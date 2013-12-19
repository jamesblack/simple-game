def intro_screen():
  print "Welcome to the Dungeon Training Course!"
  print "In this course, you will learn how to Krush, Kill, and Destroy!"
  print """You yourself are a complete and total noob, but once this is over, you'll be a seasoned
veteran. In the case of complete and total annihilation, you'll be kicked out and never allowed
to return, 'cause you'll be dead.
  
    Your first step towards greatness begins here. There will be little to no help getting through
this training course, but honestly, you don't need it. Good luck!"""
  
  print ""
  print "Press [Space] to Continue"
  
def menu_screen(player):
  print "Welcome to the Dungeon"
  print "======================"
  
  print "[N]ew Game"
  if player is not None:
    print "[R]esume Game"
  print ""
  print "[Q]uit Game"
  