import log
import schedule
import os

def plugin_main(logs_dir, interface_file):
    # Definition variables
    plugin_folder = "%s\\plugins\\exemple_plugin\\"%(os.path.dirname(os.path.abspath(__file__)))
    config_file = '%sconfig.txt'%(plugin_folder)

    # Démarrage des services de logs
    Log_ex = log.Log("Plugin Exemple", logs_dir)
    Log_ex.append("Plugin loaded", "info")
    print("[exemple_plugin]start Plugin")

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

    # Create schedule task
    def job():
        if start_pl:
            Log_ex.append("Task do with success", "info")
            print("coucou")
    schedule.every().minute.do(job)
