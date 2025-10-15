import pygame, sys
from pygame.locals import *
from card import Card
from deck import Deck

GAMES = ["Highest Hand", "Lowest Hand", "Small to Big", "Royal Family", "Four Kings"]
RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
SUITS = ['S','H','C','D']
BACKS = [(0,4), (1,4), (2,4), (3,4), (4,4), (5,4), (6,4), (9,4), (0,5), (1,5), (3,5), (6,5)]

pygame.init()
screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption('Enter 1-5 on keyboard to start a game.')
BACKGROUND = (0,128,0)
TEXTCOLOR = (255,255,0)
screen.fill(BACKGROUND)

# define playfield positions
PLAYER_HAND = [(150,280), (250,280), (350,280), (450,280)]
OPPONENT_HAND = [(150,30), (250,30), (350,30), (450,30)]
DRAW_PILE = (300,150)
DISCARD = (400,150)
SHOW_CARDS = (10, 300)

# Load the image
img = pygame.image.load("SolitaireCards.png")
width, height = img.get_width()/13, img.get_height()/6
trash = pygame.image.load("trash1.png")
trashed = pygame.image.load("trash2.png")
button = pygame.image.load("button.png")

# Load sounds
trash_sound = pygame.mixer.Sound("trash.wav")
card_flip = pygame.mixer.Sound("cardflip.wav")

# Define Text parameters
fontObj = pygame.font.Font('freesansbold.ttf', 20)
TEXT_X = 10
TEXT_Y = [140, 160, 180, 200, 220, 240]
TEXT_WIDTH, TEXT_HEIGHT = 290, 125

class Game(object):
    def __init__(self):
        self.current_back = 0
        self.mode_selected = False
        self.game_on = False
        self.players_turn = False
        self.game_mode = 0
        self.delay = 0
        self.frame = 0

    def new_game(self):
        d1=Deck(SUITS,RANKS)
        if self.game_mode == 5:
            for i in range(3):
                for suit in SUITS:
                    d1.cards.append(Card(d1,suit,'K'))
        d1.shuffle()

        #Deal Cards
        c0=d1.get_next_card()
        c0.turn_over()
        e0=d1.get_next_card()

        c1=d1.get_next_card()
        c1.turn_over()
        e1=d1.get_next_card()

        c2=d1.get_next_card()
        c2.turn_over()
        e2=d1.get_next_card()

        c3=d1.get_next_card()
        c3.turn_over()
        e3=d1.get_next_card()

        self.player=[c0,c1,c2,c3]
        self.opponent=[e0,e1,e2,e3]
        self.player_discarded = [False, False, False, False]
        self.opponent_discarded = [False, False, False, False]
        self.deck = d1

g = Game()

def set_game_mode(key):
    g.game_mode = key
    g.mode_selected = True
    g.game_on = True
    g.players_turn = True
    g.new_game()
    pygame.display.set_caption(f"Playing {GAMES[key-1]}")

def clicked_card(x,y,i):
    return x>=PLAYER_HAND[i][0] and x<=PLAYER_HAND[i][0]+width and y>=PLAYER_HAND[i][1] and y<=PLAYER_HAND[i][1]+height

def select_card(upx,upy):
    if not g.game_on:
        g.current_back = (g.current_back + 1) % len(BACKS)
    if g.players_turn:
        if upx>=DRAW_PILE[0] and upx<=DRAW_PILE[0]+width and upy>=DRAW_PILE[1] and upy<=DRAW_PILE[1]+height:
            for i in range(4):
                if g.player_discarded[i]:
                    pygame.mixer.Sound.play(card_flip)
                    new_card = g.deck.get_next_card()
                    new_card.turn_over()
                    g.player[i] = new_card
                    g.player_discarded[i] = False
                    g.players_turn = False
        elif upx>=SHOW_CARDS[0] and upx<=SHOW_CARDS[0]+89 and upy>=SHOW_CARDS[1] and upy<=SHOW_CARDS[1]+33:
            if not any(g.player_discarded):
                show_hands()

def swap_cards(downx,downy,upx,upy):
    if upx>=DISCARD[0] and upx<=DISCARD[0]+width and upy>=DISCARD[1] and upy<=DISCARD[1]+height:
        for i in range(4):
            if clicked_card(downx,downy,i):
                pygame.mixer.Sound.play(trash_sound)
                g.player_discarded[i] = True
    
def get_card_rect(card, frame=0):
    if card.is_face_up:
        pci_rank = RANKS.index(card.rank)
        pci_suit = SUITS.index(card.suit)
        return pygame.Rect((width*pci_rank, height*pci_suit), (width, height))
    else:
        a = BACKS[g.current_back]
        if a == (1,5):
            if frame < 15 or (frame > 30 and frame < 45):
                return pygame.Rect((width*(a[0]+1), height*(a[1])), (width, height))
            else:
                return pygame.Rect((width*a[0], height*a[1]), (width, height))
        elif a in [(6,4), (3,5), (6,5)]:
            if frame < 15:
                return pygame.Rect((width*(a[0]), height*(a[1])), (width, height))
            elif frame < 30 or frame > 45:
                return pygame.Rect((width*(a[0]+1), height*(a[1])), (width, height))
            else:
                return pygame.Rect((width*(a[0]+2), height*(a[1])), (width, height))
        else:
            return pygame.Rect((width*a[0], height*a[1]), (width, height))

def lowest_card(): # playing Highest Hand
    if calc_score(g.opponent) >= 30:
        show_hands()
    else:
        lowest = 0
        for i in [1,2,3]:
            if g.opponent[i] < g.opponent[lowest]:
                lowest = i
        pygame.mixer.Sound.play(trash_sound)
        g.opponent_discarded[lowest] = True

def highest_card(): # playing Lowest Hand
    if calc_score(g.opponent) <= 10:
        show_hands()
    else:
        highest = 0
        for i in [1,2,3]:
            if g.opponent[i] > g.opponent[highest]:
                highest = i
        pygame.mixer.Sound.play(trash_sound)
        g.opponent_discarded[highest] = True

def out_of_order(): # playing Small to Big
    if in_order(g.opponent):
        show_hands()
    else:
        discard = 0
        threshold = [Card('','','7'),Card('','','9'),Card('','','J'),Card('','','K')]
        for c in [0,1,2,3]:
            if g.opponent[c] > threshold[c]:
                discard = c
                break
            else:
                if c != 0 and g.opponent[c] < g.opponent[c-1]:
                    discard = c
                    break
        pygame.mixer.Sound.play(trash_sound)
        g.opponent_discarded[discard] = True

def not_royal(): # playing Royal Family
    discard = -1
    for i in [0,1,2,3]:
        if not (g.opponent[i].rank in ['J','Q','K']):
            discard = i
            break
    if discard == -1:
        show_hands()
    else:
        pygame.mixer.Sound.play(trash_sound)
        g.opponent_discarded[discard] = True

def not_king(): # playing Four Kings
    discard = -1
    for i in [0,1,2,3]:
        if g.opponent[i].rank != 'K':
            discard = i
            break
    if discard == -1:
        show_hands()
    else:
        pygame.mixer.Sound.play(trash_sound)
        g.opponent_discarded[discard] = True

def opponent_draws_card():
    for i in range(4):
        if g.opponent_discarded[i]:
            pygame.mixer.Sound.play(card_flip)
            new_card = g.deck.get_next_card()
            g.opponent[i] = new_card
            g.opponent_discarded[i] = False
            g.players_turn = True

def calc_score(hand): # for games 0, 1
    score = 0
    for c in hand:
        if c.rank == 'A':
            score += 1
        elif c.rank == 'T' or c.rank == 'J' or c.rank == 'Q' or c.rank == 'K':
            score += 10
        else:
            score += int(c.rank)
    return score
    
def in_order(hand): # for game 2
    last_card = hand[0]
    for this_card in hand[1:]:
        if last_card > this_card:
            return False
        else:
            last_card = this_card
    return True
    
def count_cards(hand): # for game 3, 4
    cards = 0
    for c in hand:
        if c.rank == 'K':
            cards += 1
        elif (c.rank == 'J' or c.rank == 'Q') and g.game_mode == 4:
            cards += 1
    return cards
    
def show_hands():
    for e in g.opponent:
        e.turn_over()
        
    g.game_on = False
    g.players_turn = False

while True:
    mouseClicked = False
    
    screen.blit(img, DRAW_PILE, get_card_rect(Card('','',''), g.frame))
    
    if g.mode_selected and g.game_on: #game on state
        #blit trash
        if any(g.player_discarded) or any(g.opponent_discarded):
            screen.blit(trashed, DISCARD)
        else:
            screen.blit(trash, DISCARD)
        
        #blit cards
        for i in range(4):
            if g.player_discarded[i]:
                pygame.draw.rect(screen, BACKGROUND, pygame.Rect(PLAYER_HAND[i], (width, height)))
            else:
                player_card_i = g.player[i]
                source_area_p = get_card_rect(player_card_i)
                screen.blit(img, PLAYER_HAND[i], source_area_p)
            
            if g.opponent_discarded[i]:
                pygame.draw.rect(screen, BACKGROUND, pygame.Rect(OPPONENT_HAND[i], (width, height)))
            else:
                opponent_card_i = g.opponent[i]
                source_area_o = get_card_rect(opponent_card_i, g.frame)
                screen.blit(img, OPPONENT_HAND[i], source_area_o)
        
        if g.deck.is_empty():
            g.game_on = False
        else:
            if g.players_turn:
                text_fields = ["Now it's your turn.", "Pick a card and", "throw it in the trash.", "Then, deal a new card", "from the deck."]
                if g.game_mode == 1:
                    text_fields[1] = "Pick your LOWEST card and"
                elif g.game_mode == 2:
                    text_fields[1] = "Pick your HIGHEST card and"
            else:
                text_fields = ["Now i get my turn!", "", "", "", ""]
                if g.delay<5:
                    g.delay += 1
                else:
                    g.delay = 0
                    if any(g.opponent_discarded):
                        opponent_draws_card()
                    else:
                        if g.game_mode == 1:
                            lowest_card()
                        elif g.game_mode == 2:
                            highest_card()
                        elif g.game_mode == 3:
                            out_of_order()
                        elif g.game_mode == 4:
                            not_royal()
                        elif g.game_mode == 5:
                            not_king()
    elif g.mode_selected: #game over state
        for i in range(4):
            player_card_i = g.player[i]
            source_area_p = get_card_rect(player_card_i)
            screen.blit(img, PLAYER_HAND[i], source_area_p)
            
            opponent_card_i = g.opponent[i]
            source_area_o = get_card_rect(opponent_card_i)
            screen.blit(img, OPPONENT_HAND[i], source_area_o)
            
        text_fields[0] = "Game Over."
        if g.game_mode == 1:
            opponent_value = calc_score(g.opponent)
            player_value = calc_score(g.player)
            text_fields[1] = f"My hand equals {opponent_value}."
            text_fields[2] = f"Your hand equals {player_value}."
            
            if player_value > opponent_value:
                text_fields[3] = "You win!"
            elif player_value < opponent_value:
                text_fields[3] = "I win!"
            else:
                text_fields[3] = "It's a draw! We both win!"
        elif g.game_mode == 2:
            opponent_value = calc_score(g.opponent)
            player_value = calc_score(g.player)
            text_fields[1] = f"My hand equals {opponent_value}."
            text_fields[2] = f"Your hand equals {player_value}."
            
            if player_value < opponent_value:
                text_fields[3] = "You win!"
            elif player_value > opponent_value:
                text_fields[3] = "I win!"
            else:
                text_fields[3] = "It's a draw! We both win!"
        elif g.game_mode == 4 or g.game_mode == 5:
            opponent_value = count_cards(g.opponent)
            player_value = count_cards(g.player)
            if opponent_value == 1 :
                text_fields[1] = f"My hand has 1 {"king" if g.game_mode==5 else "court card"}."
            else:
                text_fields[1] = f"My hand has {opponent_value} {"kings" if g.game_mode==5 else "court cards"}."
            if player_value == 1:
                text_fields[2] = f"Your hand has 1 {"king" if g.game_mode==5 else "court card"}."
            else:
                text_fields[2] = f"Your hand has {player_value} {"kings" if g.game_mode==5 else "court cards"}."
                
            if player_value == 4 and opponent_value == 4:
                text_fields[3] = "It's a draw! We both win!"
            elif player_value == 4:
                text_fields[3] = "You win!"
            elif opponent_value == 4:
                text_fields[3] = "I win!"
            else:
                text_fields[3] = "It's a draw! We both lose."
        else:
            opponent_value = in_order(g.opponent)
            player_value = in_order(g.player)
            text_fields[1] = f"My hand is{"" if opponent_value else " not"} in order."
            text_fields[2] = f"Your hand is{"" if player_value else " not"} in order."
            if player_value and opponent_value:
                text_fields[3] = "It's a draw! We both win!"
            elif player_value:
                text_fields[3] = "You win!"
            elif opponent_value:
                text_fields[3] = "I win!"
            else:
                text_fields[3] = "It's a draw! We both lose."
        text_fields[4] = "Choose 1-5 to play again."
        pygame.display.set_caption('1:Highest Hand, 2:Lowest Hand, 3:Small to Big, 4:Royal Family, 5:Four Kings')
    else: #initial state
        text_fields = ["Choose a game mode:", "1: Highest Hand", "2: Lowest Hand", "3: Small to Big", "4: Royal Family", "5: Four Kings"]
        
    # blit text
    pygame.draw.rect(screen, BACKGROUND, (TEXT_X, TEXT_Y[0], TEXT_WIDTH, TEXT_HEIGHT))
    for t in range(len(text_fields)):
        textSurfaceObj = fontObj.render(text_fields[t], True, TEXTCOLOR)
        screen.blit(textSurfaceObj, (TEXT_X, TEXT_Y[t]))
    
    # blit buttons
    screen.blit(button, SHOW_CARDS)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            downx, downy = event.pos
        elif event.type == MOUSEBUTTONUP:
            mouseClicked = True
            upx, upy = event.pos
            if upx==downx and upy==downy:
                select_card(upx,upy)
            else:
                if g.players_turn and not any(g.player_discarded): swap_cards(downx,downy,upx,upy)
        elif event.type == KEYDOWN:
            if event.key == K_1:
                set_game_mode(1)
            elif event.key == K_2:
                set_game_mode(2)
            elif event.key == K_3:
                set_game_mode(3)
            elif event.key == K_4:
                set_game_mode(4)
            elif event.key == K_5:
                set_game_mode(5)
    pygame.display.update()
    pygame.time.wait(50)
    g.frame = (g.frame + 1) % 60
