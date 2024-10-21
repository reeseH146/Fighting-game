# --- This is a pygame fighting game ---
import time
import pygame as pg
pg.init()
from pygame.locals import *
if not pg.get_init():
    print("There was something wrong with the program *>*")
    quit()
# import math
# import random as r

"""
# --- Sprite Class ---
# Creates and assigns attributes to the sprite
class Spr:
    def __init__(self, name, start_loc, spriteIMG):
        self.rect = pg.rect.Rect(start_loc)
        # self.colour = charColour
        self.Char = spriteIMG
        self.name = name
        self.health = 100
        self.healTimes = 3
        self.mana = 100

    # Moves character forward by redrawing the whole scene then calculating change in position
    def moveForward(self):
        # Redraws the scene with character position modified
        pg.draw.rect(Window, [000, 000, 000], Window.fill((000, 000, 000)))
        self.rect[0] += 7
        Window.blit(char1Still, self.rect)

    # Moves character backwards by redrawing the whole scene then calculating change in position
    def moveBackward(self):
        # Redraws the scene with character position modified
        pg.draw.rect(Window, [000, 000, 000], Window.fill((000, 000, 000)))
        self.rect[0] -= 7
        Window.blit(char1Still, [0, 0])

        # Character jumps by redrawing the whole scene then calculating change in position
    def moveJump(self):
        # Redraws the scene with character position modified
        pg.draw.rect(Window, [000, 000, 000], Window.fill((000, 000, 000)))
        self.rect[1] += 10
        Window.blit(char1Still, [0, 0])

        # Character crouches forward by redrawing the whole scene then calculating change in position
    def moveCrouch(self):
        # Redraws the scene with character position modified
        pg.draw.rect(Window, [000, 000, 000], Window.fill((000, 000, 000)))
        self.rect[0] -= (1) ###Change this value based on the character size
        Window.blit(char1Still, [self.rect[0], ])

    # Punch is weaker than kick but faster
    @staticmethod
    def punch(opponent):
        opponent.health -= r.randint(5, 15)
        print(opponent.name, opponent.health)
    #####

    # Kick is generally more powerful than punch but slower
    @staticmethod
    def kick(opponent):
        opponent.health -= r.randint(10, 20)
        print(opponent.name, opponent.health)

    # Player cannot move while healing
    def heal(self):
        if (self.health <= 10) & (self.healTimes > 0):
            pg.event.set_blocked([pg.KEYDOWN, pg.MOUSEBUTTONUP])
            self.healTimes -= 1
            self.health += 10
            pg.event.set_allowed([pg.KEYDOWN, pg.MOUSEBUTTONUP])
            print(self.name, self.health)

    def ranGen(self, mini, maxi):
        randomNumber = r.randint(int(r.random() * mini), int(r.random() * maxi))
        return randomNumber
"""

# --- Font generator ---
"""
Font class takes various arguments to create an instance of text with its attributes
This makes it easier to place fonts during runtime as only the location will change
 - Font and size creates the type of font that will be used with the text
 - Text, Antialias, Text Colour and Background Colour are attributes of the text and its the text box
"""
# --- Text generator ---
class TextGen:
    def __init__(self, font, size, text, antialias, textColour, backgroundColour, centrePosX, centrePosY):
        self.font = pg.font.Font(font, size)
        self.text = self.font.render(text, antialias, textColour, backgroundColour)
        self.rect = self.text.get_rect()
        self.rect.center = (centrePosX, centrePosY)
        self.originX = self.rect[0]
        self.originY = self.rect[1]
        self.endX = self.originX + self.rect[2]
        self.endY = self.originY + self.rect[3]

    # Renders the text onto the screen
    def render(self):
        Window.blit(self.text, self.rect)

# --- Button generator ---
# Works similarly to the font generator but has interactivity by checking whether there is input within its hit box
class ButtonGen:
    def __init__(self, font, size, text, antialias, textColour, backgroundColour, centrePosX, centrePosY):
        self.font = pg.font.Font(font, size)
        self.text = self.font.render(text, antialias, textColour, backgroundColour)
        self.rect = self.text.get_rect()
        self.rect.center = (centrePosX, centrePosY)
        self.originX = self.rect[0]
        self.originY = self.rect[1]
        self.endX = self.originX + self.rect[2]
        self.endY = self.originY + self.rect[3]

    # Renders the button onto the screen
    def render(self):
        Window.blit(self.text, self.rect)

    # Checks whether the input is within the button parameters
    def positionCheck(self, MousePosition):
        if (self.originX < MousePosition[0] < self.endX) and (self.originY < MousePosition[1] < self.endY):
            return True


# --- Main ---
# Loads the variables and constants
WinSize = (480, 270)
Clock = pg.time.Clock()
#Preset colours which will be used in the menus
BackgroundColour = (66, 129, 164)
AccentColour = (72, 169, 166)
SubBackgroundColour = (228, 223, 218)
SubAccentColour = (212, 180, 131)
#Game states used to determine what part of teh code can be executed
StateInMenu = False
StateInOptions = False
StateInCharacterSelection = False
StateInMapSelection = False
StateInGame = False

# Load assets - Loads assets such as images and fonts
DefaultFont = "Other assets\Agdasima\Agdasima-Regular.ttf"
AlternativeFont = "freesansbold.ttf"
TempBG = "Other assets\Archive\SizeTest3.png"              ### Remove this
TempChar = "Other assets\Archive\TempChar.png"             ### Remove this
Icon = pg.image.load("Game assets\Icon.png")
Char1Still = pg.image.load("Game assets\Char1Still.png")
#Char2Still = pg.image.load("Game assets\")                ### Create image
#Char3Still = pg.image.load("Game assets\")
Background1 = pg.image.load("Game assets\BG1_Ring.png")
Background2 = pg.image.load("Game assets\BG2_Beach.png")
Background3 = pg.image.load("Game assets\BG3_Woodlands.png")
#Background4 = pg.image.load("Game assets\BG4_Hell.png)    ### Create image

# Loads the screen and visual assets onto the screen
pg.display.set_icon(Icon)
pg.display.set_caption("PyG Battle program")
Window = pg.display.set_mode(WinSize)

#Loads all the text and buttons to be used in the game
#(font, size, text, antialias, textColour, backgroundColour, centrePosX, centrePosY)
LoadingText = TextGen(DefaultFont, 35, "Loading The Game...Please Wait", True, SubAccentColour, SubBackgroundColour, WinSize[0] // 2, WinSize[1] // 2)
WelcomeText = TextGen(DefaultFont, 30, "FightingGame Booted", True, SubAccentColour, SubBackgroundColour, WinSize[0] // 2, WinSize[1] // 2)
"""
StartGameButton = ButtonGen()
SettingButton = ButtonGen()
ReturnButton = ButtonGen()
CharSelectText = TextGen()
Player1Text = TextGen()
Player2Text = TextGen()
Char1Button = ButtonGen()
Char2Button = ButtonGen()
Char3Button = ButtonGen()
Char4Button = ButtonGen()
Background1Button = ButtonGen()
Background2Button = ButtonGen()
Background3Button = ButtonGen()
Background4Button = ButtonGen()
"""

#A loading screen which waists the players' time since this is not needed and also yes, I spelt it waist not waste
Window.fill(BackgroundColour, pg.Rect(0, 0, WinSize[0], WinSize[1]))
LoadingText.render()
pg.display.update()
time.sleep(5)
#The welcome screen which notifies the user the pointless loading screen has been completed
Window.fill(BackgroundColour, pg.Rect(0, 0, WinSize[0], WinSize[1]))
WelcomeText.render()
pg.display.update()
time.sleep(3)

pg.display.update()
# The main loop which runs the game
while True:
    for event in pg.event.get():
        if (event.type == pg.QUIT) or ((event.type == pg.KEYDOWN) and (event.key == K_ESCAPE)):
            pg.quit()
            print("Exited pygame")
            quit()
        # This is done every cycle to keep the game running smoothly
    pg.display.update()
    Clock.tick(60)
