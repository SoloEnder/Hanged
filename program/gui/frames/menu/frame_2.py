import tkinter as tk

class MenuFrame2(tk.Frame):
    
    def __init__(self, master):
        super().__init__(master)
        self.config(bg="white")
        self.play_b = tk.Button(self, text="Jouer",width=12, font=("default 20 bold"), bg="light green", relief="flat", command=self.master.switch_game_fr)
        self.play_b.grid(row=0, column=0)
        self.about_b = tk.Button(self, text="A propos", width=12, font=("default 20 bold"), bg="gray", relief="flat", command=self.master.switch_about_fr)
        self.about_b.grid(row=1, column=0, pady=70)
        self.quit_app_b = tk.Button(self, text="Exit", width=12, font=("default 20 bold"), bg="red", relief="flat", command=self.master.exit_app)
        self.quit_app_b.grid(row=2, column=0)