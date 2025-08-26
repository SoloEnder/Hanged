import tkinter as tk
from ....logics.utils import path_maker

class GameFrame4(tk.Frame):
    
   def __init__(self, master):
       super().__init__(master)
       self["bg"] = "white"
       self.columnconfigure(0, weight=1)
       self.rowconfigure(0, weight=1)
       
       self.victory_bov = tk.BooleanVar(self, False)
       self.victory_img_path = path_maker.make_path(__file__, "../../../assets/end_game/victory_crown.png")
       self.victory_img = tk.PhotoImage(file=self.victory_img_path) if self.victory_img_path != None else None
       self.defeat_img_path = path_maker.make_path(__file__, "../../../assets/end_game/defeat_skull.png")
       self.defeat_img = tk.PhotoImage(file=self.defeat_img_path) if self.defeat_img_path != None else None
       self.end_game_lb = tk.Label(self, bg="white")
       self.end_game_lb_2 = tk.Label(self, bg="white", text=" ")
       self.return_menu_b = tk.Button(self, text="Menu", command=self.master.switch_menu_fr)
       
   def end_game(self, hidden_word):
       
       if self.victory_bov.get() == True:
           self.end_game_lb.image = self.victory_img
           self.end_game_lb.config(image=self.victory_img, text="Bravo !", compound=tk.TOP, font=("default 14 bold"))
           
       else:
           self.end_game_lb.image = self.defeat_img
           self.end_game_lb.config(image=self.defeat_img, text="Vous êtes pendu !", compound=tk.TOP, font=("default 14 bold"))
           
       self.end_game_lb.grid(row=0, column=0)
       self.end_game_lb_2.config(text=f"Le mot mystère était '{hidden_word}'", font=("default 12 bold"))
       self.end_game_lb_2.grid(row=1, column=0, pady=40)
       self.return_menu_b.grid(row=2, column=0)
           