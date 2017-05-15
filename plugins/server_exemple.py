import log
import interface_gui
import schedule
import os
from random import randint


class plugin_main:
    def __init__(self, logs_dir, interface):
        # Definition variables
        self.plugin_folder = "%s\\plugins\\server_exemple\\"%(os.path.dirname(os.path.abspath(__file__)))
        self.config_file = '%sconfig.txt'%(self.plugin_folder)
        # Démarrage des services de logs
        self.Log_ex = log.Log("Server Exemple", logs_dir)
        self.Log_ex.append("Plugin loaded", "info")
        print("[exemple_server]start Plugin")

        self.interface = interface

        # Check du service de config
        # Vérification du dossier
        if not os.path.exists(self.plugin_folder):
            os.makedirs(self.plugin_folder)
        # Vérification du fichier
        if not os.path.exists(self.config_file):
            self.start_pl = False
            print('No config file : plugin will not start.')
            self.Log_ex.append("No config file : plugin will not start.", "warn")
            self.config = open(config_file, 'w')
            self.config.write("""# Configuration file
server_name : exemple
port : 1234
pass : 0123456789""")
            self.config.close()
        else:
            self.start_pl = True
            print('Config file found, plugin start')
            self.Log_ex.append("Config file found, start plugin", "info")
            self.config = open(self.config_file, 'r')
            self.modify_config = open(self.config_file, 'w')

        schedule.every().minute.do(self.job_server_exemple)

    # Create schedule task
    def job_server_exemple(self):
        self.conf = ""
        self.Stat_server = randint(0, 2)
        if self.start_pl:
            if self.Stat_server==0:
                self.Stat_server="starting"
            elif self.Stat_server==1:
                self.Stat_server="start"
            elif self.Stat_server==2:
                self.Stat_server="stop"
            self.interface.change_value("server_exemple", "server_exemple : %s"%(self.Stat_server))
            self.Log_ex.append("Task do with success", "info")
            print("Restart server exemple")
