from functools import total_ordering
import deck
from unicards import unicard

@total_ordering
class Card(object):
    '''A card with a rank and a suit that can be either face up or face down.
    The rank is one of Deck.RANKS and the suit is one of
    Deck.SUITS.'''
    
    def __init__(self, d, s, r, b='XX', unicard_mode=False, color=False):
        '''(str, str, str) -> Card
        Create new face-down Card with suit s and rank r and back design b,
        belonging to Deck d
        '''
        self.deck = d
        self.suit = s
        self.rank = r
        self.back = b
        self.is_face_up = False
        self.unicard_mode = unicard_mode
        self.color = color
        
    def __hash__(self):
        return hash(self.back+'-'+self.rank+self.suit)
        
    def __str__(self):
        '''() -> str <==> str(self)
        Return this Card's rank and suit or its back if this
        Card is face down.
        '''
        if self.is_face_up:
            if self.unicard_mode:
                return unicard(self.rank + self.suit, self.color)
            else:
                return self.rank + self.suit
        else:
            if self.unicard_mode:
                return unicard(self.back) #chr(127136)
            else:
                return self.back
        
    def __lt__(self, other):
        '''(Card) -> bool <==> self<other
        Return True iff this Card is less than other.
        The comparison is done based on the rank of the Cards.
        >>>Card('D','5')<Card('S','6')
        True
        >>>Card('D','7')<Card('S','6')
        False
        >>>Card('D','5')<Card('S','5')
        False
        '''
        return self.deck.RANKS.index(self.rank) < self.deck.RANKS.index(other.rank)
        
    def __eq__(self, other):
        '''(Card) -> bool <==> self==other
        Return True iff this Card has the same rank as other.
        >>>Card('D','5')==Card('S','6')
        False
        >>>Card('D','7')==Card('S','6')
        False
        >>>Card('D','5')==Card('S','5')
        True
        '''
        return self.deck.RANKS.index(self.rank) == self.deck.RANKS.index(other.rank)
        
    def set_value(self,val):
        self.value = val
        
    def turn_over(self):
        '''() -> NoneType
        Flip this Card over.
        '''
        self.is_face_up = not self.is_face_up
        
    def turn_down(self):
        '''() -> NoneType
        Make this Card be face down.
        '''
        self.is_face_up = False
    
    def is_joker(self):
        return self.suit == ''
