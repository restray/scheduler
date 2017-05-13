from Tkinter import *
import time
import os

class SampleApp(Tk):
    def __init__(self, *args, **kwargs):
        self.change = "Stats"

        Tk.__init__(self, *args, **kwargs)
        self.geometry('{}x{}'.format(768, 400))
        self.t = Text(self)
        self.t.grid()
        self.update()

        self.bouton_quitter = Button(self, text="Refresh", command=self.update_clock)
        self.bouton_quitter.pack(side="right")

    def update_clock(self):

        self.i = 0

        self.t.destroy()

        self.t = Text(self)
        self.t.grid()

        self.gui_interface = open("%s\\libraries\\gui_interface.txt"%(os.path.dirname(os.path.abspath(__file__))), "r")
        self.num_lines = sum(1 for line in open("%s\\libraries\\gui_interface.txt"%(os.path.dirname(os.path.abspath(__file__)))))
        for line in self.gui_interface:
            if self.i == self.num_lines-1:
                self.t.insert(0.0, "%s\n"%(line))
                self.i += 1
            else:
                self.t.insert(0.0, "%s"%(line))
                self.i+=1

        self.t["state"] = DISABLED
        self.gui_interface.close()
        self.update()

if __name__== "__main__":
    app = SampleApp()
    app.mainloop()
