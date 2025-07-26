try:
     
    import tkinter as tk
    
except ImportError:
    print("Ce programme a besoin que le module 'tkinter' soit installé")
    exit()

from program.gui.window import Window

if __name__ == "__main__":
    app = Window()
    app.switch_menu_fr()
    app.mainloop()