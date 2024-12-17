# --- This is a pygame fighting game ---
import SpriteClass
import UIScript
import pygame as pg
pg.init()
from pygame.locals import *
if not pg.get_init():
    print("There was something wrong with the program *>*")
    quit()

# --- Main ---
# Loads the variables and constants
WinSize = (16*30, 9*30)
Clock = pg.time.Clock()

# Player configurable data
P1Char = ""
P2Char = ""
ChosenMap = ""
Scale = None

# Default colours
BGColour = (66, 129, 164)
BGAccent = (72, 169, 166)
SubBGColour = (228, 223, 218)
SubBGAccent = (212, 180, 131)
DefColour = [SubBGColour, SubBGAccent]

# Frequently used coordinates
CentreX = WinSize[0] // 2
CentreY = WinSize[1] // 2
LeftX = int(WinSize[0] * 0.1)
RightX = int(WinSize[0] * 0.9)
TopY = int(WinSize[1] * 0.1)
BottomY = int(WinSize[1] * 0.9)

# Load assets - Loads assets such as images and fonts
Icon = pg.image.load("Game assets/Icon.png")
Char1Still = pg.image.load("Game assets/Char1Still.png")
Char2Still = pg.image.load("Game assets/Char2Still.png")
Char3Still = pg.image.load("Game assets/Char3Still.png")
Char4Still = pg.image.load("Game assets/Char4Still.png")
BG1 = pg.image.load("Game assets/BG1_Ring.png")
BG2 = pg.image.load("Game assets/BG2_Beach.png")
BG3 = pg.image.load("Game assets/BG3_Woodlands.png")
BG4 = pg.image.load("Game assets/BG4_Hell.png")    # This code is literally hell

# Creates remaining assets to be used in game
#(font, size, text, antialias, textColour, BGColour, centrePosX, centrePosY)
LoadText = UIScript.TextGen(28, "Loading The Game...Please Wait", True, DefColour, CentreX, CentreY) #Pos at Centre
WelcomeText = UIScript.TextGen(28, "FightingGame Booted", True, DefColour, CentreX, CentreY) # Pos at Centre
StartButton = UIScript.TextButton(27, "Start Game", True, DefColour, CentreX, ((WinSize[1] - 75) // 2)) # Pos at centre, first button
SettingButton = UIScript.TextButton(27, "Settings", True, DefColour, CentreX, CentreY) # Pos at centre, second button
ExitButton = UIScript.TextButton(27, "Close game", True, DefColour, CentreX, ((WinSize[1] + 75) // 2)) # Pos at centre, third button
OptionMenuText = UIScript.TextButton(27, "Options Menu", True, DefColour, CentreX, TopY) # Pos at top
OptionMenuText1 = UIScript.TextButton(27, "Nothing to see here at the moment", True, DefColour, CentreX, CentreY) # Pos Centre
ReturnButton = UIScript.TextButton(27, "Return", True, DefColour, RightX, BottomY) # Bottom Right
CharSelectText = UIScript.TextGen(27, "Select a character", True, DefColour, CentreX, TopY) # At top centre
P1Text = UIScript.TextGen(27, "Player 1", True, DefColour, LeftX, TopY) # At Top Left
P2Text = UIScript.TextGen(27, "Player2", True, DefColour, RightX, TopY) # At Top Right
Char1Button = UIScript.ImgButton(Char1Still, int((WinSize[0] * (1/5))), CentreY)
Char2Button = UIScript.ImgButton(Char2Still, int((WinSize[0] * (2/5))), CentreY)
Char3Button = UIScript.ImgButton(Char3Still, int((WinSize[0] * (3/5))), CentreY)
Char4Button = UIScript.ImgButton(Char4Still, int((WinSize[0] * (4/5))), CentreY)
MapSelectText = UIScript.TextGen(27, "Select a map", True, DefColour, CentreX, TopY) # At top centre
BG1Button = UIScript.ImgButton(pg.transform.scale(BG1, (144, 81)), int((WinSize[0] * (1/3))), int((WinSize[1] * (1/3)))) # Centre of top left quadrant
BG2Button = UIScript.ImgButton(pg.transform.scale(BG2, (16*9, 9*9)), int((WinSize[0] * (2/3))), int((WinSize[1] * (1/3)))) # Centre of top right quadrant
BG3Button = UIScript.ImgButton(pg.transform.scale(BG3, (16*9, 9*9)), int((WinSize[0] * (1/3))), int((WinSize[1] * (2/3)))) # Centre of bottom left quadrant
BG4Button = UIScript.ImgButton(pg.transform.scale(BG4, (16*9, 9*9)), int((WinSize[0] * (2/3))), int((WinSize[1] * (2/3)))) # Centre of bottom right quadrant
CountDown = UIScript.TextButton(30, "Begin in : 3", True, DefColour, CentreX, TopY) # Pos at top centre

# -- Load screen and user welcome message --
pg.display.set_icon(Icon)
pg.display.set_caption("PyG Battle program")
Window = pg.display.set_mode(WinSize)
# A loading screen which waists the players' time since this is not needed and also yes, I spelt it waist not waste
Window.fill(BGColour, pg.Rect(0, 0, WinSize[0], WinSize[1]))
pg.draw.rect(Window, BGAccent, (0, 0, WinSize[0], WinSize[1]), 5)
LoadText.render(Window)
pg.display.update()
pg.time.wait(500)
# The welcome screen which notifies the user the pointless loading screen has been completed
Window.fill(BGColour, pg.Rect(0, 0, WinSize[0], WinSize[1]))
pg.draw.rect(Window, BGAccent, (0, 0, WinSize[0], WinSize[1]), 5)
WelcomeText.render(Window)
pg.display.update()
pg.time.wait(1600)
pg.display.update()

pg.key.set_repeat(50, 20)

# Game states which determines the current scene the player is in
StateInMenu = True
StateInOptions = False
StateInCharacterSelection = False
StateInMapSelection = False
InMenu = True
# Menu loop which lets the player configure game/program data 
while InMenu:
    for event in pg.event.get():
        # Quit the game
        if (event.type == pg.QUIT) or (event.type == K_ESCAPE):
            InGame = False
            pg.quit()
            print("""-------------\nExited pygame\n-------------""")
            quit()
        # Main menu which brings the user to the next menus when the user clicks onto a button
        elif StateInMenu:
            pg.event.set_allowed(MOUSEBUTTONDOWN)
            pg.event.set_allowed(MOUSEBUTTONUP)
            # Renders main menu
            Window.fill(BGColour, pg.Rect(0, 0, WinSize[0], WinSize[1]))
            pg.draw.rect(Window, BGAccent, (0, 0, WinSize[0], WinSize[1]), 5)
            StartButton.render(Window)
            SettingButton.render(Window)
            ExitButton.render(Window)
            pg.display.update()
            # Checks for mouse input and position and whether to load the appropriate menu
            if event.type == MOUSEBUTTONDOWN:
                MousePosition = pg.mouse.get_pos()
                if StartButton.positionCheck(MousePosition):
                    StateInMenu = False
                    StateInCharacterSelection = True
                    pg.event.set_blocked(MOUSEBUTTONDOWN)
                elif SettingButton.positionCheck(MousePosition):
                    StateInMenu = False
                    StateInOptions = True
                elif ExitButton.positionCheck(MousePosition):
                    StateInMenu = False
                    Running = False
                    pg.quit()
                    print("""-------------\nExited pygame\n-------------""")
                    quit()
        # Options menu, currently nothing here because providing settings will break this game
        elif StateInOptions:
            # Renders the options menu
            Window.fill(BGColour, pg.Rect(0, 0, WinSize[0], WinSize[1]))
            pg.draw.rect(Window, BGAccent, (0, 0, WinSize[0], WinSize[1]), 5)
            OptionMenuText.render(Window)
            OptionMenuText1.render(Window)
            ReturnButton.render(Window)
            pg.display.update()
            pg.event.set_allowed(MOUSEBUTTONDOWN)
            # Checks for mouse input and position and whether to load the appropriate menu
            if event.type == MOUSEBUTTONDOWN:
                MousePosition = pg.mouse.get_pos()
                if ReturnButton.positionCheck(MousePosition):
                    StateInOptions = False
                    StateInMenu = True
                    pg.event.set_blocked(MOUSEBUTTONDOWN)
        # Character selection menu, 2 players can choose what character they want to play in the game
        elif StateInCharacterSelection:
            # Renders the character selection menu
            Window.fill(BGColour, pg.Rect(0, 0, WinSize[0], WinSize[1]))
            pg.draw.rect(Window, BGAccent, (0, 0, WinSize[0], WinSize[1]), 5)
            CharSelectText.render(Window)
            P1Text.render(Window)
            P2Text.render(Window)
            Char1Button.render(Window)
            Char2Button.render(Window)
            Char3Button.render(Window)
            Char4Button.render(Window)
            ReturnButton.render(Window)
            pg.display.update()
            pg.event.set_allowed(MOUSEBUTTONDOWN)
            if event.type == MOUSEBUTTONDOWN:
                ButtonClicked = pg.mouse.get_pressed()
                MousePosition = pg.mouse.get_pos()
                if ReturnButton.positionCheck(MousePosition):
                    StateInCharacterSelection = False
                    StateInMenu = True
                    pg.event.set_blocked(MOUSEBUTTONDOWN)
                    P1Char = ""
                    P2Char = ""
                # Checks where the input was and then who pressed
                if ButtonClicked[0]:
                    if Char1Button.positionCheck(MousePosition):
                        P1Char = Char1Still
                    elif Char2Button.positionCheck(MousePosition):
                        P1Char = Char2Still
                    elif Char3Button.positionCheck(MousePosition):
                        P1Char = Char3Still
                    elif Char4Button.positionCheck(MousePosition):
                        P1Char = Char4Still
                elif ButtonClicked[2]:
                    if Char1Button.positionCheck(MousePosition):
                        P2Char = Char1Still
                    elif Char2Button.positionCheck(MousePosition):
                        P2Char = Char2Still
                    elif Char3Button.positionCheck(MousePosition):
                        P2Char = Char3Still
                    elif Char4Button.positionCheck(MousePosition):
                        P2Char = Char4Still
            # Checks both players have selected a character before proceeding
            elif (P1Char != "") and (P2Char != ""):
                StateInCharacterSelection = False
                StateInMapSelection = True
                pg.event.set_blocked(MOUSEBUTTONDOWN)
        # Map selection menu, 1 player can choose what map to play
        elif StateInMapSelection:
            # Renders the map selection menu
            Window.fill(BGColour, pg.Rect(0, 0, WinSize[0], WinSize[1]))
            pg.draw.rect(Window, BGAccent, (0, 0, WinSize[0], WinSize[1]), 5)
            MapSelectText.render(Window)
            BG1Button.render(Window)
            BG2Button.render(Window)
            BG3Button.render(Window)
            BG4Button.render(Window)
            ReturnButton.render(Window)
            pg.display.update()
            pg.event.set_allowed(MOUSEBUTTONDOWN)
            # Checks for input and position to choose a map
            if event.type == MOUSEBUTTONUP:
                ButtonClicked = pg.mouse.get_pressed()
                MousePosition = pg.mouse.get_pos()
                # Resets the character chosen before returning
                if ReturnButton.positionCheck(MousePosition):
                    StateInMapSelection = False
                    StateInCharacterSelection = True
                    P1Char = ""
                    P2Char = ""
                # Checks mouse activity is in here and assigns the background to it
                elif BG1Button.positionCheck(MousePosition):
                    ChosenMap = BG1
                elif BG2Button.positionCheck(MousePosition):
                    ChosenMap = BG2
                elif BG3Button.positionCheck(MousePosition):
                    ChosenMap = BG3
                elif BG4Button.positionCheck(MousePosition):
                    ChosenMap = BG4
                # If the map has been chosen then it loads the stage before moving on to the actual game
                if ChosenMap != "":
                    StateInMapSelection = False
                    InMenu = False
    Clock.tick(60)

# Menu loop which lets the player configure game/program data
print(f"""---------------------
Starting game...
Chosen Characters : 
P1 : {P1Char}, P2 : {P2Char}
Map : 
{ChosenMap}
Colours : 
{BGColour}, {BGAccent}, {SubBGColour}, {SubBGAccent}
Scale : 
{Scale}
---------------------""")
Player1 = SpriteClass.defSprite("Player 1", [WinSize[0] * 0.1 + 25, WinSize[1] - 56], P1Char)
Player2 = SpriteClass.defSprite("Player 2", [WinSize[0] * 0.9 - 25, WinSize[1] - 56], P2Char)
Window.blit(ChosenMap, (0, 0))
Player1.render(Window)
Player2.render(Window)
CountDown.render(Window)
pg.display.update()
pg.time.wait(999)
for x in range(2, 0, -1):
    CountDown = UIScript.TextGen(30, f"Begin in : {x}", True, DefColour, CentreX, TopY) # Pos at top centre
    CountDown.render(Window)
    pg.display.update()
    pg.time.wait(999)
CountDown = UIScript.TextGen(30, "!!! Begin Battle !!!", True, DefColour, CentreX, TopY) # Pos at top centre
CountDown.render(Window)
pg.display.update()
pg.time.wait(250)
# Renders the map and characters
Window.blit(ChosenMap, (0, 0))
Player1.render(Window)
Player2.render(Window)
print("""-----------\nLoaded game\n-----------""")
InGame = True
while InGame:
    for event in pg.event.get():
        # Checks through the list of keys pressed for movement updates
        PressedKeys = pg.key.get_pressed()
        # Quit the game
        if (event.type == pg.QUIT) or (PressedKeys[K_ESCAPE]) or (Player1.health < 1) or (Player2.health < 1):
            InGame = False
            pg.quit()
            print("""-------------\nExited pygame\n-------------""")
            quit()
        # Checks for input and performs the respective actions
        # Player 1 movement and actions
        # Movements
        if PressedKeys[K_a]:
            Player1.moveBackward(Window, ChosenMap)
            Player2.render(Window)
        elif PressedKeys[K_d]:
            Player1.moveForward(Window, ChosenMap)
            Player2.render(Window)
        # Actions
        if PressedKeys[K_e]:
            Player1.attackPunch(Player2)
        elif PressedKeys[K_q]:
            Player1.attackKick(Player2)
        elif PressedKeys[K_w]:
            Player1.heal()
        # Player 2 movements and actions
        # Movements
        if PressedKeys[K_RIGHT]:
            Player2.moveForward(Window, ChosenMap)
            Player1.render(Window)
        elif PressedKeys[K_LEFT]:
            Player2.moveBackward(Window, ChosenMap)
            Player1.render(Window)
        # Actions
        if PressedKeys[K_RSHIFT]:
            Player2.attackPunch(Player1)
        elif PressedKeys[K_SLASH] or PressedKeys[K_QUESTION]:
            Player2.attackKick(Player1)
        elif PressedKeys[K_UP]:
            Player2.heal()
    # Updates any changes to the display and ensures the game runs smoothly
    pg.display.update()
    Clock.tick(60) # Change to 45 if it breaks

# TODO : Document code better
# TODO : Implement better user feedback for buttons and text and player data in game
# TODO : Allow user changed settings
# TODO : Implement more actions for characters
# TODO : Implement animations

# I'm sorry for whoever has to read this, I hope you enjoy understanding how this works
# I made some good progress yesterday, made the base of the game so then I can actually implement the mechanics - message to Zeke since it was register in the study room