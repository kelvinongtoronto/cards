import card
from random import shuffle

class Deck(object):
    '''A deck of Cards.'''

    # The four suits, representing Clubs, Diamonds, Hearts, and Spades.
    #SUITS = [chr(9830), chr(9827), chr(9829), chr(9824)] #unicode black suits
    #SUITS = [chr(9826), chr(9831), chr(9825), chr(9828)] #white suits
    #SUITS = ['S','H','C','D'] #letters

    # The 13 ranks, representing
    # 2, 3, ..., 9, 10, Jack, Queen, King, and Ace.
    #RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

    # def __init__(self, low='2', high='A'):
        # '''() -> Deck
        # Create new Deck with 52 face-down cards.
        # '''

        ##The top card is at self.cards[-1]
        # self.cards = []
        # low_i = Deck.RANKS.index(low)
        # high_i = Deck.RANKS[low_i:].index(high) + low_i
        # for suit in Deck.SUITS:
            # for rank in Deck.RANKS[low_i : high_i + 1]:
                # self.cards.append(card.Card(suit, rank))
    
    def __init__(self, suits=['S','H','C','D'], ranks=['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A'], backs=['XX'], jokers=[], unicard=False, color=False):
        '''() -> Deck
        Create new Deck with 52 face-down cards.
        '''
        self.SUITS = suits
        self.RANKS = ranks
        self.BACKS = backs
        # The top card is at self.cards[-1]
        self.cards = []
        for back in backs:
            for suit in suits:
                for rank in ranks:
                    self.cards.append(card.Card(self, suit, rank, back, unicard, color))
            for joker in jokers:
                self.cards.append(card.Card(self, '', joker, back, unicard, color))

    def shuffle(self):
        '''() -> NoneType
        Randomly rearrange the cards in the Deck.
        '''

        shuffle(self.cards)
        
    def is_empty(self):
        '''() -> bool
        Return True iff this Deck has no cards.
        '''
        
        return len(self.cards) == 0
    
    def get_next_card(self):
        '''() -> Card
        Remove and return this deck's next Card, face down.
        The Deck must not be empty.
        '''

        return self.cards.pop()
        
    def deal_next_card(self):
        '''() -> Card
        Remove and return this deck's next Card, face up.
        The Deck must not be empty.
        '''

        c = self.cards.pop()
        c.turn_over()
        return c
        
    def get_cards(self):#not a required function
        '''()-> list
        '''
        cards=[]
        for next_card in self.cards:
            if not next_card.is_face_up:
                next_card.turn_over()
            cards.append(str(next_card))
        return (cards)
