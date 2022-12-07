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

    def addDir(self, dirName, dirPath):
        self.directories[dirName] = Directory(dirName, dirPath)
        return self.getDir(dirName)

    def getDir(self, dirName):
        return self.directories.get(dirName)

    def delDir(self, dirName):
        dir = self.directories.get(dirName)
        self.directories.pop(dirName)
        return dir

    def moveDir(self, dirName, directoryObj):
        self.directories[dirName] = directoryObj
        return self.getDir(dirName)

    def addFile(self, fileName):
        self.files[fileName] = File(fileName)

    def getFile(self, fileName):
        return self.files.get(fileName)

    def moveFile(self, fileName, fileObj):
        self.files[fileName] = fileObj

    def delFile(self, fileName):
        file = self.files.get(fileName)
        self.files.pop(fileName)
        return file


