import os
from datetime import datetime

class Log:
    def __init__(self, appname, path):
        self.path_log = os.path.join(path, "logs\\")
        if not os.path.exists(self.path_log):
            os.makedirs(self.path_log)
        self.path = os.path.join(path, r"logs\\latest.txt")
        self.appname = appname
        self.date = datetime.now()

    def write(self, text, state):
        f = open(self.path, "w")
        f.write('%s - [%s][%s]%s\n'%(datetime.now(), state, self.appname, text))
        f.close()
    def append(self, text, state):
        f = open(self.path, "a")
        f.write('%s - [%s][%s]%s\n'%(datetime.now(), state, self.appname, text))
        f.close()
            
    def space(self):
        f = open(self.path, "a")
        f.write(' \n')
        f.close()
    def close(self):
        os.rename(self.path, "logs\\%s.txt"%(self.date.strftime("%d-%m-%y_%H-%M-%S")))
