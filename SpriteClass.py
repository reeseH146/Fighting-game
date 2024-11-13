# Single sprite class which
import pygame as pg
pg.init()
from pygame.locals import *
if not pg.get_init():
    print("There was something wrong with the program *>*")
    quit()
import random as r
# import math


# --- Sprite Class ---
# Creates and assigns attributes to the sprite
# There are some functions in this class which allows the user to interact with the sprite
"""
Base movements : 
 - Move forward
 - Move backward
 - Punch
 - Kick
 - Heal
More movements : 
 - Jump
 - Crouch
 - Adjust kick and punch hitbox
 - Grab
Advanced movements : 
 - Character based movements (Alternate movements, new movements)
 - Dodge
 - Roll
 - Flip
 - Parry
 - Counter
 - Brace
Additional items and weapons : 
 - Shield
 - Sword : Depends on types of sword/dagger...
 - Bow : Depends on type of bow...
 - Magic : Potions and spells
 - Others : Chainsaw, hammer, ...
"""
class spriteCreation:
    def __init__(self, name, startLoc, spriteIMG):
        self.char = spriteIMG
        self.loc = [startLoc[0], startLoc[1]]
        self.rect = self.char.get_rect().center = (self.loc[0], self.loc[1])
        self.name = name
        self.health = 100
        self.healTimes = 3
        self.mana = 100
        self.attackRange = self.char.get_rect().inflate_ip(40, 20)
        self.attackRange.center = (startLoc[0], startLoc[1])
        self.atkCool = 500

    def render(self, Window):
        Window.blit(self.char, self.rect)

    # Moves character forward by redrawing the whole scene then calculating change in position
    def moveForward(self, Window, ChosenMap):
        # Redraws the scene
        Window.blit(ChosenMap, (1, 1))
        # Modifies the character position
        self.loc[0] += 5
        self.rect.center = (self.loc[0], self.loc[1])
        self.attackRange.center = (self.loc[0], self.loc[1])
        Window.blit(self.char, self.rect)

    # Moves character backwards by redrawing the whole scene then calculating change in position
    def moveBackward(self, Window, ChosenMap):
        # Redraws the scene
        Window.blit(ChosenMap, (1, 1))
        # Modifies the character position
        self.loc[0] -= 5
        self.rect.center = (self.loc[0], self.loc[1])
        self.attackRange.center = (self.loc[0], self.loc[1])
        Window.blit(self.char, self.rect)


    def attackPunch(self, opponent):
        # Character punches the opponent if in attack range
        if self.attackRange.colliderect(opponent.rect):
            opponent.health -= r.randint(7, 10)