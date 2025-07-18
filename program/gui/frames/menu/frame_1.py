import tkinter as tk

class MenuFrame1(tk.Frame):
    
    def __init__(self, master):
        super().__init__(master)
        self.config(bg="red")
        self.header_lbl = tk.Label(self, text="Hanged Game", font=("default 16 bold"), bg="white")
        self.header_lbl.grid(row=0, column=0, ipady=50, ipadx="50")
        
        