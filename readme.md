# Introduction
 - Hello, this is our cooperative program by SAM and REESE
 - This is a fighting platformer in pycharm

# Flow of game for user
 - Character selection
 - Load into map and countdown
 - Fight until health depleted
 - Restart or quit game

# Main program
 - Load menu
 - User selects character
 - Load battleground and character
 - When user presses certain keys
    - Play sprite and calculate damage based on hitbox
    - Or interact with the game system
 - When lives end
    - Load menu 

# Main
# Variable/Constant
 - Creates/loads different variables/constants
 - 
# Load visual assets
 - Loads images (Characters, Maps, Misc)
# Sprite creation
 - Creates sprites/buttons with classes
# Load screen
 - Loads all visual assets to screen along with other items to load

# Sprite Class
A class for creating sprites
 - Creates physical sprite with attributes
 - Creates a set of possible moves (Currently : Punch, Kick)

# Button Generator
Creates buttons containing text or images allowing users to interact with the system easier
 - Takes attributes of the button and creates it
 - Methods will be used to provide functionality

# Current scene generator
Stores objects of the current scene and attributes (E.g. POS)
 - Store different visual object in categories
 - Store their attributes if applicable
 - Can change record of object and their attribute 
 - Reapplies every object when record is changed

# Sprites to draw : (Scenes(xxx scenes(Plain(WII Fit scene at Smash Bros), Hell(Cuphead devil boss battle scene), Forest(GI Mondstat), Beach(GI Mualani))), Characters(3 character based on colour(Still, hit, kick, heal, jump, move forward(reverse image for backward), crouch)), Effects(Physical hit, Ground particle), Text Background(Scroll, Paper in gold frame))

# Others : Somehow get collision detection working
# Additional features : Settings, Tutorial, more keybind options, more assets(map, character(gif/img), sound,
# additional objects, more gameplay changes(map objects, skills and mechanics of their interaction)),
# add easter eggs like animation or something
