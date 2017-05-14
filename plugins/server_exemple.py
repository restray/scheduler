import log
import interface_gui
import schedule
import os
from random import randint

def plugin_main(logs_dir, interface):
    # Definition variables
    plugin_folder = "%s\\plugins\\server_exemple\\"%(os.path.dirname(os.path.abspath(__file__)))
    config_file = '%sconfig.txt'%(plugin_folder)

    # Démarrage des services de logs
    Log_ex = log.Log("Server Exemple", logs_dir)
    Log_ex.append("Plugin loaded", "info")
    print("[exemple_server]start Plugin")

    # Check du service de config
    # Vérification du dossier
    if not os.path.exists(plugin_folder):
        os.makedirs(plugin_folder)
    # Vérification du fichier
    if not os.path.exists(config_file):
        start_pl = False
        print('No config file : plugin will not start.')
        Log_ex.append("No config file : plugin will not start.", "warn")
        config = open(config_file, 'w')
        config.write("""# Configuration file
server_name : exemple
port : 1234
pass : 0123456789""")
        config.close()
    else:
        start_pl = True
        print('Config file found, plugin start')
        Log_ex.append("Config file found, start plugin", "info")
        config = open(config_file, 'r')
        modify_config = open(config_file, 'w')

    # Create schedule task
    def job_server_exemple():
        conf = ""
        Stat_server = randint(0, 2)
        if start_pl:
            if Stat_server==0:
                Stat_server="starting"
            elif Stat_server==1:
                Stat_server="start"
            elif Stat_server==2:
                Stat_server="stop"
            interface.change_value("server_exemple", "server_exemple : %s"%(Stat_server))
            Log_ex.append("Task do with success", "info")
            print("Restart server exemple")
    schedule.every().minute.do(job_server_exemple)
