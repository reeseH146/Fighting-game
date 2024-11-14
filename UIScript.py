# Python file containing classes to make instances of UI objects such as buttons
"""
v 1.0
 - Normal and image static buttton class
 - Normal static fonts class
"""
import pygame as pg
pg.init()
if not pg.get_init():
    print("There was something wrong with the program *>*")
    quit()

# Loads general data
# Default fonts
DefaultFont = "Other assets\Agdasima\Agdasima-Regular.ttf"
AlternativeFont = "freesansbold.ttf"

# --- Text generator ---
"""
Font class takes various arguments to create and instance of text and rectangle with their attributes
This simplifies the use of fonts throughout the game after creation
"""
class TextGen:
    def __init__(self, size, text, antialias, textColour, centrePosX, centrePosY):
        self.font = pg.font.Font(DefaultFont, size)
        self.text = self.font.render(text, antialias, textColour[1], textColour[0])
        self.rect = self.text.get_rect()
        self.rect.center = (centrePosX, centrePosY)
        self.originX = self.rect[0]
        self.originY = self.rect[1]
        self.endX = self.originX + self.rect[2]
        self.endY = self.originY + self.rect[3]

    # Renders the text onto the screen
    def render(self, Window):
        Window.blit(self.text, self.rect)

# --- Button text generator ---
# Works similarly to the font generator but has interactivity by checking whether there is input within its hit box
class TextButton:
    def __init__(self, size, text, antialias, defColour, centrePosX, centrePosY):
        self.font = pg.font.Font(DefaultFont, size)
        self.text = self.font.render(text, antialias, defColour[1], defColour[0])
        self.rect = self.text.get_rect()
        self.rect.center = (centrePosX, centrePosY)
        self.originX = self.rect[0]
        self.originY = self.rect[1]
        self.endX = self.originX + self.rect[2]
        self.endY = self.originY + self.rect[3]

    # Renders the button onto the screen
    def render(self, Window):
        Window.blit(self.text, self.rect)

    # Checks whether the input is within the button parameters
    def positionCheck(self, MousePos):
        if (self.originX < MousePos[0] < self.endX) and (self.originY < MousePos[1] < self.endY):
            return True

    def changeText(self, newText):
        self.text = newText

# --- Button image generator ---
# Works similarly but text attributes are replaced with an image
class ImgButton:
    def __init__(self, image, centrePosX, centrePosY):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (centrePosX, centrePosY)
        self.originX = self.rect[0]
        self.originY = self.rect[1]
        self.endX = self.originX + self.rect[2]
        self.endY = self.originY + self.rect[3]

    # Renders the button onto the screen
    def render(self, Window):
        Window.blit(self.image, self.rect)

    # Checks whether the input is within the button parameters
    def positionCheck(self, MousePos):
        if (self.originX < MousePos[0] < self.endX) and (self.originY < MousePos[1] < self.endY):
            return True