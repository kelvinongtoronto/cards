from card import Card
from deck import Deck
from sys import argv

games = ["Highest Hand", "Lowest Hand", "Small to Big", "Royal Family", "Four Kings"]

if len(argv) == 2:
	game_mode = argv[1]
else:
	#print("usage: "+argv[0]+" game_mode")
	#print("game_mode = ")
	print("Select Game Mode:")
	for i in range(0,5):
		print('\t',i, games[i])
	game_mode = input()

d1=Deck('A','K')
if game_mode == '4':
	for i in range(0,3):
		for suit in Deck.SUITS:
			d1.cards.append(Card(suit,'K'))
d1.shuffle()

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

player=[c0,c1,c2,c3]
opponent=[e0,e1,e2,e3]

game_on = True

def players_turn():
	print("Your Hand: 0:"+str(player[0])+" 1:"+str(player[1])+" 2:"+str(player[2])+" 3:"+str(player[3]))
	discard = input("Select Card to Discard or 's' to show hand:")
	while not (len(discard)==1 and discard in ['0','1','2','3','s']):
		discard = input("Select Card to Discard or 's' to show hand: ")
	if discard=='s':
		show_hands()
	else:
		new_card = d1.get_next_card()
		new_card.turn_over()
		player[int(discard)] = new_card

def highest_card(): # playing Lowest Hand
	if calc_score(opponent) <= 10:
		print("I'm ready to show my hand!")
		show_hands()
	else:
		highest = 0
		for i in [1,2,3]:
			if opponent[i] > opponent[highest]:
				highest = i
		opponent[highest] = d1.get_next_card()
		print("I replace card "+str(highest)+".")

def lowest_card(): # playing Highest Hand
	if calc_score(opponent) >= 30:
		print("I'm ready to show my hand!")
		show_hands()
	else:
		lowest = 0
		for i in [1,2,3]:
			if opponent[i] < opponent[lowest]:
				lowest = i
		opponent[lowest] = d1.get_next_card()
		print("I replace card "+str(lowest)+".")

def out_of_order(): # playing Small to Big
	if in_order(opponent):
		print("I'm ready to show my hand!")
		show_hands()
	else:
		discard = 0
		threshold = [Card('','7'),Card('','9'),Card('','J'),Card('','K')]
		for c in [0,1,2,3]:
			if opponent[c] > threshold[c]:
				discard = c
				break
			else:
				if c != 0 and opponent[c] < opponent[c-1]:
					discard = c
					break
		opponent[discard] = d1.get_next_card()
		print("I replace card "+str(discard)+".")

def not_royal(): # playing Royal Family
	discard = -1
	for i in [0,1,2,3]:
		if not (opponent[i].rank in ['J','Q','K']):
			discard = i
			break
	if discard == -1:
		print("I'm ready to show my hand!")
		show_hands()
	else:
		opponent[discard] = d1.get_next_card()
		print("I replace card "+str(discard)+".")

def not_king(): # playing Four Kings
	discard = -1
	for i in [0,1,2,3]:
		if opponent[i].rank != 'K':
			discard = i
			break
	if discard == -1:
		print("I'm ready to show my hand!")
		show_hands()
	else:
		opponent[discard] = d1.get_next_card()
		print("I replace card "+str(discard)+".")

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
		elif (c.rank == 'J' or c.rank == 'Q') and game_mode == '3':
			cards += 1
	return cards
	
def show_hands():
	if game_mode == '0' or game_mode == '1':
		opponent_value = calc_score(opponent)
		player_value = calc_score(player)
	elif game_mode == '3' or game_mode == '4':
		opponent_value = count_cards(opponent)
		player_value = count_cards(player)
	else:
		opponent_value = in_order(opponent)
		player_value = in_order(player)
	
	for e in opponent:
		e.turn_over()
	
	print()
	
	print("My Hand: 0:"+str(opponent[0])+" 1:"+str(opponent[1])+" 2:"+str(opponent[2])+" 3:"+str(opponent[3]))
	if game_mode == '0' or game_mode == '1':
		print("My hand equals: %d." % (opponent_value))
	elif game_mode == '3':
		print ("I have %d court card%s." % (opponent_value, "" if opponent_value==1 else "s"))
	elif game_mode == '4':
		print ("I have %d king%s." % (opponent_value, "" if opponent_value==1 else "s"))
	else:
		print ("My hand is %sin order" % ("" if opponent_value else "not "))
	
	print()
	
	print("Your Hand: 0:"+str(player[0])+" 1:"+str(player[1])+" 2:"+str(player[2])+" 3:"+str(player[3]))
	if game_mode == '0' or game_mode == '1':
		print("Your hand equals: %d." % (player_value))
	elif game_mode == '3':
		print ("You have %d court card%s." % (player_value, "" if player_value==1 else "s"))
	elif game_mode == '4':
		print ("You have %d king%s." % (player_value, "" if player_value==1 else "s"))
	else:
		print ("Your hand is %sin order" % ("" if player_value else "not "))
	
	print()
	
	if game_mode == '0':
		if player_value > opponent_value:
			print("You win!")
		elif player_value < opponent_value:
			print("I win!")
		else:
			print("It's a draw! We both win!")
	elif game_mode == '1':
		if player_value < opponent_value:
			print("You win!")
		elif player_value > opponent_value:
			print("I win!")
		else:
			print("It's a draw! We both win!")
	elif game_mode == '2':
		if player_value and opponent_value:
			print("It's a draw! We both win!")
		elif player_value:
			print("You win!")
		elif opponent_value:
			print("I win!")
		else:
			print("It's a draw! We both lose.")
	elif game_mode == '3' or game_mode == '4':
		if player_value == 4 and opponent_value == 4:
			print("It's a draw! We both win!")
		elif player_value == 4:
			print("You win!")
		elif opponent_value == 4:
			print("I win!")
		else:
			print("It's a draw! We both lose.")
	
	#game_on = False
	exit(0)

print("Playing %s." % (games[int(game_mode)]))
	
while game_on:
	print("\nNow it's your turn!")
	players_turn()
# 	if not game_on:
# 		break
	print("\nNow it's my turn!")
	if game_mode == '0':
		lowest_card()
	elif game_mode == '1':
		highest_card()
	elif game_mode == '2':
		out_of_order()
	elif game_mode == '3':
		not_royal()
	elif game_mode == '4':
		not_king()
# 	if not game_on:
# 		break
