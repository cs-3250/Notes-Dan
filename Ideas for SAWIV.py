# Title Screen, Help Screen Display, and Player Setup
# @author 

import cmd
import textwrap
import sys
import os
import time
import random

screen_width = 100

#### Player Setup ####
class player:
    def __init__(self): 
        self.name = ''           # Player Name
        self.hp = 0              # Player Health
        self.status_effects = [] # Player Status Effects
myPlayer = player()

#### Title Screen ####
def title_screen_selections():     
    while option.lower() not in ['play', 'help', 'quit']:
        print("Please enter a new valid command.")
        option = input("> ")
        if option.lower() == ("play"):
            #start_game() !!! A placeholder at the moment !!!  
        elif option.lower() == ("help"):
            help_menu()
        elif option.lower() == ("quit"):
            sys.exit()

#### Title Screen Display ###
def title_screen():
    os.system('clear')
    print('##################################')
    print('#  This is our Horror Text RPG   #')
    print('#    Prepare to die a lot lol    #')
    print('##################################')
    print('             - Play -             ')
    print('             - Help -             ')
    print('             - Quit -             ')
    print('    - Copyright 2019 DCDEGMD -    ')
    print('##################################')
    title_screen_selections()

### Help Menu Display ###
def help_menu():
    print('##################################')
    print('#   This is our Horror Text RPG  #')
    print('##################################')
    print('- Type North, East, South, West to move your character') 
    print('- Use "Look" to inspect something in a room')
    print('- Good luck and have a fun time!') 
    print('##################################')
    title_screen_selections()