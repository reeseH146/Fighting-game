# --- This is a pygame fighting game ---
import pygame as pg
pg.init()
from pygame.locals import *
if not pg.get_init():
    print("There was something wrong with the program *>*")
    quit()
# import math
# import random as r


# --- Sprite Class ---
# Creates and assigns attributes to the sprite
class sprite:
    def __init__(self, name, startLoc, spriteIMG):
        self.char = spriteIMG
        self.rect = self.char.get_rect()
        self.rect.center = (startLoc[0], startLoc[1])
        self.name = name
        self.health = 100
        self.healTimes = 3
        self.mana = 100

    def render(self):
        Window.blit(self.char, self.rect)
"""
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

# --- Button text generator ---
# Works similarly to the font generator but has interactivity by checking whether there is input within its hit box
class ButtonGenText:
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
    def positionCheck(self, MousePos):
        if (self.originX < MousePos[0] < self.endX) and (self.originY < MousePos[1] < self.endY):
            return True

    def changeText(self, newText):
        self.text = newText

# --- Button image generator
class ButtonGenImg:
    def __init__(self, image, centrePosX, centrePosY):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (centrePosX, centrePosY)
        self.originX = self.rect[0]
        self.originY = self.rect[1]
        self.endX = self.originX + self.rect[2]
        self.endY = self.originY + self.rect[3]

    # Renders the button onto the screen
    def render(self):
        Window.blit(self.image, self.rect)

    # Checks whether the input is within the button parameters
    def positionCheck(self, MousePos):
        if (self.originX < MousePos[0] < self.endX) and (self.originY < MousePos[1] < self.endY):
            return True


# --- Main ---
# Loads the variables and constants
WinSize = (16*30, 9*30)
Clock = pg.time.Clock()
Running = True
ChosenChar1 = ""
ChosenChar2 = ""
ChosenMap = ""
#Preset colours which will be used in the menus
BackgroundColour = (66, 129, 164)
AccentColour = (72, 169, 166)
SubBackgroundColour = (228, 223, 218)
SubAccentColour = (212, 180, 131)
#Game states used to determine what part of teh code can be executed
StateInMenu = True
StateInOptions = False
StateInCharacterSelection = False
StateInMapSelection = False
StateInGame = False
#Coordinates, the variables are named by their xy position, custom positions have to be tweaked individually
CentreTop = [(WinSize[0] // 2), int(WinSize[1] * 0.1)]
CentreBottom = [(WinSize[0] // 2), int((WinSize[1] * 0.9))]
CentreCentre = [(WinSize[0] // 2), (WinSize[1] // 2)]
LeftTop = [int((WinSize[0] * 0.1)), int((WinSize[1] * 0.1))]
RightTop = [int((WinSize[0] * 0.9)), int((WinSize[1] * 0.1))]
RightBottom = [int((WinSize[0] * 0.9)), int((WinSize[1] * 0.9))]

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
#Background4 = pg.image.load("Game assets\BG4_Hell.png)    ### Create image # This code is literally hell

# Loads the screen and visual assets onto the screen
pg.display.set_icon(Icon)
pg.display.set_caption("PyG Battle program")
Window = pg.display.set_mode(WinSize)

#Loads all the text and buttons to be used in the game
#(font, size, text, antialias, textColour, backgroundColour, centrePosX, centrePosY)
LoadingText = TextGen(AlternativeFont, 28, "Loading The Game...Please Wait", True, SubAccentColour, SubBackgroundColour, CentreCentre[0], CentreCentre[1]) #Pos at Centre
WelcomeText = TextGen(AlternativeFont, 28, "FightingGame Booted", True, SubAccentColour, SubBackgroundColour, CentreCentre[0], CentreCentre[1]) # Pos at Centre
StartGameButton = ButtonGenText(DefaultFont, 27, "Start Game", True, SubAccentColour, SubBackgroundColour, CentreCentre[0], ((WinSize[1] - 75) // 2)) # Pos at centre, first button
SettingButton = ButtonGenText(DefaultFont, 27, "Settings", True, SubAccentColour, SubBackgroundColour, CentreCentre[0], CentreCentre[1]) # Pos at centre, second button
ExitButton = ButtonGenText(DefaultFont, 27, "Close game", True, SubAccentColour, SubBackgroundColour, CentreCentre[0], ((WinSize[1] + 75) // 2)) # Pos at centre, third button
OptionMenuText = ButtonGenText(DefaultFont, 27, "Options Menu", True, SubAccentColour, SubBackgroundColour, CentreTop[0], CentreTop[1]) # Pos at top
OptionMenuText1 = ButtonGenText(DefaultFont, 27, "Nothing to see here at the moment", True, SubAccentColour, SubBackgroundColour, CentreCentre[0], CentreCentre[1]) # Pos Centre
ReturnButton = ButtonGenText(DefaultFont, 27, "Return", True, SubAccentColour, SubBackgroundColour, RightBottom[0], RightBottom[1]) # Bottom Right

CharSelectText = TextGen(DefaultFont, 27, "Select a character", True, SubAccentColour, SubBackgroundColour, CentreTop[0], CentreTop[1]) # At top centre
Player1Text = TextGen(DefaultFont, 27, "Player 1", True, SubAccentColour, SubBackgroundColour, RightTop[0], RightTop[1]) # At Top Right
Player2Text = TextGen(DefaultFont, 27, "Player2", True, SubAccentColour, SubBackgroundColour, LeftTop[0], LeftTop[1]) # At Top Left

Char1Button = ButtonGenImg(Char1Still, int((WinSize[0] * (1/6))), int((WinSize[1] * 0.5))) # Centre of top left quadrant # 0.5 * (1/3)
#Char2Button = ButtonGenImg(Char2Still, int((WinSize[0] * (1/3))), int((WinSize[1] * 0.25))) # Centre of top right quadrant
#Char3Button = ButtonGenImg(Char3Still, int((WinSize[0] * (2/3))), int((WinSize[1] * 0.75))) # Centre of bottom left quadrant
#Char4Button = ButtonGenImg(Char4Still, int((WinSize[0] * (5/6))), int((WinSize[1] * 0.75))) # Centre of bottom right quadrant
MapSelectText = TextGen(DefaultFont, 27, "Select a map", True, SubAccentColour, SubBackgroundColour, CentreTop[0], CentreTop[1]) # At top centre
Background1Button = ButtonGenImg(pg.transform.scale(Background1, (144, 81)), int((WinSize[0] * 0.30)), int((WinSize[1] * 0.30))) # Centre of top left quadrant
Background2Button = ButtonGenImg(pg.transform.scale(Background2, (16*9, 9*9)), int((WinSize[0] * 0.70)), int((WinSize[1] * 0.30))) # Centre of top right quadrant
Background3Button = ButtonGenImg(pg.transform.scale(Background3, (16*9, 9*9)), int((WinSize[0] * 0.30)), int((WinSize[1] * 0.70))) # Centre of bottom left quadrant
#Background4Button = ButtonGenImg(pg.transform.scale(Background4, (16*9, 9*9)), int((WinSize[0] * 0.70)), int((WinSize[1] * 0.70))) # Centre of bottom right quadrant
CountDown = ButtonGenText(DefaultFont, 30, "Begin in : 3", True, SubAccentColour, SubBackgroundColour, CentreTop[0], CentreTop[1]) # Pos at top centre

#A loading screen which waists the players' time since this is not needed and also yes, I spelt it waist not waste
Window.fill(BackgroundColour, pg.Rect(0, 0, WinSize[0], WinSize[1]))
pg.draw.rect(Window, AccentColour, (0, 0, WinSize[0], WinSize[1]), 5)
LoadingText.render()
pg.display.update()
pg.time.wait(3200)
#The welcome screen which notifies the user the pointless loading screen has been completed
Window.fill(BackgroundColour, pg.Rect(0, 0, WinSize[0], WinSize[1]))
pg.draw.rect(Window, AccentColour, (0, 0, WinSize[0], WinSize[1]), 5)
WelcomeText.render()
pg.display.update()
pg.time.wait(1600)

pg.display.update()
# The main loop which runs the game
while Running:
    for event in pg.event.get():
        # Quit the game
        if (event.type == pg.QUIT) or ((event.type == pg.KEYDOWN) and (event.key == K_ESCAPE)):
            Window.fill((0, 0, 0), (0, 0, WinSize[0], WinSize[1]))
            pg.display.update()
            pg.quit()
            print("Exited pygame")
            quit()
        # Main menu which brings the user to the next menus when the user clicks onto a button
        elif StateInMenu:
            # Renders main menu
            Window.fill(BackgroundColour, pg.Rect(0, 0, WinSize[0], WinSize[1]))
            pg.draw.rect(Window, AccentColour, (0, 0, WinSize[0], WinSize[1]), 5)
            StartGameButton.render()
            SettingButton.render()
            ExitButton.render()
            pg.display.update()
            # Checks for mouse input and position and whether to load the appropriate menu
            if event.type == MOUSEBUTTONDOWN:
                MousePosition = pg.mouse.get_pos()
                if StartGameButton.positionCheck(MousePosition):
                    StateInMenu = False
                    StateInCharacterSelection = True
                elif SettingButton.positionCheck(MousePosition):
                    StateInMenu = False
                    StateInOptions = True
                elif ExitButton.positionCheck(MousePosition):
                    StateInMenu = False
                    Running = False
        # Options menu, currently nothing here because providing settings will break this game
        elif StateInOptions:
            # Renders the options menu
            Window.fill(BackgroundColour, pg.Rect(0, 0, WinSize[0], WinSize[1]))
            pg.draw.rect(Window, AccentColour, (0, 0, WinSize[0], WinSize[1]), 5)
            OptionMenuText.render()
            OptionMenuText1.render()
            ReturnButton.render()
            pg.display.update()
            # Checks for mouse input and position and whether to load the appropriate menu
            if event.type == MOUSEBUTTONDOWN:
                MousePosition = pg.mouse.get_pos()
                if ReturnButton.positionCheck(MousePosition):
                    StateInOptions = False
                    StateInMenu = True
        # Character selection menu, 2 players can choose what character they want to play in the game
        elif StateInCharacterSelection:
            # Renders the character selection menu
            Window.fill(BackgroundColour, pg.Rect(0, 0, WinSize[0], WinSize[1]))
            pg.draw.rect(Window, AccentColour, (0, 0, WinSize[0], WinSize[1]), 5)
            CharSelectText.render()
            Player1Text.render()
            Player2Text.render()
            Char1Button.render()
            """
            Char2Button.render()
            Char3Button.render()
            Char4Button.render()
            """
            ReturnButton.render()
            # ---- Blit the rest of the buttons
            # Checks for input, moves on to next scene if detected both players clicked on a character
            pg.display.update()
            if event.type == MOUSEBUTTONDOWN:
                ButtonClicked = pg.mouse.get_pressed()
                MousePosition = pg.mouse.get_pos()
                if ReturnButton.positionCheck(MousePosition):
                    StateInCharacterSelection = False
                    StateInMenu = True
                    ChosenChar1 = ""
                    ChosenChar2 = ""
                # Checks where the input was and then who pressed
                if Char1Button.positionCheck(MousePosition):
                    if ButtonClicked[0]:
                        ChosenChar1 = sprite("Player 1", [50, WinSize[1] - 56], Char1Still)
                    elif ButtonClicked[2]:
                        ChosenChar2 = sprite("Player 2", [WinSize[0] - 70, WinSize[1] - 56], Char1Still)
                """
                Put in the rest of them
                """
            # Checks both players have selected a character before proceeding
            elif (ChosenChar1 != "") and (ChosenChar2 != ""):
                StateInCharacterSelection = False
                StateInMapSelection = True


        # Map selection menu, 1 player can choose what map to play
        elif StateInMapSelection:
            # Renders the map selection menu
            Window.fill(BackgroundColour, pg.Rect(0, 0, WinSize[0], WinSize[1]))
            pg.draw.rect(Window, AccentColour, (0, 0, WinSize[0], WinSize[1]), 5)
            Background1Button.render()
            Background2Button.render()
            Background3Button.render()
            #Background4Button.render()
            ReturnButton.render()
            pg.display.update()
            # Checks for input and position to choose a map
            if event.type == MOUSEBUTTONUP:
                ButtonClicked = pg.mouse.get_pressed()
                MousePosition = pg.mouse.get_pos()
                if ReturnButton.positionCheck(MousePosition):
                    StateInMapSelection = False
                    StateInCharacterSelection = True
                    ChosenChar1 = ""
                    ChosenChar2 = ""
                elif Background1Button.positionCheck(MousePosition):
                    ChosenMap = Background1
                    StateInMapSelection = False
                    StateInGame = True
                    Window.blit(ChosenMap, (1, 1))
                    ChosenChar1.render()
                    ChosenChar2.render()
                    CountDown.render()
                    pg.display.update()
                    pg.time.wait(999)
                    for x in range(2, 0, -1):
                        CountDown = TextGen(DefaultFont, 30, f"Begin in : {x}", True, SubAccentColour, SubBackgroundColour, CentreTop[0], CentreTop[1]) # Pos at top centre
                        CountDown.render()
                        pg.display.update()
                        pg.time.wait(999)
                    CountDown = TextGen(DefaultFont, 30, "!!! Begin Battle !!!", True, SubAccentColour, SubBackgroundColour, CentreTop[0], CentreTop[1]) # Pos at top centre
                    CountDown.render()
                    pg.display.update()
                    pg.time.wait(500)
                elif Background2Button.positionCheck(MousePosition):
                    ChosenMap = Background2
                    StateInMapSelection = False
                    StateInGame = True
                elif Background3Button.positionCheck(MousePosition):
                    ChosenMap = Background3
                    StateInMapSelection = False
                    StateInGame = True
                    """
                    elif Background4Button.positionCheck(MousePosition):
                        ChosenMap = Background4
                        StateInMapSelection = False
                        StateInGame = True
                    """
        # In game, renders map and players, it countdowns before the players can interact each other until 1 "dies"
        elif StateInGame:
            Window.blit(ChosenMap, (1, 1))
            ChosenChar1.render()
            ChosenChar2.render()
    # This is done every cycle to keep the game running smoothly
    pg.display.update()
    Clock.tick(60)

# I'm sorry for whoever has to read this, I hope you enjoy understanding how this works
# I made some good progress yesterday, made the base of the game so then I can actually implement the mechanics the fans