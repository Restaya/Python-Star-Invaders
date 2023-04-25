# Base logic learned from Clear Code's Space Invaders YouTube video
# Buttons logic learned from Code with Russel's YouTube video
# Code has been adjusted,not copied entirely
# Enemy generation logic selfwritten

from gui.game import Game

if __name__ == "__main__":
    game = Game(800,600,25)
    game.start_menu()