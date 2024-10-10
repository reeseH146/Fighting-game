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
        pg.draw.rect(Window, [000, 000, 000], currentDisplay)
        self.rect[0] += 7
        Window.blit(Char1Still, [0, 0])

    # Moves character backwards by redrawing the whole scene then calculating change in position
    def moveBackward(self):
        # Redraws the scene with character position modified
        pg.draw.rect(Window, [000, 000, 000], currentDisplay)
        self.rect[0] -= 7
        Window.blit(Char1Still, [0, 0])

        # Character jumps by redrawing the whole scene then calculating change in position
    def moveJump(self):
        # Redraws the scene with character position modified
        pg.draw.rect(Window, [000, 000, 000], currentDisplay)
        self.rect[1] += 10
        Window.blit(Char1Still, [0, 0])

        # Character crouches forward by redrawing the whole scene then calculating change in position
    def moveCrouch(self):
        # Redraws the scene with character position modified
        pg.draw.rect(Window, [000, 000, 000], currentDisplay)
        self.rect[0] -= (1) ###Change this value based on the character size
        Window.blit(Char1Still, [self.rect[0], ])

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

# --- Button generator ---
class ButtonGEN:
    def __init__(self, rect, position):
        self.button = pg.rect.Rect(rect)
        pg.draw.rect(Window, [000, 000, 000], self.button)

    def kill(self):
        displaySize = pg.display.get_window_size()
        pg.Rect.move(self.button, displaySize[0], displaySize[1])

    def move(self, position):
        pg.Rect.move(self.button, position[0], position[1])

# --- Main ---
# Loads the variables and constants
WinSize = (1800, 900)
Green = [0, 255, 0]
currentDisplay = pg.Rect(0, 0, 1800, 1200)

# Loads visual assets
Icon = pg.image.load("Game assets\Icon.png")
Char1Still = pg.image.load("Game assets\Char1Still.png")

# Sprite creation
p1 = Spr("player 1!!!", [300, 150, 20, 55], Char1Still)
p2 = Spr("player 2!!!", [300, 150, 20, 55], Char1Still)

# Loads the screen and visual assets onto the screen
pg.display.set_icon(Icon)###
pg.display.set_caption("Draft - PyG Battle program")
Window = pg.display.set_mode(WinSize)

Window.blit(Char1Still, (0, 175))#pg.draw.rect(Window, p2.colour, p2.rect)
Window.blit(Char1Still, (0, 175))#pg.draw.rect(Window, p2.colour, p2.rect)

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
        pg.time.Clock().tick(60)
