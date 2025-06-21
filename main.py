try:
    import getpass
    
except ImportError:
    print("Ce programme a besoin que le module 'getpass' soit installé")
    exit()
    
from program.game_styles import multi

print("Welcome to Hanged Game")
class Game:
    
    def __init__(self):
        self.multi = multi
    
    def new_game(self):
        mod_loop = True
        
        while mod_loop == True:
            
            mod_choice = input("\n=== Mod ===\n1) Multi-player\n2) Back\n")
            
            if mod_choice == "1":
                self.multi.multi_player()
                
            elif mod_choice == "2":
                mod_loop = False
                
            else: 
                print("\nInvalid choice")
        
    def menu(self):
        menu_loop = True
        
        while menu_loop == True:
            menu_choice = input("\n===== Menu =====\n1) New Game\n2) Quit\n")
            
            if menu_choice == "1":
                self.new_game()
                
            elif menu_choice == "2":
                print("\nGoodbye !")
                exit()
            
            else:
                print("\nInvalid choice")
                
                
game = Game()
game.menu()