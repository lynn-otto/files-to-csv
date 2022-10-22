import os
import Argument

class Folder:

    def __init__(self, path = os.curdir, filetypes = [], arguments = []):
        self.path = path
        self.filetypes = filetypes
        self.arguments = arguments

    @property
    def filetypes(self):
        return self._filetypes
    
    @filetypes.setter
    def filetypes(self, new_filetypes):
        self._filetypes = ['.'+ type for type in new_filetypes]
        self.filetypes_caps = [type.upper() for type in self._filetypes]


    def check_type(self, file):
        for i in range(len(self.filetypes)):
            if file.endswith(self.filetypes[i]) or file.endswith(self.filetypes_caps[i]):
                return True
        return False


    def add_arguments(self, file):
        added_arguments = [file]
        for argument in self.arguments:
            added_arguments.append(argument.find_argument(file))
        return added_arguments


    def create_filenames_and_arugments(self):
        filenames_and_arguments = []
        os.chdir(self.path)
        for file in os.listdir():
            if self.check_type(file):
                filenames_and_arguments.append(self.add_arguments(file))
        self.filenames_and_arguments = filenames_and_arguments
        return filenames_and_arguments

