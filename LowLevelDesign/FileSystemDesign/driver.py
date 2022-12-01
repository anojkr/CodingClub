from FileSystemDesign.Directory import Directory
from FileSystemDesign.File import File

"""
    FileSystem Implementation used composite design pattern
"""


def driver():
    base = Directory("Movies")
    comedy = Directory("Comedy")
    comedy.add(File("all the best"))
    comedy.add(File("golmal"))
    action = Directory("Action")
    action.add(File("avenger"))
    action.add(File("thor"))
    romance = Directory("Romance")
    romance.add(File("deewaana"))
    romance.add(File("rehna h tere dil me"))
    base.add(comedy)
    base.add(action)
    base.add(romance)
    base.ls()
    print("\n")
    base.delete("Com")
    base.delete("Comedy")
    base.ls()


if __name__ == "__main__":
    driver()
