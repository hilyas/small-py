import os
import sys
import time
import random
import colorama

class Game():
    def __init__(self):
        self.history = []
        self.plays = [
            (colorama.Fore.RED + 'Red', 'r'),
            (colorama.Fore.YELLOW + 'Yellow', 'y'),
            (colorama.Fore.GREEN + 'Green', 'g'),
            (colorama.Fore.BLUE + 'Blue', 'b')
        ]

    def show_level(self):
        self.clear()
        for h in self.history:
            print(h[0], end=' ')
            sys.stdout.flush()
            time.sleep(1)

        self.clear()

    def add_move(self):
        self.history.append(random.choice(self.plays))
    
    def test_player(self):
        print(colorama.Fore.WHITE + "{} moves:".format(len(self.history)))
        for t, v in self.history:
            guess = input("Next [r,y,g,b]: ")
            if guess != v:
                return False
        return True

    def clear(self):
        os.system('clear')