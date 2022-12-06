from File import File


def getFileName(dirPath):
    return dirPath.split("/")[-1]

def getPath(prevPath, currDir):
    currPath = ""
    if prevPath == "/" or prevPath == "":
        currPath = "{}".format(currDir.getDirName())
    else:
        currPath = "{}/{}".format(prevPath, currDir.getDirName())
    return currPath

class FileSystemManager:
    rootDir = None

    def __init__(self, rootDir):
        self.__class__.rootDir = rootDir

    def getRootDirectory(self):
        return self.__class__.rootDir

    def mkdir(self, dirPath):
        currDir = self.getRootDirectory()
        pathList = dirPath.split("/")
        currPath = ""
        for dirName in pathList:
            currPath = "{}/{}".format(currPath, dirName)
            if currDir.getDir(dirName) is None:
                currDir.addDir(dirName, dirPath)
            currDir = currDir.getDir(dirName)
        return currDir

    def addContentToFile(self, dirPath, fileContent=None):
        fileName = getFileName(dirPath)
        currDir = self.mkdir(dirPath)
        currFile = currDir.getFile(fileName)
        if currFile is None:
            currDir.files[fileName] = File(fileName, fileContent)
        else:
            currFile = currDir.files[fileName]
            currFile.appendContent(fileContent)

    def getCurrentDirectory(self, dirPath):
        pathList = dirPath.split("/")
        currDir = self.getRootDirectory()
        for dirName in pathList:
            if currDir.getDir(dirName) is not None:
                currDir = currDir.getDir(dirName)
            else:
                raise BaseException("Path not exist")
        return currDir

    def ls(self, path=None):
        currDir = self.getRootDirectory()
        if path is not None:
            currDir = self.getCurrentDirectory(path)

        path = "" if path is None else path
        for directory in sorted(currDir.directories.keys()):
            print("{}/{}".format(path, directory))
        for file in sorted(currDir.files.keys()):
            print("{}/{}".format(path, file))

    def findFile(self, fileName, currDir, prevPath):
        filePathList = []
        for currDir in currDir.getAllDir().values():
            currPath = getPath(prevPath, currDir)
            fileExist = currDir.getFile(fileName)
            if fileExist:
                filePathList.append(currPath)
            res = self.findFile(fileName, currDir, currPath)
            if len(res) >= 1:
                filePathList.extend(res)
        return filePathList

    def lsFile(self, fileName):
        currDir = self.getRootDirectory()
        foundListPath = self.findFile(fileName, currDir, "")
        print(foundListPath)
        return foundListPath

    def readContentFromFile(self, path):
        currDir = self.getRootDirectory()
        fileName = getFileName(path)
        if path is not None:
            currDir = self.getCurrentDirectory(path)
        currFile = currDir.getFile(fileName)
        print(currFile.content)
