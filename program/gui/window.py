import tkinter as tk
from tkinter.messagebox import askyesno
from program.gui.frames.game.frame_1 import GameFrame1
from program.gui.frames.game.frame_2 import GameFrame2
from program.gui.frames.game.frame_3 import GameFrame3
from program.gui.frames.game.frame_4 import GameFrame4
from program.gui.frames.menu.frame_1 import MenuFrame1
from program.gui.frames.menu.frame_2 import MenuFrame2
from program.gui.frames.about.frame_1 import AboutFrame1

class Window(tk.Tk):
    """Link all frame in this class and init the window
        - Menu frames
        - Game frames
    """
    
    def __init__(self):
        super().__init__()
        self.title("Hanged Game")
        self.geometry("700x750")
        self.resizable(False, False)
        self.config(bg="white")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.protocol("WM_DELETE_WINDOW", self.exit_app)
        self.game_in_progress = False
        
    def switch_menu_fr(self):
        attr_list = ["g1", "gf2", "gf3", "gf4"]
        
        if hasattr(self, "gf1"):
            self.gf1.destroy()
            
        if hasattr(self, "gf2"):
            self.gf2.destroy()
            
        if hasattr(self, "gf3"):
            self.gf3.destroy()
            
        if hasattr(self, "gf4"):
            self.gf4.destroy()
            
        self.mf1 = MenuFrame1(self)
        self.mf1.grid(row=0, column=0)
        self.mf2 = MenuFrame2(self)
        self.mf2.grid(row=1, column=0)
        
    def switch_game_fr(self):
        self.mf1.destroy()
        self.mf2.destroy()
        self.gf1 = GameFrame1(self)
        self.gf1.grid(row=0, column=0, sticky="new")
        self.gf2 = GameFrame2(self)
        self.gf2.grid(row=1, column=0, sticky="new")
        self.gf3 = GameFrame3(self)
        self.gf3.grid(row=2, column=0, sticky="new")
        self.gf4 = GameFrame4(self)
        
    def switch_end_game_fr(self, hidden_word):
        self.gf1.destroy()
        self.gf2.destroy()
        self.gf3.destroy()
        self.gf4.grid(row=0, column=0, sticky="nsew")
        self.gf4.end_game(hidden_word)
        
    def switch_about_fr(self):
        self.mf1.destroy()
        self.mf2.destroy()
        self.af1 = AboutFrame1(self)
        self.af1.grid(row=0, column=0, sticky="nsew")
        
        
    def exit_app(self):
        
        if self.game_in_progress == True:
            exit_app_confirm = askyesno(message="Une partie est en cours. Si vous la quittez, vous la perdrez. Voulez vous quitter ?")
            
        else:
            exit_app_confirm = askyesno(message="Voulez vous vraiment quitter ?")
            
        if exit_app_confirm == True:
            self.destroy()
        