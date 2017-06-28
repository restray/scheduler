# coding: utf-8

import os

class Config:
    def __init__(self, plugin_folder, plugin_name):
        self.plugin_folder = os.path.join(plugin_folder, plugin_name)
        self.config_file = os.path.join(self.plugin_folder, "config.txt")

        # Vérification du Dossier plugin
        if not os.path.exists(plugin_folder):
            os.makedirs(plugin_folder)

        # Vérification du Dossier du plugin
        if not os.path.exists(self.plugin_folder):
            os.makedirs(self.plugin_folder)

        # Vérification du fichier
        if not os.path.exists(self.config_file):
            self.file_to_create = open(self.config_file, "w")
            self.file_to_create.write("#Configuration file for the project %s\n"%(plugin_name))
            self.file_to_create.close()

    def append(self, value):
        self.file = open(self.config_file, "a")
        self.file.write("%s\n"%(value))
        self.file.close()

    def read_value(self):
        self.reponse = {}
        self.file = open(self.config_file, "r")
        self.all_line = self.file.readlines()
        for self.line in self.all_line:
            if ":" in self.line and "#" not in self.line:
                self.line_info = self.line.split(":")
                self.reponse[self.line_info[0]] = self.line_info[1].rstrip().replace(" ", "")
        self.file.close()
        return self.reponse
