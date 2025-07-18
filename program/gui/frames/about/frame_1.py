import tkinter as tk

class AboutFrame1(tk.Frame):
    
    def __init__(self, master):
        super().__init__(master)
        self["bg"] = "white"
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        
        self.game_icon_img = tk.PhotoImage(file="program/assets/pendu/0.png")
        self.game_title_lb = tk.Label(self)
        self.game_title_lb.image = self.game_icon_img
        self.game_title_lb.config(image=self.game_icon_img, text="Hanged Game", compound=tk.LEFT, font=("default 13 bold"))
        self.game_title_lb.grid(row=0, column=0)
         