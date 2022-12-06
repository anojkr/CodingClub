from InMemoryFileSystem.FileSystem import FileSystem


class File(FileSystem):

    def __init__(self, fileName, fileContent=None):
        self.name = fileName
        self.content = fileContent

    def appendContent(self, newContent):
        self.content = self.content + "\n" + newContent

