import schedule
import time
import os
import sys
from import_file import import_file
from Tkinter import *
from threading import Thread
from string import printable
from curses import erasechar, wrapper

#Other importation

sys.path.insert(0, "%s\\plugins\\"%(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, "%s\\libraries\\"%(os.path.dirname(os.path.abspath(__file__))))

import log

#------------------------------------------------------------------------------

print("Le Scheduler est démarré")
gui_active = False
PRINTABLE = map(ord, printable)

#------------------------------------------------------------------------------
# Initalisation des methodes pour charger les plugins

# plugin_folder = "%s\\plugins\\"%(os.path.dirname(os.path.abspath(__file__)))

def load_plugin(name):
    mod = import_file(name)
    return mod

def call_plugin(name):
    try:
        plugin = load_plugin(name)
        plugin.plugin_main(os.path.dirname(os.path.abspath(__file__)))
        log1.append("Plugin %s is load"%(files[0:length-3]), "info")
        return True
    except:
        print("The plugin don\'t contain a plugin_main()")
        log1.append("Plugin %s isn't load : The plugin don\'t contain a plugin_main()"%(files[0:length-3]), "warning")
        return False

#------------------------------------------------------------------------------
# Configuration des jobs


#------------------------------------------------------------------------------

if sys.argv[1] == "-h" or sys.argv[1] == "help":
    print("Pour faire tourner le serveur utiliser: run")
    print("Pour faire tourner une tâche particulière: run_task [task]")

elif sys.argv[1] == "-r" or sys.argv[1] == "run":
    #---------------------------------------------------------------------------
    # Initialisation des logs
    log1 = log.Log("Schedule task", os.path.dirname(os.path.abspath(__file__)))

    log1.write("Start task", "Info")
    #---------------------------------------------------------------------------
    # Chargement des plugins

    for files in os.listdir(".\\plugins\\"):
        #Check if the file is a python file
        length = len(files)
        check_py_file = files[length-3:length]
        if check_py_file == ".py":
            gui_interface = open("%s\\libraries\\gui_interface.txt"%(os.path.dirname(os.path.abspath(__file__))), "w")
            print("Load %s"%(files[0:length-3]))
            log1.append("Start the plugin : %s"%(files[0:length-3]), "info")
            if call_plugin(".\\plugins\\%s"%(files)):
                gui_interface.write("%s: True"%(files[0:length-3]))
            else:
                gui_interface.write("%s: False"%(files[0:length-3]))
            gui_interface.close()

    try :
        while 1:
            schedule.run_pending()
            time.sleep(1)

    finally :
        log1.close()
