import utils

#Singleton
class Database:
    _store = {}

    def get(self, key):
        value = self.__class__._store.get(key)
        if value:
            print("Found key: {}".format(key))
        return value

    def put(self, key, value: dict):
        utils.validator(value)
        self.__class__._store[key] = value

    def search(self, attrKey, attrValue):
        result = []
        for key, value in self._store.items():
            for storeAttrKey, storeAttrValue in value.items():
                if storeAttrKey == attrKey and storeAttrValue.getValue() == attrValue:
                    result.append(key)
        if len(result) > 0:
            print("Found keys are: [{}]".format(",".join(map(str, result))))
        else:
            print("No item found")
