import tkinter as tk

class GameFrame2(tk.Frame):
    
    def __init__(self, master):
        super().__init__(master)
        self["bg"] = "white"
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.pendu_lb = tk.Label(self, bg="white")
        self.pendu_lb.grid()
             