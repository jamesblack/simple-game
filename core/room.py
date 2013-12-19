class Room(object):
    
    monster = None
    items = []
    
    def __init__(self, items = [], monster = None):
        self.items = items
        self.monster = monster
        
    def describe(self):
        return [self.items, self.monster]