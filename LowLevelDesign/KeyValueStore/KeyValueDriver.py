
from KeyValueStore.Database import Database
from KeyValueStore.models.AttributeFactoryManager import AttributeFactoryManager as AFM
import utils
def driver():
    kvStore = Database()
    kvStore.put("car", {"bmw": AFM.getValue(300), "jeep": AFM.getValue(False), "maruti": AFM.getValue("tr")})
    kvStore.put("test", {"bmw": AFM.getValue(300), "jeep": AFM.getValue(False), "maruti": AFM.getValue("tr")})
    utils.getAttribute(kvStore.get("car"))
    kvStore.search("bmw", 300)

if __name__ == "__main__":
    driver()