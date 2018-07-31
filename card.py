from functools import total_ordering
import deck

@total_ordering
class Card(object):
    '''A card with a rank and a suit that can be either face up or face down.
    The rank is one of Deck.RANKS and the suit is one of
    Deck.SUITS.'''
    
    def __init__(self, s, r):
        '''(str, str) -> Card
        Create new face-down Card with suit s and rank r.
        '''

        self.suit = s
        self.rank = r
        self.is_face_up = False
        
    def __str__(self):       
        '''() -> str <==> str(self)
        Return this Card's rank and suit or 'XX' if this
        Card is face down.
        '''

        if self.is_face_up:
            return self.rank + self.suit
        else:
            return 'XX'
    
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

        return deck.Deck.RANKS.index(self.rank) < deck.Deck.RANKS.index(other.rank)
    
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

        return deck.Deck.RANKS.index(self.rank) == deck.Deck.RANKS.index(other.rank)
        
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
