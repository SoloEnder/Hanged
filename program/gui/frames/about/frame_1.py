import tkinter as tk
import json
from program.logics.about.get_version_infos import get_vinfos
from program.logics.about.open_link import open_link_f

class AboutFrame1(tk.Frame):
    
    def __init__(self, master):
        super().__init__(master)
        self["bg"] = "white"
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(1, weight=1)
        
        self.game_icon_img = tk.PhotoImage(file="program/assets/pendu/0.png")
        self.game_title_lb = tk.Label(self)
        self.game_title_lb.image = self.game_icon_img
        vinfos = get_vinfos()
        self.game_title_lb.config(
                                                    image=self.game_icon_img, 
                                                    text=f"""Hanged Game
v{vinfos["current_version"]["exact"] if vinfos is not None else "unknown version"}""", 
                                                    compound=tk.LEFT, 
                                                    font=("default 14"),
                                                    bg="white"
                                                    )
        self.game_title_lb.grid(row=0, column=0)
        
        self.releases_link_b = tk.Button(self, text="Toutes les versions", command=lambda: open_link_f("https://github.com/SoloEnder/Hanged/releases"))
        self.releases_link_b.grid(row=1, column=0, sticky="w", padx=50)
        self.git_page_b = tk.Button(self, text="Page du projet", command=lambda: open_link_f("https://github.com/SoloEnder/Hanged/"))
        self.git_page_b.grid(row=1, column=0, sticky="e")
        self.master.switch_menu_fr()
            