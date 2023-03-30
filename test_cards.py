from card import Card
from deck import Deck

#SUITS = [chr(9830), chr(9827), chr(9829), chr(9824)] #black suits
#SUITS = [chr(9826), chr(9831), chr(9825), chr(9828)] #white suits
SUITS = [chr(c) for c in range(9824,9832)]


d1 = Deck(suits=SUITS, ranks=['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'C', 'Q', 'K'], backs=['XX','YY','ZZ'], unicard=False, color=True)
c=0
#d1.shuffle()
for card in d1.cards:
    print(card, end='-')
    card.turn_over()
    print(card, end=' ' if c!=13 else '\n')
    if c==13: c=0
    else: c+=1