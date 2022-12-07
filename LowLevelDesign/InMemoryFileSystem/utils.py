
def getFileName(dirPath):
    return dirPath.split("/")[-1]

def getPath(prevPath, currDir):
    currPath = ""
    if prevPath == "/" or prevPath == "":
        currPath = "{}".format(currDir.getDirName())
    else:
        currPath = "{}/{}".format(prevPath, currDir.getDirName())
    return currPath