import webbrowser
from tkinter.messagebox import showinfo, showerror, askyesno

def open_link_f(link):
    open_link_conf = askyesno(message=f"Voulez vous ouvrir le lien '{link}' ?")
    
    if open_link_conf == True:
        opened_link = webbrowser.open_new_tab(link)
    
        if opened_link == False:
            showerror("Impossible d'ouvrir le lien")