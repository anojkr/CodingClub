from FileSystem import FileSystem
from File import File


class Directory(FileSystem):

    def __init__(self, directoryName, dirPath):
        self.name = directoryName
        self.files = {}
        self.dirPath = dirPath
        self.directories = {}

    def getDirName(self):
        return self.name

    def getDirPath(self):
        return self.dirPath

    def getAllDir(self):
        return self.directories

    def getAllFiles(self):
        return self.files

    def getDir(self, dirName):
        return self.directories.get(dirName)

    def addDir(self, dirName, dirPath):
        self.directories[dirName] = Directory(dirName, dirPath)
        return self.getDir(dirName)

    def addFile(self, fileName):
        self.files[fileName] = File(fileName)

    def getFile(self, fileName):
        return self.files.get(fileName)
