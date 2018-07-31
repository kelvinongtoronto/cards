from card import Card
from deck import Deck

if __name__=='__main__':
	d1=Deck()
	d1.shuffle()

	game=True
	
	c1=d1.get_next_card()
	c1.turn_over()
	c2=d1.get_next_card()
	c2.turn_over()
	c3=d1.get_next_card()
	c3.turn_over()
	c4=d1.get_next_card()
	c4.turn_over()

	while not d1.is_empty() and game:
		print('',c1,' ',c2,' ',c3,' ',c4,' cards left:',len(d1.cards))
		if c1.rank==c2.rank and c1.rank==c3.rank and c1.rank==c4.rank:
			if not d1.is_empty(): c1=d1.deal_next_card()
			if not d1.is_empty(): c2=d1.deal_next_card()
			if not d1.is_empty(): c3=d1.deal_next_card()
			if not d1.is_empty(): c4=d1.deal_next_card()
		elif c1.rank==c2.rank and c1.rank==c3.rank:
			if not d1.is_empty(): c1=d1.deal_next_card()
			if not d1.is_empty(): c2=d1.deal_next_card()
			if not d1.is_empty(): c3=d1.deal_next_card()
		elif c1.rank==c2.rank and c1.rank==c4.rank:
			if not d1.is_empty(): c1=d1.deal_next_card()
			if not d1.is_empty(): c2=d1.deal_next_card()
			if not d1.is_empty(): c4=d1.deal_next_card()
		elif c1.rank==c3.rank and c1.rank==c4.rank:
			if not d1.is_empty(): c1=d1.deal_next_card()
			if not d1.is_empty(): c3=d1.deal_next_card()
			if not d1.is_empty(): c4=d1.deal_next_card()
		elif c2.rank==c3.rank and c2.rank==c4.rank:
			if not d1.is_empty(): c2=d1.deal_next_card()
			if not d1.is_empty(): c3=d1.deal_next_card()
			if not d1.is_empty(): c4=d1.deal_next_card()
		elif c1.rank==c2.rank:
			if not d1.is_empty(): c1=d1.deal_next_card()
			if not d1.is_empty(): c2=d1.deal_next_card()
		elif c1.rank==c3.rank:
			if not d1.is_empty(): c1=d1.deal_next_card()
			if not d1.is_empty(): c3=d1.deal_next_card()
		elif c1.rank==c4.rank:
			if not d1.is_empty(): c1=d1.deal_next_card()
			if not d1.is_empty(): c4=d1.deal_next_card()
		elif c2.rank==c3.rank:
			if not d1.is_empty(): c2=d1.deal_next_card()
			if not d1.is_empty(): c3=d1.deal_next_card()
		elif c2.rank==c4.rank:
			if not d1.is_empty(): c2=d1.deal_next_card()
			if not d1.is_empty(): c4=d1.deal_next_card()
		elif c3.rank==c4.rank:
			if not d1.is_empty(): c3=d1.deal_next_card()
			if not d1.is_empty(): c4=d1.deal_next_card()
		elif c1.suit==c2.suit and c1.suit==c3.suit and c1.suit==c4.suit:
			if not d1.is_empty(): c1=d1.deal_next_card()
			if not d1.is_empty(): c2=d1.deal_next_card()
			if not d1.is_empty(): c3=d1.deal_next_card()
			if not d1.is_empty(): c4=d1.deal_next_card()
		elif c1.suit==c2.suit and c1.suit==c3.suit:
			if not d1.is_empty(): c1=d1.deal_next_card()
			if not d1.is_empty(): c2=d1.deal_next_card()
			if not d1.is_empty(): c3=d1.deal_next_card()
		elif c1.suit==c2.suit and c1.suit==c4.suit:
			if not d1.is_empty(): c1=d1.deal_next_card()
			if not d1.is_empty(): c2=d1.deal_next_card()
			if not d1.is_empty(): c4=d1.deal_next_card()
		elif c1.suit==c3.suit and c1.suit==c4.suit:
			if not d1.is_empty(): c1=d1.deal_next_card()
			if not d1.is_empty(): c3=d1.deal_next_card()
			if not d1.is_empty(): c4=d1.deal_next_card()
		elif c2.suit==c3.suit and c2.suit==c4.suit:
			if not d1.is_empty(): c2=d1.deal_next_card()
			if not d1.is_empty(): c3=d1.deal_next_card()
			if not d1.is_empty(): c4=d1.deal_next_card()
		elif c1.suit==c2.suit:
			if not d1.is_empty(): c1=d1.deal_next_card()
			if not d1.is_empty(): c2=d1.deal_next_card()
		elif c1.suit==c3.suit:
			if not d1.is_empty(): c1=d1.deal_next_card()
			if not d1.is_empty(): c3=d1.deal_next_card()
		elif c1.suit==c4.suit:
			if not d1.is_empty(): c1=d1.deal_next_card()
			if not d1.is_empty(): c4=d1.deal_next_card()
		elif c2.suit==c3.suit:
			if not d1.is_empty(): c2=d1.deal_next_card()
			if not d1.is_empty(): c3=d1.deal_next_card()
		elif c2.suit==c4.suit:
			if not d1.is_empty(): c2=d1.deal_next_card()
			if not d1.is_empty(): c4=d1.deal_next_card()
		elif c3.suit==c4.suit:
			if not d1.is_empty(): c3=d1.deal_next_card()
			if not d1.is_empty(): c4=d1.deal_next_card()
		else:
			print("No more moves. You lose.")
			game=False
	
	if d1.is_empty():
		print('',c1,' ',c2,' ',c3,' ',c4,' cards left:',len(d1.cards))
		print("No more cards. You win!")

