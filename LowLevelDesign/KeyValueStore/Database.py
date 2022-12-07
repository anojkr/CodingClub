from singleton.singleton import Singleton
import utils


class Database():
    _store = {}

    def get(self, key):
        return self.__class__._store.get(key)

    def put(self, key, value: dict):
        utils.validator(value)
        self.__class__._store[key] = value

    def search(self, attrKey, attrValue):
        result = []
        for key, value in self._store.items():
            for storeAttrKey, storeAttrValue in value.items():
                if storeAttrKey == attrKey and storeAttrValue == attrValue:
                    result.append(key)
        print("Found keys are {}".format("".join(map(str, result))))
