import pygame, sys
from card import Card
from deck import Deck
from pygame.locals import *
from random import random

pygame.init()
screen = pygame.display.set_mode((1600, 220))
pygame.display.set_caption('Hello World!')
BACKGROUND = (0,128,0)
TEXTCOLOR = (255,255,0)
TEXT_X, TEXT_Y, TEXT_WIDTH, TEXT_HEIGHT = 10, 120, 300, 30
screen.fill(BACKGROUND)
fontObj = pygame.font.Font('freesansbold.ttf', 26)

origin1 = (0,0)
xseparation = 20

# Load the image
# img = pygame.image.load("jeu-de-tarot-complet.png")
img = pygame.image.load("Tarotcards.jpg")
img = pygame.transform.scale_by(img, 0.5)
width, height = img.get_width()/14, img.get_height()/6

SUITS = ['P', 'C', 'K', 'T'] #pique, coeur, carreau, trefle
RANKS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'X', 'V', 'C', 'D', 'R']
BACKS = ['XX']
JOKER = [str(i) for i in range(1,23)]

#create the deck
d = Deck(SUITS,RANKS,BACKS,JOKER)
d.shuffle()

tableau={}

def get_moused_card(mx, my):
    for card,position in tableau.items():
        if position[0][0]<mx<position[1][0] and position[0][1]<my<position[1][1]:
            return card
    return None
    
while True: # main game loop
    if not d.is_empty():
        # draw a card
        c = d.deal_next_card()# if random()>0.5 else d.get_next_card()
        if c.is_joker():
            i = JOKER.index(c.rank)
            rank = i if i < 14 else i - 14
            suit = 0 if i < 14 else 1
        else:
            rank = RANKS.index(c.rank)
            suit = SUITS.index(c.suit) + 2
        
        # Blit the card
        if c.is_face_up:
            source_area = pygame.Rect((width*rank, height*suit), (width, height))
        else:
            source_area = pygame.Rect((width*13, height*1), (width, height))
            
        screen.blit(img, origin1, source_area)
        tableau[c] = (origin1, (origin1[0]+xseparation, origin1[1]+height))
        origin1 = origin1 if d.is_empty() else (origin1[0] + xseparation, origin1[1])
        
        pygame.draw.rect(screen, BACKGROUND, (TEXT_X, TEXT_Y, TEXT_WIDTH, TEXT_HEIGHT))
        textSurfaceObj = fontObj.render(str(c), True, TEXTCOLOR)
        screen.blit(textSurfaceObj, (TEXT_X, TEXT_Y))
        
        if d.is_empty():
            tableau[c] = (origin1, (origin1[0]+width, origin1[1]+height))
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEMOTION:
            mousex, mousey = event.pos
            if d.is_empty():
                pygame.draw.rect(screen, BACKGROUND, (TEXT_X, TEXT_Y, TEXT_WIDTH, TEXT_HEIGHT))
                moused_card = get_moused_card(mousex, mousey)
                textSurfaceObj = fontObj.render(str(moused_card) if moused_card else '', True, TEXTCOLOR)
                screen.blit(textSurfaceObj, (TEXT_X, TEXT_Y))
    pygame.display.update()
    pygame.time.wait(50)
