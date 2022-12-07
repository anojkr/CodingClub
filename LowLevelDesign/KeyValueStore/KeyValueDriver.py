
from KeyValueStore.Database import Database

def driver():
    kvStore = Database()
    kvStore.put("car", {})
    kvStore.get("car")



if __name__ == "__main__":
    driver()