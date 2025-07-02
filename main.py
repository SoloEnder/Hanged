try:
    
    import getpass
    import tkinter as tk
    
except ImportError:
    print("Ce programme a besoin que les modules 'getpass' et 'tkinter' soient installés")
    exit()
    

print("Welcome to Hanged Game")
from program.game_styles.multi import multi_player

class Game:
    
    def multi(self):
        multi_player(self)
    
    def __init__(self):
        self.w = tk.Tk()
        
        # La frame pour la saisie de carractères et l'affichage des erreurs
        self.entry_errors_fr = tk.Frame(self.w)
        self.entry_errors_fr.grid(row=0, column=0)
        self.entry_lbl = tk.Label(self.entry_errors_fr, text="Entrez le mot que les autres joueurs devront deviner")
        self.entry_lbl.grid(row=0, pady=20, padx=10)
        self.entry_e = tk.Entry(self.entry_errors_fr, show="*")
        self.entry_e.grid(row=1)
        self.alph_error = tk.Label(self.entry_errors_fr)
        self.alph_error.grid(row=2)
        self.enter_b = tk.Button(self.entry_errors_fr, text="Next", command=self.multi)
        self.enter_b.grid(row=4, pady=10)
        self.error_lbl = tk.Label(self.entry_errors_fr, fg="red")
        self.error_lbl.grid(row=3)
        
        # Partie où sera dessiné le pendu
        self.pendu_fr = tk.Frame(self.w)
        self.pendu_fr.grid(row=1, column=0)
        self.pendu_cv = tk.Canvas(self.pendu_fr, width=200, height=200, bg="white")
        self.pendu_cv.grid(row=0, column=0, pady=20)
        self.w.mainloop()
Game()