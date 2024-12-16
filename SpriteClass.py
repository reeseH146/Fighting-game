# Single sprite class which
import pygame as pg
pg.init()
if not pg.get_init():
    print("There was something wrong with the program *>*")
    quit()
import random as r

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
class defSprite:
    def __init__(self, name, startLoc, spriteIMG):
        self.name = name
        self.char = spriteIMG
        self.loc = [startLoc[0], startLoc[1]]
        self.rect = self.char.get_rect()
        self.rect.center = (self.loc[0], self.loc[1])
        self.health = 100
        self.healTimes = 3
        self.mana = 100
        self.coolReq = [500, 600, 2000] # Punch, Kick, Heal
        self.coolCount = [self.coolReq[0], self.coolReq[1], self.coolReq[2]]
        self.attackRange = self.char.get_rect()
        self.attackRange.inflate_ip(40, 40)
        self.attackRange.center = (self.loc[0], self.loc[1])

    def render(self, Window):
        Window.blit(self.char, self.rect)

    # Moves character forward by redrawing the whole scene then calculating change in position
    def moveForward(self, Window, ChosenMap):
        # Redraws the scene
        Window.blit(ChosenMap, (0, 0))
        # Modifies the character position
        self.loc[0] += 2
        self.rect.center = (self.loc[0], self.loc[1])
        self.attackRange.center = (self.loc[0], self.loc[1])
        Window.blit(self.char, self.rect)

    # Moves character backwards by redrawing the whole scene then calculating change in position
    def moveBackward(self, Window, ChosenMap):
        # Redraws the scene
        Window.blit(ChosenMap, (0, 0))
        # Modifies the character position
        self.loc[0] -= 2
        self.rect.center = (self.loc[0], self.loc[1])
        self.attackRange.center = (self.loc[0], self.loc[1])
        Window.blit(self.char, self.rect)

    # If opponent is within character attack range then reduce its HP
    def attackPunch(self, opponent):
        # Character punches the opponent if in attack range and cooldown over
        if (self.coolCount[0] + self.coolReq[0]) < pg.time.get_ticks():
            if self.attackRange.colliderect(opponent.rect):
                opponent.health -= r.randint(7, 10)
                self.coolCount[0] = pg.time.get_ticks()
                print(f"{opponent.name}'s health : {opponent.health}")

    # If opponent is within character attack range then reduce its HP
    def attackKick(self, opponent):
        # Character punches the opponent if in attack range
        if (self.coolCount[1] + self.coolReq[1]) < pg.time.get_ticks():
            if self.attackRange.colliderect(opponent.rect):
                opponent.health -= r.randint(10, 15)
                self.coolCount[0] = pg.time.get_ticks()
                print(f"{opponent.name}'s health : {opponent.health}")

    # Heals the character if it meets some requirements
    def heal(self):
        if (self.coolCount[2] + self.coolReq[2]) < pg.time.get_ticks():
            if self.healTimes > 0:
                self.healTimes -= 1
                self.health += r.randint(5, 15)
                print(f"{self.name}'s health : {self.health}")