def hand_value_check(hole_cards, *board):


	board_list = []

	for card in hole_cards:
		board_list.append(convert_card(card))

	for i in board:
		board_list.append(convert_card(i))


	if len(board_list) == 5: print("You are on the flop")
	elif len(board_list) == 6: print("You are on the turn")
	elif len(board_list) == 7: print("You are on the river")
	else: print("Incorrect number of cards specified.")
	print("your hole cards are ", hole_cards[0], " and ", hole_cards[1])

	board_list.sort(reverse = True)
	board_numbers = []
	board_suit = []
	for card in board_list:
		board_numbers.append(card[0])
		board_suit.append(card[1])
	std_suit = ['S','H','C','D']
	

	straight_flush = False
	straight = False
	four_kind = False
	flush = False
	three_kind = False
	pair_count = 0



	#Check for flush
	u_suit_count = []
	for suit in std_suit:
		count = 0
		for card in board_suit:
			if card == suit:
				count += 1
		u_suit_count.append((suit,count))

	#print("Suits: ", u_suit_count)

	for suit in u_suit_count:
		if suit[1] == 5:
			flush = True




	#Look for a straight	
	consecutive = 0
	consec_list = []

	for x in range(len(board_list)-1):
		if consecutive >= 4:
			straight = True
			continue


		if board_list[x+1][0] == board_list[x][0] - 1:
			consecutive += 1
			if len(consec_list) == 0:
				consec_list.append(board_list[x])
			consec_list.append(board_list[x+1])

		elif len(consec_list) < 5:
			consec_list = []

	print(board_list)
	#print("consecutive numbers ", consecutive)

	if straight and flush:
		straight_flush = True

	if straight:
		print("your straight: ", consec_list)
	else: 
		print("you have no straight")



	#Look for four of a kind
	unique_numbers = []
	u_number_count = []
	
	#set() function returns all the unique elements 
	#in a list as a dictionary. 
	for number in set(board_numbers):
		unique_numbers.append((number))

	print(unique_numbers)

	for u_number in unique_numbers:
		count = 0
		for number in board_list:
			if u_number == number[0]:
				count += 1
		u_number_count.append((u_number, count))


	print("matching cards: ", u_number_count)

	#Now u_numbers_count is populated, search through to
	#check for four of a kind, full house, pair etc.

	for number in u_number_count:
		if number[1] == 4:
			four_kind = True
		if number[1] == 3:
			three_kind = True
		if number[1] == 2:
			pair_count +=1


	if straight_flush:
		print("You have a straight flush")
	elif four_kind:
		print("You have four of a kind")
	elif three_kind and pair_count == 1:
		print("You have full house")
	elif flush:
		print("You have a flush")
	elif three_kind:
		print("You have three of a kind")
	elif pair_count == 2:
		print("You have two pair")
	elif pair_count == 1:
		print("You have a pair")











# Converts cards to a standard 3 char format:
# Eg 6H = 06,H   KC = 13,C
def convert_card(card_value):

	card_value = card_value.upper()

	if card_value[:1] == 'T':
		card_value = '10' + card_value[1:]
	if card_value[:1] == 'J':
		card_value = '11' + card_value[1:]
	if card_value[:1] == 'Q':
		card_value = '12' + card_value[1:]
	if card_value[:1] == 'K':
		card_value = '13' + card_value[1:]
	if card_value[:1] == 'A':
		card_value = '14' + card_value[1:]

	if len(card_value) > 2:
		return int(card_value[:2]), card_value[-1:]
	else:
		return int(card_value[:1]), card_value[-1:]






hand_value_check(('8d', 'Kc'), 'Kd', 'Qc', '7s', '9d', '6s')

