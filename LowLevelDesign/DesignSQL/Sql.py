
from typing import List
class SQL(object):

    def __init__(self, database):
        self.database = database

    def addTable(self, tableName):
        return self.database.addTable(tableName)

    def getRecord(self, tableName, ids : List[str]):
        return self.database.getRecord(tableName, ids)

    def addRecord(self, tableName, id, record):
        return self.database.addRecord(tableName, id, record)
