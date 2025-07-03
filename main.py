try:
    
    import getpass
    import tkinter as tk
    from tkinter.messagebox import askyesno
    
except ImportError:
    print("Ce programme a besoin que les modules 'getpass' et 'tkinter' soient installés")
    exit()
    

print("Welcome to Hanged Game")

from program.game_styles.multi import multi_player

class Game:
    
    def multi(self):
        multi_player(self, tk)
        
    def quit_game(self):
        exit_confirm = askyesno(message="Voulez vous vraiment quitter ?")
        
        if exit_confirm == True:
            self.w.destroy()
    
    def __init__(self):
        self.w = tk.Tk()
        self.w.protocol("WM_DELETE_WINDOW", self.quit_game)
        
        # La frame pour la saisie de carractères et l'affichage des erreurs
        self.entry_errors_fr = tk.Frame(self.w)
        self.entry_errors_fr.grid(row=0)
        self.entry_lbl = tk.Label(self.entry_errors_fr, text="Entrez le mot que les autres joueurs devront deviner", width=80)
        self.entry_lbl.grid(row=0, pady=20, padx=10)
        self.entry_e = tk.Entry(self.entry_errors_fr, show="*")
        self.entry_e.grid(row=1)
        self.alph_error = tk.Label(self.entry_errors_fr)
        self.alph_error.grid(row=2)
        self.enter_b = tk.Button(self.entry_errors_fr, text="Entrer", command=self.multi)
        self.enter_b.grid(row=4, pady=10)
        self.error_lbl = tk.Label(self.entry_errors_fr, fg="red")
        self.error_lbl.grid(row=3)
        
        # Partie où sera dessiné le pendu
        self.pendu_fr = tk.Frame(self.w)
        self.pendu_fr.grid(row=1, column=0)
        self.pendu_cv = tk.Canvas(self.pendu_fr, width=350, height=300, bg="white")
        self.pendu_cv.grid(pady=20)
        
        # Partie où seront affichées des infos
        self.infos_fr = tk.Frame(self.w)
        self.infos_fr.grid(row=2)
        self.hidden_word_lbl = tk.Label(self.infos_fr)
        self.tried_letters_lbl = tk.Label(self.infos_fr)
        self.life_intv = tk.IntVar(self.w, 8)
        self.life_lbl = tk.Label(self.infos_fr)
        
        self.w.mainloop()
        
Game()
