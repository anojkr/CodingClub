
class User(object):

    def __init__(self, id: str):
        self.id = id
        self.email = None

    def getId(self):
        return self.id

    def getEmail(self):
        return self.email

    def setEmail(self, email):
        self.email = email
