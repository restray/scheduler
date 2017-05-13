from Tkinter import * 

class GUI:
    def __init__(self):
        self.fenetre = Tk()
        self.fenetre.title("Scheduler")
        self.t = Text(self.fenetre)
        self.t.grid()
        self.t.insert(0.0, "Le scheduler s\'allume\n")
        self.t.insert(0.0, "Demarrage des plugins\n")
        # Just make sure you disable it AFTER you put the text in
        self.t["state"] = DISABLED
        self.t.pack()

        self.fenetre.mainloop()

    def insert_text(self, text):
        self.t.insert(0.0, "%s\n"%(text))
        self.fenetre.update()

    def __exit__(self):
        self.fenetre.destroy()
