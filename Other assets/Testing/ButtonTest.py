# Test Program - Creates a window and tests a button
import pygame as pg
from pygame.locals import *
pg.init()

# Button
class ButtonGenTest:
    def __init__(self, font, size, text, antialias, textColour, backgroundColour):#, textBackground, textTransformation):
        self.font = pg.font.Font(font, size)
        self.text = self.font.render(text, antialias, textColour, backgroundColour)
        self.rect = self.text.get_rect()
        self.rect.center = (1920//2, 1080//2)
        self.X = self.rect[0]
        self.Y = self.rect[1]
        self.Wid = self.X + self.rect[2]
        self.Hig = self.Y + self.rect[3]

    # Renders the text onto the screen
    def render(self):
        Screen.blit(self.text, self.rect)

# Main Program
# Initializes the screen and creates a button object
Screen = pg.display.set_mode((1920, 1080))
pg.display.set_caption("Button test program")

Button = ButtonGenTest("freesansbold.ttf", 54, "Click for Discord Light Mode", True, (255, 255, 0), (0, 255, 255))
Button.render()

# Main game loop
Running = True
while Running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            Running = False
        elif (event.type == pg.KEYDOWN) and (event.key == K_ESCAPE):
            Running = False
        elif pg.mouse.get_pressed()[0] == 1:
            MousePosition = pg.mouse.get_pos()
            print(MousePosition)
            if (Button.X < MousePosition[0] < Button.Wid) & (Button.Y < MousePosition[1] < Button.Hig):
                Screen.fill((255, 255, 255), pg.Rect(0, 0, 1920, 1080))
    pg.display.update()
pg.quit()
quit()