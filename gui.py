from flask import Flask
from flask import render_template
import os

app = Flask(__name__)

@app.route("/")
def hello():
    entries = {}
    for task in open("%s\\libraries\\gui_interface.txt"%(os.path.dirname(os.path.abspath(__file__)))):
        if ":" in task:
            if "True" in task or "False" in task:
                tasked = task.split(":")
                if "True" in tasked[1]:
                    task_stat = "Work"
                else:
                    task_stat = "Error"
                entries[tasked[0]] = task_stat
    return render_template('index.html', entries=entries)

if __name__ == "__main__":
    app.run()
