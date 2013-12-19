class BaseMobile(object):
    
    name = "Default Mobile"
    hits = 10
    
    def __init__(self, name = "Default Mobile", hits = 10):
        self.name = name
        self.hits = hits