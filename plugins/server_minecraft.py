# coding: utf8

import rcon_mc.rcon
import rcon_mc.lib.msocket

import socket;

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
        self.plugin_folder = "%s\\plugins\\server_minecraft\\"%(os.path.dirname(os.path.abspath(__file__)))
        self.config_file = '%sconfig.txt'%(self.plugin_folder)
        # Démarrage des services de logs
        self.Log_ex = log.Log("Server Minecraft", logs_dir)
        self.Log_ex.append("Plugin loaded", "info")
        print("[server_Minecraft]start Plugin")

        self.configuration = configuration.Config("%s\\plugins\\"%(os.path.dirname(os.path.abspath(__file__))), "server_minecraft")
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
            print("[server_Minecraft] Config file, plugin launch")
            print("[server_Minecraft] Start the plugin with the server on : %s"%(self.ip_port))
            self.Log_ex.append("Config file found", "info")

            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.result = self.sock.connect_ex((self.configuration.read_value()['ip'], int(self.configuration.read_value()['port'])))

            if self.result == 0:
                self.start_pl = True
                print("[server_Minecraft]Your server is ok...")
            else:
                self.start_pl = False
                print("[server_Minecraft]Your server is broken or the port is not open...")
        schedule.every().minute.do(self.job_server_minecraft)

    # Create schedule task
    def job_server_minecraft(self):
        #Check if the plugin run if the plugin had already a config.txt at the wake up
        if self.start_pl:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.result = self.sock.connect_ex((self.configuration.read_value()['ip'], int(self.configuration.read_value()['port'])))
            if self.result == 0:
                self.Stat_server="start"
                client=rcon_mc.rcon.client(self.configuration.read_value()['ip'], int(self.configuration.read_value()['port']), self.configuration.read_value()['pass'])
                response=client.send("/msg restray message envoyé depuis le scheduler !")
                print response
            else:
                self.Stat_server="stop"
                print('[Server Minecraft]Your server is stopped...')
            self.interface.change_value("server_minecraft", "server_minecraft : %s"%(self.Stat_server))
            self.Log_ex.append("Task do with success", "info")
