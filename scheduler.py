import schedule
import time
import os
import sys
from import_file import import_file

#Other importation

sys.path.insert(0, "%s\\plugins\\"%(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, "%s\\libraries\\"%(os.path.dirname(os.path.abspath(__file__))))

import log

#------------------------------------------------------------------------------

print("Le Scheduler est démarré")

#------------------------------------------------------------------------------
# Initalisation des methodes pour charger les plugins

def load_plugin(name):
    mod = import_file(name)
    return mod

def call_plugin(name):
    try:
        plugin = load_plugin(name)
        plugin.plugin_main(os.path.dirname(os.path.abspath(__file__)))
        log1.append("Plugin %s is load"%(files[0:length-3]), "info")
    
    except:
        print("The plugin don\'t contain a plugin_main()")
        log1.append("Plugin %s isn't load : The plugin don\'t contain a plugin_main()"%(files[0:length-3]), "warning")
        

#------------------------------------------------------------------------------
def job1():
    try:
        print("working ever 10 min")
        log1.append('Task 1 run with success', 'Info')
    except:
        print("Task 1 error")
        log1.append('Task 1 run with problem', 'Warning')
        

def job2():
    try:
        print("working every hours")
        log1.append('Task 1 run with success', 'Info')
    except:
        print("Task 2 error")
        log1.append('Task 1 run with problem', 'Warning')
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
            print("Load %s"%(files[0:length-3]))
            log1.append("Start the plugin : %s"%(files[0:length-3]), "info")
            call_plugin(".\\plugins\\%s"%(files))
    
    try :
        while 1:
            schedule.run_pending()
            time.sleep(1)

    finally :
        log1.close()


