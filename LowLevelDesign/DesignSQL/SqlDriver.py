
from DesignSQL.Database import Database
from DesignSQL.Sql import SQL
from DesignSQL.models import Driver

def SqlDriver():
    sql = SQL(Database("UBER"))
    sql.addTable("driver")
    sql.addRecord("driver", "id-1", Driver("id-1", "anoj"))
    sql.addRecord("driver", "id-2", Driver("id-2", "vinod"))
    sql.addRecord("driver", "id-3", Driver("id-3", "nitin"))
    recordSet = sql.getRecord("driver", ["id-3", "id-2"])
    for _ in recordSet:
        print("{}".format(_))


if __name__ == "__main__":
    SqlDriver()