import pygame, sys
from card import Card
from deck import Deck
from pygame.locals import *
import random

pygame.init()
screen = pygame.display.set_mode((1440, 780))
pygame.display.set_caption('Hello World!')
BACKGROUND = (0,128,0)
TEXTCOLOR = (255,255,0)
TEXT_X, TEXT_Y, TEXT_WIDTH, TEXT_HEIGHT = 1225, 745, 300, 30
screen.fill(BACKGROUND)
fontObj = pygame.font.Font('freesansbold.ttf', 26)

origin1 = (0,0)
row = 0
col = 0

COLS = 19

BN = 7
BM = 5

#FN = 1

# Load the image
img = pygame.image.load("Balatro.png")
backs = pygame.image.load("Balatro (Card Backs).png")
width, height = backs.get_width()/BN, backs.get_height()/BM
#FRONT = pygame.Rect((width*(FN%BN), height*(FN//BN)), (width, height))

#create the deck
SUITS = ['H', 'C', 'D', 'S']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
BACKS = ['RED', 'BLUE', 'YELLOW', 'GREEN', 'BLACK', 'MAGIC', 'NEBULA', 'GHOST', 'ABANDON', 'CHECKER', 'ZODIAC', 'PAINTED', 'ANAGLYPH', 'PLASMA', 'ERRATIC', 'CHALLENGE', 'LOCK']
BINDX = [0,14,15,16,17,21,3,20,24,22,31,25,30,18,23,28,4]
FRONTS = ['', 'bonus', 'multi', 'wild', 'steel', 'stone', 'gold', 'lucky', 'glass']
FINDX = [1,8,9,10,13,5,6,11,12]

d = Deck(SUITS, RANKS, random.sample(BACKS,3))
d.shuffle()

tableau={}
enhancements={}

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
            fn = FINDX[FRONTS.index(enhancements[moused_card])]
            front = pygame.Rect((width*(fn%BN), height*(fn//BN)), (width, height))
            screen.blit(backs, origin, front)
            source_area = pygame.Rect((width*rank, height*suit), (width, height))
            screen.blit(img, origin, source_area)
        else:
            deck_number = BINDX[BACKS.index(moused_card.back)]
            source_area = pygame.Rect((width*(deck_number%BN), height*(deck_number//BN)), (width, height))
            screen.blit(backs, origin, source_area)
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
            fn1 = FINDX[FRONTS.index(enhancements[card1])]
            front1 = pygame.Rect((width*(fn1%BN), height*(fn1//BN)), (width, height))
            screen.blit(backs, origin1, front1)
            source_area1 = pygame.Rect((width*rank1, height*suit1), (width, height))
            screen.blit(img, origin1, source_area1)
        else:
            deck1 = BINDX[BACKS.index(card1.back)]
            source_area1 = pygame.Rect((width*(deck1%BN), height*(deck1//BN)), (width, height))
            screen.blit(backs, origin1, source_area1)
            
        if card2.is_face_up:
            fn2 = FINDX[FRONTS.index(enhancements[card2])]
            front2 = pygame.Rect((width*(fn2%BN), height*(fn2//BN)), (width, height))
            screen.blit(backs, origin2, front2)
            source_area2 = pygame.Rect((width*rank2, height*suit2), (width, height))
            screen.blit(img, origin2, source_area2)
        else:
            deck2 = BINDX[BACKS.index(card2.back)]
            source_area2 = pygame.Rect((width*(deck2%BN), height*(deck2//BN)), (width, height))
            screen.blit(backs, origin2, source_area2)
    except:
        pass
        
while True: # main game loop
    mouseClicked = False
    if not d.is_empty():
        # draw a card
        c = d.deal_next_card() if random.random()>0.5 else d.get_next_card()
        rank = RANKS.index(c.rank)
        suit = SUITS.index(c.suit)
        mod = random.choice(FRONTS[:-1])
        # Blit the card
        if c.is_face_up:
            #mod = random.choice(FRONTS[:-1])
            fn = FINDX[FRONTS.index(mod)]
            front = pygame.Rect((width*(fn%BN), height*(fn//BN)), (width, height))
            screen.blit(backs, origin1, front)
            source_area = pygame.Rect((width*rank, height*suit), (width, height))
            screen.blit(img, origin1, source_area)
        else:
            #mod = 
            deck_number = BINDX[BACKS.index(c.back)]
            source_area = pygame.Rect((width*(deck_number%BN), height*(deck_number//BN)), (width, height))
            screen.blit(backs, origin1, source_area)
        tableau[c] = (origin1, (origin1[0]+width, origin1[1]+height))
        enhancements[c] = mod
        
        if col==(COLS):
            origin1 = (0, origin1[1] + height)
            row+=1
            col=0
        else:
            origin1 = (origin1[0] + width, origin1[1])
            col+=1
            
        pygame.draw.rect(screen, BACKGROUND, (TEXT_X, TEXT_Y, TEXT_WIDTH, TEXT_HEIGHT))
        card_str = f"{mod} {str(c)}" if c.is_face_up else str(c)
        textSurfaceObj = fontObj.render(card_str, True, TEXTCOLOR)
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
                textSurfaceObj = fontObj.render(f"{enhancements[moused_card] if moused_card.is_face_up else ''} {str(moused_card)}" if moused_card else '', True, TEXTCOLOR)
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
