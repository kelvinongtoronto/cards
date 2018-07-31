from card import Card
from deck import Deck

d1=Deck()
d1.shuffle()

c0=d1.get_next_card()
c0.turn_over()
c1=d1.get_next_card()
c1.turn_over()
c2=d1.get_next_card()
c2.turn_over()
c3=d1.get_next_card()
c3.turn_over()

tableau=[c0,c1,c2,c3]

while not d1.is_empty():
	print('0:',tableau[0],' 1:',tableau[1],' 2:',tableau[2],' 3:',tableau[3],' cards left:',len(d1.cards))
	cover=input('select cards to cover:')
	if len(cover)==2:
		if tableau[int(cover[0])].rank==tableau[int(cover[1])].rank or tableau[int(cover[0])].suit==tableau[int(cover[1])].suit:
			if not d1.is_empty(): c0=d1.deal_next_card()
			tableau[int(cover[0])]=c0
			if not d1.is_empty(): c1=d1.deal_next_card()
			tableau[int(cover[1])]=c1
		else:
			print('invalid input. cards must have same suit or same rank.')
	elif len(cover)==3:
		if (tableau[int(cover[0])].rank==tableau[int(cover[1])].rank and tableau[int(cover[0])].rank==tableau[int(cover[2])].rank)or(tableau[int(cover[0])].suit==tableau[int(cover[1])].suit and tableau[int(cover[0])].suit==tableau[int(cover[2])].suit):
			if not d1.is_empty(): c0=d1.deal_next_card()
			tableau[int(cover[0])]=c0
			if not d1.is_empty(): c1=d1.deal_next_card()
			tableau[int(cover[1])]=c1
			if not d1.is_empty(): c2=d1.deal_next_card()
			tableau[int(cover[2])]=c2
		else:
			print('invalid input. cards must have same suit or same rank.')
	elif len(cover)==4:
		if (tableau[int(cover[0])].rank==tableau[int(cover[1])].rank and tableau[int(cover[0])].rank==tableau[int(cover[2])].rank and tableau[int(cover[0])].rank==tableau[int(cover[3])].rank) or (tableau[int(cover[0])].suit==tableau[int(cover[1])].suit and tableau[int(cover[0])].suit==tableau[int(cover[2])].suittableau[int(cover[0])].suit==tableau[int(cover[3])].suit):
			if not d1.is_empty(): c0=d1.deal_next_card()
			tableau[int(cover[0])]=c0
			if not d1.is_empty(): c1=d1.deal_next_card()
			tableau[int(cover[1])]=c1
			if not d1.is_empty(): c2=d1.deal_next_card()
			tableau[int(cover[0])]=c2
			if not d1.is_empty(): c2=d1.deal_next_card()
			tableau[int(cover[1])]=c2
		else:
			print('invalid input. cards must have same suit or same rank.')		
	else:
		print('invalid input. must input 2-4 cards to cover.')
		
if d1.is_empty():
		print('0:',tableau[0],' 1:',tableau[1],' 2:',tableau[2],' 3:',tableau[3],' cards left:',len(d1.cards))
		print("No more cards. You win!")

