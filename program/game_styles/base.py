def base():
    
    def wrapper():
        hidden_word_list = []
        find_list = []
        alph_error = False
        tried_letters = []
        
        if hidden_word != "":
            
            for c in hidden_word:
                
                if c in alph:
                    hidden_word_list.append(c)
                    find_list.append("_")
                    
                else:
                    alph_error = True
                    
            if alph_error == True:
                print("Le mot mystère ne peut contenir que des lettres de l'alphabet et les caractères 'à','ä','é','è','ê','ë','ÿ','ù','ç','-', des apostrophes et '-' !")
            
            else:
                game_loop = True
                life = 8
                enter_hidden_word = False
                
        else:
            
                
