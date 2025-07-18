import tkinter as tk

class GameFrame3(tk.Frame):
    
    def __init__(self, master):
        super().__init__(master)
        self["bg"] = "white"
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.found_letters_lbl = tk.Label(self, bg="white")
        self.found_letters_lbl.grid(row=1)
        self.tried_letters_lbl = tk.Label(self, bg="white")
        self.tried_letters_lbl.grid(row=2)
        self.life_intv = tk.IntVar(self, 8)
        self.life_lbl = tk.Label(self, bg="white")
        self.life_lbl.grid(row=0)
        self.tried_chars_stv = tk.StringVar(self, "Caractères déjà essayés : ")
        self.find_chars_stv = tk.StringVar(self, "Mot mystère : ")     