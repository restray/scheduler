import log
import schedule

def plugin_main(logs_dir):
    Log_ex = log.Log("Plugin Exemple", logs_dir)
    Log_glm.append("Plugin loaded", "info")
    print("start Plugin")
    def job():
        Log_glm.append("Task do with success", "info")
        print("coucou")
    schedule.every().minute.do(job)
    
