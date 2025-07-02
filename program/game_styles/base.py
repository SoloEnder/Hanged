import json
from tkinter.messagebox import*
alph = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZzàäéèêëÿùç-'"

def base(func):
    
    def wrapper(self):
                    
        def game():
            find = False
            tried_letter = self.entry_e.get()
            
            if len(tried_letter) == 1 and tried_letter in alph:
                
                if tried_letter not in tried_letters:
                    self.error_lbl.config(text="")
                    tried_letters.append(tried_letter)
                    
                    for index, c in enumerate(hidden_word_list):
                        
                        if c == tried_letter:
                            find_list[index] = c
                            find = True
                            
                    if find == True:
                        self.error_lbl.config(text=f"La lettre {tried_letter} est dans le mot mystère", fg="green")
                        
                    else:
                        self.error_lbl.config(text=f"La lettre {tried_letter} n'est pas dans le mot mystère", fg="red")
                        self.life_intv.set(self.life_intv.get() - 1)
                        self.pendu_cv.delete("all")
                        self.pendu_cv.create_text((100, 150), text=pendu_img[str(self.life_intv.get())])
                        
                        if self.life_intv.get() == 0:
                            showinfo(message=f"Vous êtes pendu, le mot mystère était '{hidden_word}'")
                            self.w.destroy()
                            exit()
                                                
                    if find_list == hidden_word_list:
                        showinfo(message=f"Bravo ! Le mot mystère était bien '{hidden_word}'")
                        self.w.destroy()
                        exit()
                        
                else:
                    self.error_lbl.config(text="Vous avez déjà entré cette lettre !", fg="red")
                
            else:
                self.error_lbl.config(text="Vous devez entrer une lettre présente dans l'alphabet, ou l'un des caractères suivant : àäéèêëÿùç-'", fg="red")
                
            self.hidden_word_lbl.config(text=f"Mot mystère : {find_list}")
            self.hidden_word_lbl.grid(row=0)
            self.tried_letters_lbl.config(text=f"Vous avez essayé les lettres : {tried_letters}")
            self.tried_letters_lbl.grid(row=1)                   
                                     
        with open("program/assets/pendu_img.json", "r") as f:
            pendu_img = json.load(f)
                   
        hidden_word = func(self)
        alph_error = False
        hidden_word_list = []
        find_list = []
        tried_letters = []
            
        if len(hidden_word) > 0:
                
            for c in hidden_word:
                    
                if c in alph:
                    hidden_word_list.append(c)
                    find_list.append("_")
                        
                else:
                    alph_error = True
                        
                if alph_error == False:
                    self.error_lbl.config(text="")
                    self.life_lbl.config(textvariable=self.life_intv)
                    self.life_lbl.grid(row=2)
                    self.enter_b.config(command=game)
                    self.entry_lbl.config(text="Essayez de deviner une lettre")
                                            
                else:
                    self.error_lbl.config(text="Le mot ne doit comporter que des lettres de l'alphabet et les caractères àäéèêëÿùç-'")
                
        else:
            self.error_lbl.config(text="Vous devez entrer un mot")
             
    return wrapper