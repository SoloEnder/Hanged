import tkinter as tk
from tkinter.messagebox import askokcancel
from program.logics.game.core import hanged, true_hanged

class GameFrame1(tk.Frame):
    
    # This class contain widgets for entry word/letter and show errors
    
    def __init__(self, master):
        super().__init__(master)
        self["bg"] = "white"
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.return_b = tk.Button(self, text="<--", bg="white", relief="flat", command=self.return_menu_fr)
        self.return_b.grid(row=0, column=0, sticky="w")
        self.entry_lbl = tk.Label(self, text="Entrez le mot que les autres joueurs devront deviner", bg="white")
        self.entry_lbl.grid(row=1, ipady=10, column=0, ipadx=20)
        self.entry_e = tk.Entry(self, show="*")
        self.entry_e.grid(row=2, column=0)
        self.alph_error = tk.Label(self, bg="white")
        self.alph_error.grid(row=3, column=0)
        self.enter_b = tk.Button(self, text="Entrer", command=lambda: hanged(self))
        self.enter_b.grid(row=5, column=0)
        self.error_lbl = tk.Label(self, fg="red", bg="white")
        self.error_lbl.grid(row=4, column=0)
        
    def switch_widgets_1(self):
        """Configure the widget for the game start"""
        
        self.error_lbl.config(text="")
        self.master.gf3.life_lbl.config(textvariable=self.master.gf3.life_intv)
        self.enter_b.config(command=lambda: true_hanged(self))
        self.entry_lbl.config(text="Essayez de deviner une lettre")
        self.entry_e.config(show="")
        self.entry_e.delete(0, tk.END)
        
    def return_menu_fr(self):
        conf = askokcancel(message="Si vous retournez au menu, tous les progrès seront perdus !")
        
        if conf == True:
           self.master.switch_menu_fr()
           