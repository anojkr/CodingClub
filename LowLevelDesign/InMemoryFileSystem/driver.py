from FileSystemDesign.Directory import Directory
from FileSystemDesign.File import File

"""
    Reference: https://jerry4013.github.io/Github-blog/2020/08/03/LeetCode-588.html
    FileSystem Implementation used composite design pattern
    Supported Action
        - mkDir : Create new directory
        - addContentToFile: add new file to directory or change content of file
        - ls : show list of files and directories in mentioned path
        - readContentFromFile: view content of file
"""
from FileSystemManager import FileSystemManager
from InMemoryFileSystem.Directory import Directory


def driver():
    fileSystem = FileSystemManager(Directory("/", "/"))
    root = fileSystem.getRootDirectory()
    fileSystem.mkdir("/MOVIES")
    fileSystem.mkdir("/MOVIES/TEST/FIR")
    fileSystem.addContentToFile("/MOVIES/TEST/readme.txt", "read subtitle")
    fileSystem.readContentFromFile("/MOVIES/TEST/readme.txt")
    fileSystem.addContentToFile("/MOVIES/TEST/readme.txt", "write subtitle")
    fileSystem.mkdir("MOVIES/ACTION/AVENGER")
    fileSystem.addContentToFile("MOVIES/ACTION/AVENGER/Ultron/readme.txt", "read subtile")
    fileSystem.addContentToFile("MOVIES/ACTION/AVENGER/EndGame/readme.txt", "write subtile")
    # fileSystem.ls("MOVIES/ACTION/AVENGER")
    # fileSystem.ls("/MOVIES/TEST")
    # fileSystem.lsFile("readme.txt")
    # fileSystem.readContentFromFile("/MOVIES/TEST/readme.txt")
    fileSystem.move("/MOVIES/TEST", "MOVIES/ACTION/AVENGER")
    fileSystem.ls("/MOVIES")
    fileSystem.ls("MOVIES/ACTION/AVENGER/TEST")



if __name__ == "__main__":
    driver()
