# --- This is a pygame fighting game ---
import sys
import pygame as pg
import random as r
pg.init()
if not pg.get_init():
    print("There was something wrong with the program *>*")
    sys.exit()
# import math

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

    """
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
 - Text is moved with a tuple which contains its new position     
"""
class FontGEN:
    def __init__(self, font, size, text, antialias, textColour, backgroundColour):#, textBackground, textTransformation):
        self.font = pg.font.Font(font, size)
        self.text = self.font.render(text, antialias, textColour, backgroundColour)
        self.rect = self.text.get_rect()
        self.rect.center = (WinSize[0]//2, WinSize[1]//2)

    # Renders the text onto the screen
    def render(self):
        Window.blit(self.text, self.rect)

    # Changes the position of the textbox's centre with coordinates in tuple
    def move(self, newPosition):
        self.rect.center(newPosition[0], newPosition[1])
        Window.blit(self.text, self.rect)


"""
# --- Button generator ---
# Works similarly to the font generator but has interactivity
class ButtonGEN:
    def __init__(self, type, rect, position):
        if type == "Image":
            self.rect = pg.rect.rect()
        elif type == "Drawn":
            self.rect = pg.rect.rect()
            pg.draw.rect(Window, [000, 000, 000], self.button)
"""


# --- Main ---
# Loads the variables and constants
WinSize = (900, 450)
Clock = pg.time.Clock()
stateInMenu = False
stateInOptions = False
stateInCharacterSelection = False
stateInMapSelection = False
stateInGame = False

# Load assets - Loads assets such as images and fonts
defaultFont = "Other assets\Agdasima\Agdasima-Regular.ttf"
alternativeFont = "freesansbold.ttf"
icon = pg.image.load("Game assets\Icon.png")
char1Still = pg.image.load("Game assets\Char1Still.png")
#char2Still = pg.image.load("Game assets\")
#char3Still = pg.image.load("Game assets\")



# Sprite creation - Creates all sprites to be used in the game.
p1 = Spr("player 1!!!", [300, 150, 20, 55], char1Still)
p2 = Spr("player 2!!!", [300, 150, 20, 55], char1Still)

# Loads the screen and visual assets onto the screen
pg.display.set_icon(icon)###
pg.display.set_caption("Draft - PyG Battle program")
Window = pg.display.set_mode(WinSize)

Window.blit(char1Still, (0, 175))#pg.draw.rect(Window, p2.colour, p2.rect)
Window.blit(char1Still, (0, 175))#pg.draw.rect(Window, p2.colour, p2.rect)
font1 = FontGEN(defaultFont, 45, "This finally worked", False, (0, 0, 0), (155, 000, 000))#"Other assets\Agdasima\Agdasima-Regular.ttf"
font1.render()
pg.display.update()
# The main loop which runs the game
while True:
    for event in pg.event.get():
        if (event.type == pg.QUIT) or (event.type == pg.K_ESCAPE):
            pg.quit()
            print("Exited pygame")
            quit()
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_w:
                p1.moveForward()
                font1.render()
        elif event.type == pg.KEYUP:
            if event.type == pg.K_p:
                p1.punch(p2)
            elif event.type == pg.K_k:
                p1.kick(p2)
            """
            elif event.key == pg.K_h:
                p1.heal()
            """
        # This is done every cycle to keep the game running smoothly
        pg.display.update()
        Clock.tick(60)
