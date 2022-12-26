

class Driver(object):

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return "[{}, {}]".format(self.id, self.name)