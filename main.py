try:
     
    import tkinter as tk
    
except ImportError:
    print("Ce programme a besoin que le module 'tkinter' soit installé")
    exit()
    

print("Welcome to Hanged Game")

from program.gui.window import Window
app = Window()
app.switch_menu_fr()
app.mainloop()