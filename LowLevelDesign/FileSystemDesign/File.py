from FileSystemDesign.FileSystem import FileSystem


class File(FileSystem):

    def __init__(self, fileName):
        self.name = fileName

    def ls(self):
        print("FileName: {}".format(self.name))
