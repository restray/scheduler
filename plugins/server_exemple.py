import log
import interface_gui
import schedule
import os
from random import randint

# From local libraries
import configuration

class plugin_main:
    def __init__(self, logs_dir, interface):
        # Definition variables
        self.plugin_folder = "%s\\plugins\\server_exemple\\"%(os.path.dirname(os.path.abspath(__file__)))
        self.config_file = '%sconfig.txt'%(self.plugin_folder)
        # Démarrage des services de logs
        self.Log_ex = log.Log("Server Exemple", logs_dir)
        self.Log_ex.append("Plugin loaded", "info")
        print("[server_exemple]start Plugin")

        self.configuration = configuration.Config("%s\\plugins\\"%(os.path.dirname(os.path.abspath(__file__))), "server_exemple")
        self.interface = interface

        # Check du service de config
        # Vérification du dossier
        if not self.configuration.read_value():
            self.start_pl = False
            self.Log_ex.append("No config file : plugin will not start.", "warn")
            self.configuration.append("server_name: exemple")
            self.configuration.append("ip: 0.0.0.0")
            self.configuration.append("port: 1234")
            self.configuration.append("pass: 0123456789")
        #Create value in the config file if missing
        if "server_name" not in self.configuration.read_value():
            self.start_pl = False
            self.configuration.append("server_name: exemple")
            self.Log_ex.append("Config file found but argument missing, creating.", "warn")
        if "ip" not in self.configuration.read_value():
            self.start_pl = False
            self.configuration.append("ip: 0.0.0.0")
            self.Log_ex.append("Config file found but argument missing, creating.", "warn")
        if "port" not in self.configuration.read_value():
            self.start_pl = False
            self.configuration.append("port: 1234")
            self.Log_ex.append("Config file found but argument missing, creating.", "warn")
        if "pass" not in self.configuration.read_value():
            self.start_pl = False
            self.configuration.append("pass: 0123456789")
            self.Log_ex.append("Config file found but argument missing, creating.", "warn")
        #Else we start
        else:
            self.start_pl = True
            self.ip_port = "%s:%s"%(self.configuration.read_value()['ip'], self.configuration.read_value()['port'])
            print("[server_exemple] Config file, plugin launch")
            print("[server_exemple] Start the server on : %s"%(self.ip_port))
            self.Log_ex.append("Config file found", "info")

        schedule.every().minute.do(self.job_server_exemple)

    # Create schedule task
    def job_server_exemple(self):
        #Generate a random key for exemple
        self.Stat_server = randint(0, 2)

        #Check if the plugin run if the plugin had already a config.txt at the wake up
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
