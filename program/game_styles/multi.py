import getpass

from program.game_styles.base import base

@base
def multi_player():
     return getpass.getpass("\nEntrez le mot que les autres joueurs devront deviner ou cliquez sur la touche 'Enter' pour quitter : ")  