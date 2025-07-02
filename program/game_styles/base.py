import json

alph = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZzàäéèêëÿùç-'"

def base(func):
    
    def wrapper(self):
                    
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
                        self.enter_b.config(text="submitt")
                        
                    else:
                        self.error_lbl.config(text="Le mot ne doit comporter que des lettres de l'alphabet et les caractères àäéèêëÿùç-'")
                
            else:
                self.error_lbl.config(text="Vous devez entrer un mot")
             
    return wrapper