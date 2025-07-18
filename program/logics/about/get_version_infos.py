from tkinter.messagebox import showerror
import json

def get_vinfos():
        
    try:
            
        with open("program/data/vinfos.json", "r") as f:
            vinfos = json.load(f)
                
    except:
        showerror(message="Unable to load version infos")
        return None
            
    else:
        return vinfos