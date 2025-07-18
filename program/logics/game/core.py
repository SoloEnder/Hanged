import json
from tkinter.messagebox import showinfo
import tkinter as tk
alph = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZzàäéèêëÿùç-'"

hidden_word_list = []
find_list = []
tried_letters = []
hidden_word = ""

def get_hidden_word_str(self, find_list):
    find_chars = " ".join(find_list)    
    self.master.gf3.find_chars_stv.set(f"Mot mystère : {find_chars}")

def hanged(self):
    global hidden_word_list
    global find_list
    global tried_letters
    find_list = []
    tried_letters = []
    hidden_word_list = []
    global hidden_word 
    hidden_word = self.entry_e.get()                       
    alph_error = False
            
    if len(hidden_word) > 0:
                
        for c in hidden_word:
                    
            if c in alph:
                hidden_word_list.append(c)
                find_list.append("_")
                        
            else:
                alph_error = True
                        
        if alph_error == False:
            self.switch_widgets_1()
            self.master.gf3.found_letters_lbl.config(textvariable=self.master.gf3.find_chars_stv)
            self.master.gf3.tried_letters_lbl.config(textvariable=self.master.gf3.tried_chars_stv)
            get_hidden_word_str(self, find_list)
                                                       
        else:
            self.error_lbl.config(text="Caractère non autorisé")
                
    else:
        self.error_lbl.config(text="Vous devez entrer un mot")
        
def true_hanged(self):
    self.master.game_in_progress = True
    find = False
    tried_letter = self.entry_e.get()
    self.entry_e.delete(0, tk.END)
            
    if len(tried_letter) == 1 and tried_letter in alph:
                
        if tried_letter not in tried_letters:
            self.error_lbl.config(text="")
            tried_letters.append(tried_letter)
            self.master.gf3.tried_chars_stv.set(self.master.gf3.tried_chars_stv.get() + tried_letter + ", ")
                    
            for index, c in enumerate(hidden_word_list):
                        
                if c == tried_letter:
                    find_list[index] = c
                    find = True
                            
            if find == True:
                self.error_lbl.config(text=f"La lettre {tried_letter} est dans le mot mystère", fg="green")
                        
            else:
                self.error_lbl.config(text=f"La lettre {tried_letter} n'est pas dans le mot mystère", fg="red")
                self.master.gf3.life_intv.set(self.master.gf3.life_intv.get() - 1)
                pendu_img = tk.PhotoImage(file=f"program/assets/pendu/{self.master.gf3.life_intv.get()}.png")
                self.master.gf2.pendu_lb.image = pendu_img
                self.master.gf2.pendu_lb.config(image=pendu_img)
                        
                if self.master.gf3.life_intv.get() == 0:
                    self.master.game_in_progress = False
                    self.master.switch_end_game_fr(hidden_word)
                                                
            if find_list == hidden_word_list:
                self.master.game_in_progress = False
                self.master.gf4.victory_bov.set(True)
                self.master.switch_end_game_fr(hidden_word)
                        
        else:
            self.error_lbl.config(text="Vous avez déjà entré cette lettre !", fg="red")
                
    
    else:
        self.error_lbl.config(text="Caractère non autorisé", fg="red")
        
    get_hidden_word_str(self, find_list)