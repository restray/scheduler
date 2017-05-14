from tempfile import mkstemp
from shutil import move
from os import remove, close

class interface:
    def __init__(self, gui_interface, tmp_file):
        self.tmp_file = tmp_file
        self.gui_interface = gui_interface
    def read(self):
        self.file_interface = open(gui_interface, 'r')
        self.reading = self.file_interface.read()
        self.file_interface.close()
        return self.reading
    def write(self, component):
        self.file_interface_write = open(self.gui_interface, 'w')
        self.file_interface_write.write(component)
        self.file_interface_write.close()
    def append(self, component):
        self.file_interface_write = open(self.gui_interface, 'a')
        self.file_interface_write.write(component)
        self.file_interface_write.close()
    def change_value(self, to_change, value):
        #Create temp file
        self.fh, self.abs_path = mkstemp()
        with open(self.abs_path,'w') as new_file:
            with open(self.gui_interface) as old_file:
                for line in old_file:
                    new_file.write(line.replace(to_change, value))
        close(self.fh)
        #Remove original file
        remove(self.gui_interface)
        #Move new file
        move(self.abs_path, self.gui_interface)
    def close(self):
        self.file_interface.close()
