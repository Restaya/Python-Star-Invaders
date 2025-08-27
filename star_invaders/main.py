# The game's base logic code was made following a tutorial from Clear Code, how to create sprites, check for collision and draw sprites on screen
from gui.game import Game


"""
You can run this main file without further configuration to start the game
Keybinding are in the README file
"""
if __name__ == "__main__":
    """
    Creates the game given the parameters
    First parameter is the screen's width
    Second parameter is the screen's height
    Third parameter is the required score to win the game
    The screen size paramaters should be divisible by 50 to display properly
    """
    game = Game(800, 600, 25)
    game.start_menu()
