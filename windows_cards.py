import pygame, sys
from card import Card
from deck import Deck
from pygame.locals import *
from random import random

pygame.init()
screen = pygame.display.set_mode((980, 780))
pygame.display.set_caption('Hello World!')
BACKGROUND = (0,128,0)
TEXTCOLOR = (255,255,0)
TEXT_X, TEXT_Y, TEXT_WIDTH, TEXT_HEIGHT = 925, 745, 300, 30
screen.fill(BACKGROUND)
fontObj = pygame.font.Font('freesansbold.ttf', 26)

origin1 = (0,0)
row=0
col=0

# Load the image
img = pygame.image.load("SolitaireCards.png")
width, height = img.get_width()/13, img.get_height()/6

#create the deck
SUITS = ['S','H','C','D']
RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
BACKS = ['XX', 'YY']
d = Deck(SUITS, RANKS, BACKS)
d.shuffle()

tableau={}

def get_moused_card(mx, my):
    for card,position in tableau.items():
        if position[0][0]<mx<position[1][0] and position[0][1]<my<position[1][1]:
            return card
    return None
    
def flip_card(mx,my):
    try:
        moused_card = get_moused_card(mx,my)
        rank = RANKS.index(moused_card.rank)
        suit = SUITS.index(moused_card.suit)
        origin = tableau[moused_card]
        moused_card.turn_over()
        
        if moused_card.is_face_up:
            source_area = pygame.Rect((width*rank, height*suit), (width, height))
        else:
            deck_number = 0 if moused_card.back=='XX' else 1
            source_area = pygame.Rect((width*(deck_number%13), height*(4+deck_number//13)), (width, height))
        screen.blit(img, origin, source_area)
    except:
        pass
    
def swap_cards(card1x,card1y,card2x,card2y):
    try:
        card1 = get_moused_card(card1x,card1y)
        rank1 = RANKS.index(card1.rank)
        suit1 = SUITS.index(card1.suit)
        
        card2 = get_moused_card(card2x,card2y)
        rank2 = RANKS.index(card2.rank)
        suit2 = SUITS.index(card2.suit)
        
        tableau[card1], tableau[card2] = tableau[card2], tableau[card1]
        
        origin1 = tableau[card1]
        origin2 = tableau[card2]
        
        if card1.is_face_up:
            source_area1 = pygame.Rect((width*rank1, height*suit1), (width, height))
        else:
            deck1 = 0 if card1.back=='XX' else 1
            source_area1 = pygame.Rect((width*(deck1%13), height*(4+deck1//13)), (width, height))
            
        if card2.is_face_up:
            source_area2 = pygame.Rect((width*rank2, height*suit2), (width, height))
        else:
            deck2 = 0 if card2.back=='XX' else 1
            source_area2 = pygame.Rect((width*(deck2%13), height*(4+deck2//13)), (width, height))
            
        screen.blit(img, origin1, source_area1)
        screen.blit(img, origin2, source_area2)
    except:
        pass
        
while True: # main game loop
    mouseClicked = False
    if not d.is_empty():
        # draw a card
        c = d.deal_next_card() if random()>0.5 else d.get_next_card()
        rank = RANKS.index(c.rank)
        suit = SUITS.index(c.suit)
        
        # Blit the card
        if c.is_face_up:
            source_area = pygame.Rect((width*rank, height*suit), (width, height))
        else:
            deck_number = 0 if c.back=='XX' else 1
            source_area = pygame.Rect((width*(deck_number%13), height*(4+deck_number//13)), (width, height))
            
        screen.blit(img, origin1, source_area)
        tableau[c] = (origin1, (origin1[0]+width, origin1[1]+height))
        
        if col==(12):
            origin1 = (0, origin1[1] + height)
            row+=1
            col=0
        else:
            origin1 = (origin1[0] + width, origin1[1])
            col+=1
            
        pygame.draw.rect(screen, BACKGROUND, (TEXT_X, TEXT_Y, TEXT_WIDTH, TEXT_HEIGHT))
        textSurfaceObj = fontObj.render(str(c), True, TEXTCOLOR)
        screen.blit(textSurfaceObj, (TEXT_X, TEXT_Y))
        
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
        elif event.type == MOUSEBUTTONDOWN:
            downx, downy = event.pos
        elif event.type == MOUSEBUTTONUP:
            mouseClicked = True
            upx, upy = event.pos
            if upx==downx and upy==downy:
                if d.is_empty(): flip_card(upx,upy)
            else:
                if d.is_empty(): swap_cards(downx,downy,upx,upy)
    pygame.display.update()
    if not d.is_empty(): pygame.time.wait(50)
