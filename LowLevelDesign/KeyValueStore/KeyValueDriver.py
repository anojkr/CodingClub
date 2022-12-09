
from KeyValueStore.Database import Database
from KeyValueStore.models.AttributeFactoryManager import AttributeFactoryManager
from KeyValueStore.AttributeService import AttributeService
import utils
def driver():
    kvStore = Database()
    attrService = AttributeService(AttributeFactoryManager())
    kvStore.put("car", {"bmw": attrService.getAttributeValue(300), "jeep": attrService.getAttributeValue(False), "maruti": attrService.getAttributeValue("TFM")})
    kvStore.put("test", {"bmw": attrService.getAttributeValue(300), "jeep": attrService.getAttributeValue(False), "maruti": attrService.getAttributeValue("STM")})
    utils.getAttribute(kvStore.get("car"))
    # print(kvStore.get("car"))
    kvStore.search("bmw", 300)

if __name__ == "__main__":
    driver()