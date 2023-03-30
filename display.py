import pygame, sys
from card import Card
from deck import Deck
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((1400, 200))
pygame.display.set_caption('Hello World!')
BACKGROUND = (0,128,0)
TEXTCOLOR = (255,255,0)

origin1 = (0,0)
xseparation = 25

# Load the image
img = pygame.image.load("60x80cards.png")
width, height = img.get_width()/14, img.get_height()/4

#create the deck
d = Deck()
d.shuffle()
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
SUITS = ['S','H','C','D']
#c = d.get_next_card() #face down

screen.fill(BACKGROUND)
while True: # main game loop
    mouseClicked = False
    if not d.is_empty():
        # draw a card
        c = d.deal_next_card()
        rank = RANKS.index(c.rank)
        suit = SUITS.index(c.suit)
        
    # Blit the card
    if c.is_face_up:
        source_area = pygame.Rect((width*rank, height*suit), (width, height))
    else:
        source_area = pygame.Rect((width*13, height*1), (width, height))
    screen.blit(img, origin1, source_area)
    origin1 = origin1 if d.is_empty() else (origin1[0] + xseparation, origin1[1])
    
    if d.is_empty():
        fontObj = pygame.font.Font('freesansbold.ttf', 26)
        textSurfaceObj = fontObj.render('Hello world!', True, TEXTCOLOR)
        screen.blit(textSurfaceObj, (10, 100))
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEMOTION:
            mousex, mousey = event.pos
        elif event.type == MOUSEBUTTONUP:
            mousex, mousey = event.pos
            mouseClicked = True
    pygame.display.update()
    pygame.time.wait(50)
