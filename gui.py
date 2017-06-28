from flask import Flask
from flask import render_template
import os

interface_gui = os.path.join(os.path.join(os.path.dirname(os.path.abspath(__file__)), "libraries"), "gui_interface.txt")

app = Flask(__name__)

@app.route("/")
def hello():
    entries = {}
    servers = {}
    for task in open(interface_gui):
        if ":" in task:
            if "server" in task:
                tasked = task.split(":")
                task_stat = tasked[1]
                servers[tasked[0]] = task_stat
            elif "True" in task or "False" in task:
                tasked = task.split(":")
                if "True" in tasked[1]:
                    task_stat = "Work"
                else:
                    task_stat = "Error"
                entries[tasked[0]] = task_stat
    return render_template('index.html', entries=entries, servers=servers)

if __name__ == "__main__":
    app.run()
