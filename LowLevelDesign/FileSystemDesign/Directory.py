from FileSystemDesign.FileSystem import FileSystem


class Directory(FileSystem):

    def __init__(self, directoryName):
        self.name = directoryName
        self.fileSystem = {}

    def add(self, obj: FileSystem):
        self.fileSystem[obj.name] = obj

    def delete(self, name):
        fileSysObj = self.fileSystem.get(name)
        if fileSysObj:
            self.fileSystem.pop(name)
        else:
            print("No file or directory present with name={}".format(name))

    def ls(self):
        print("DirectoryName: {}".format(self.name))
        for obj in self.fileSystem.values():
            obj.ls()
