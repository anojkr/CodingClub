class Database(object):

    def __init__(self, name):
        self.name = name
        self._tables = {}

    def addTable(self, tableName):
        self._tables[tableName] = {}
        return self

    def getAllTableRecord(self, tableName):
        return self._tables.get(tableName)

    def addRecord(self, tableName, id, rowRecord):
        tablePtr = self._tables[tableName]
        if id not in tablePtr:
            tablePtr[id] = rowRecord
        else:
            raise Exception("Duplicate Record")
        return self

    def getRecord(self, tableName, ids):
        return [self._tables.get(tableName).get(id) for id in ids]
