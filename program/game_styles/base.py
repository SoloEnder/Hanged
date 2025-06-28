import json

alph = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZzàäéèêëÿùç-'"

def base(func):
    
    def wrapper():
        running = True
        
        while running == True:
                    
            with open("program/assets/pendu_img.json", "r") as f:
                pendu_img = json.load(f)
           
            enter_hidden_word = True
            
            while enter_hidden_word == True:        
                hidden_word = func()
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
                running = False
                enter_hidden_word = False
            
            while game_loop == True:
                try_loop = True
                
                while try_loop == True:
                    find = False
                    print(f"\nLettres trouvées : {find_list}")
                    print(f"\nToutes les lettres tapées : {tried_letters}")
                    user_try = input("\nTentez de deviner une lettre: ")
                            
                    if len(user_try) == 1:
                        
                         if user_try in alph:
                                
                             if user_try not in tried_letters:
                                 tried_letters.append(user_try)
                                 try_loop = False
                                        
                             else:
                                 print("\nVous avez déjà entré cette lettre !")
                                    
                    else:
                       print("\nVous devez entrer une lettre")
                       
                for index, i in enumerate(hidden_word_list):
                    
                    if user_try == i:
                        find_list[index] = user_try
                        find = True
                        
                if find == True:
                    print(f"\nLa lettre '{user_try}' est bien dans le mot mystère")
                         
                else:
                    life -= 1
                    print(pendu_img[str(life)])
                    print(f"\nLa lettre '{user_try}' n'est pas dans le mot mystère")
                    print(f"\nIl vous reste {life} chances")
                    
                if life == 0:
                    print(f"\nVous êtes pendu ! Le mot mystère était '{hidden_word}'")
                    running = False
                    game_loop = False
                    
                if find_list == hidden_word_list:
                    print(f"\nBravo ! Le mot mystère était bien '{hidden_word}' !")
                    running = False
                    game_loop = False
                    
    return wrapper