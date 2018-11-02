import sys

def hand_value_check(hole_cards, *board):

	board_list = hole_cards + board

	print(board_list)

	#Exception handling to catch repeats. 
	#set removes all duplicates, list length then compared.
	if len(board_list) != len(set(board_list)):
		raise_value_error("You have repeated cards")
	if len(board_list) < 5 or len(board_list) > 7:
		raise_value_error("Too many/few cards, between \
			5 and 7, including hole cards in brackets.")
	for card in board_list:
		if len(card) != 2:
			raise_value_error("Card format is two \
characters per card eg for six of hearts\
use 6h (from ten onwards use letters: Th, Kd")
		elif not card[1:].isalpha():
			raise_value_error("incorrect format: one charcter\
				for rand and one letter for suit, eg 8s")
		elif not (card[1:].upper() == 'S' or card[1:].upper() == 'H'\
			or card[1:].upper() == 'C' or card[1:].upper() == 'D'):
			raise_value_error("cannot identify suit")





	#print(board_list)

	board_list = convert_card(board_list)

	board_list.sort(reverse = True)

	if len(board_list) == 5: print("You are on the flop")
	elif len(board_list) == 6: print("You are on the turn")
	elif len(board_list) == 7: print("You are on the river")
	else: print("Incorrect number of cards specified.")
	#print("your hole cards are ", hole_cards[0], " and ", hole_cards[1])
	print("Complete list (ordered): ", board_list)

	
	board_numbers = []
	board_suit = []
	for card in board_list:
		board_numbers.append(card[0])
		board_suit.append(card[1])
	std_suit = ['S','H','C','D']
	
	best_hand = []
	straight_flush, s_flush_hand = False, []
	straight, straight_hand = False, []
	four_kind, f_kind_hand = False, []
	full_house, f_house_hand = False, []
	flush, flush_hand = False, []
	three_kind_count, three_kind_hand = 0, []
	two_pair, two_pair_hand = False, []
	pair_count, pair_hand = 0, []

	#Check for flush
	u_suit_count = []
	flush_suit = ''
	for suit in std_suit:
		count = 0
		for card in board_suit:
			if card == suit:
				count += 1
		u_suit_count.append((suit,count))

	#print("unique suits: ", u_suit_count)

	#print("Suits: ", u_suit_count)

	for suit in u_suit_count:
		if suit[1] >= 5:
			flush = True
			flush_suit = suit[0]

	#print("your flush suit", flush_suit)

	for card in board_list:
		if card[1] == flush_suit:
			flush_hand.append(card)
		if len(flush_hand) == 5:
			continue





	#Look for a straight	
	consecutive = 0
	

	for x in range(len(board_list)-1):
		#if consecutive >= 4:
		#	straight = True
		#	continue


		if board_list[x+1][0] == board_list[x][0] - 1:
			consecutive += 1
			if len(straight_hand) == 0:
				straight_hand.append(board_list[x])
			straight_hand.append(board_list[x+1])

			#need to check if it's most efficient to put
			#this block here instead of above original place
			if consecutive >= 4:
				straight = True
				continue		

		#As long as there is one break in the 
		#consec count, reset to 0
		else:
			consecutive = 0

	if len(straight_hand) < 5:
		straight_hand = []

	#cover the case where Ace is low card
	#first check if ace exists
	ace_list = [card for card in board_list if card[0] ==14]
	if not straight and ace_list:
		#take the smallest 4 cards and check if == 2,3,4,5
		smallest_4 = board_list[-4:]
		match = 0

		for index in range(4):
			if smallest_4[index][0] + index == 5:
				match += 1

		if match == 4:
			straight = True
			#build the straight hand
			#since we know ace already exists and it will
			#always be the 0th element
			straight_hand = smallest_4
			straight_hand.append(board_list[0])

			print("your straight_hand = ", straight_hand)








	#Check if your straight is a straight-flush
	if straight:
		same_suit = 0
		for card in straight_hand:
			if card[1] == straight_hand[0][1]:
				same_suit += 1
		if same_suit == 5:
			straight_flush = True
			s_flush_hand = straight_hand







	#Look for four of a kind
	unique_numbers = []
	u_number_count = []
	
	#set() function returns all the unique elements 
	#in a list as a dictionary. 
	for number in set(board_numbers):
		unique_numbers.append((number))

	#print(unique_numbers)

	for u_number in unique_numbers:
		count = 0
		for number in board_list:
			if u_number == number[0]:
				count += 1
		u_number_count.append((u_number, count))

	#Now u_numbers_count is populated, search through to
	#check for four of a kind, full house, pair etc.
	three_kind_rank = 0
	for number in u_number_count:
		if number[1] == 4:
			four_kind = True
			f_kind_rank = number[0]
		if number[1] == 3:
			three_kind_count += 1
		if number[1] == 2:
			pair_count += 1

		if three_kind_count and pair_count or three_kind_count == 2: 
			full_house = True
			for numb2 in u_number_count:
				if numb2[1] == 3:
					three_kind_rank = numb2[0] 



		elif three_kind_count == 2:
			full_house = True

			print("hello u_number_count = ", u_number_count)
			#you have two 3 of a kind, find which
			#one is bigger
			for number in u_number_count:
				if number[1] == 3 and number[0] > three_kind_rank:
					three_kind_rank = number[0]
			#now the smaller three kind will be used as a 
			#pair in the full house
			for index, number in enumerate(u_number_count):
				if number[1] == 3 and number[0] != three_kind_rank:
					u_number_count[index] = (number[0],2)

		elif pair_count > 1:
			two_pair = True


	


	#Build the strongest 5 card hand
	temp_board = []
	if four_kind:
		for card in board_list:
			if card[0] == f_kind_rank:
				f_kind_hand.append(card)
			else:
				temp_board.append(card)
		f_kind_hand.append(max(temp_board))

	elif full_house:
		#find the highest pair
		largest_pair = 0
		for num in u_number_count:
			if num[1] == 2 and num[0] > largest_pair:
				largest_pair = num[0]

		#print("three kind rank = ", three_kind_rank)
		#build the hand
		for card in board_list:
			if card[0] == three_kind_rank: 
				f_house_hand.append(card)

		#need to separate to above in situation where you have 
		#2x three of a kind, one of those is treated as a pair.
		count = 0
		for card in board_list:
			if count == 2:
				continue
			elif card[0] == largest_pair:
				f_house_hand.append(card)
				count += 1
	elif three_kind_count > 0:
		three_kind_rank = [card for card in u_number_count if card[1] == 3][0][0]
		for card in board_list:
			
			
			if card[0] == three_kind_rank:
				three_kind_hand.append(card)
		for card in board_list:
			if card[0] != three_kind_rank and len(three_kind_hand) < 5:
				three_kind_hand.append(card)
	elif two_pair:
		u_number_count.sort(reverse=True)

		for numb3 in u_number_count:
			if numb3[1] == 2:
				for card in board_list:
					if card[0] == numb3[0]:
						two_pair_hand.append(card)
						if len(two_pair_hand) == 4:
							continue
		#now we have a result with two pairs for four cards,
		#next step just append the largest remaining card that isn't
		#already used in a pair
		for card in board_list:
			z_rank, z_suit = zip(*two_pair_hand)
			if card[0] not in z_rank:
				two_pair_hand.append(card)
				break

	elif pair_count:
		pair_rank = 0
		for numb3 in u_number_count:
			if numb3[1] == 2:
				pair_rank = numb3[0]
				for card in board_list:
					if numb3[0] == card[0]:
						pair_hand.append(card)

		
		
		assert (len(pair_hand) == 2), "Issue pending pair to pair_hand"

		#board list with the pair removed
		re_board_list = [i for i in board_list if i[0] != pair_rank]

		pair_hand += re_board_list[:3]

					

	

	if straight_flush:
		print("You have a straight flush", conv_to_rank_suit(s_flush_hand))
	elif four_kind:
		print("You have four of a kind",conv_to_rank_suit(f_kind_hand))
	elif full_house:
		print("You have full house", conv_to_rank_suit(f_house_hand))
	elif flush:
		print("You have a flush", conv_to_rank_suit(flush_hand))
	elif straight:
		print("You have a straight: ", conv_to_rank_suit(straight_hand))
	elif three_kind_count:
		print("You have three of a kind", conv_to_rank_suit(three_kind_hand))
	elif two_pair:
		print("You have two pair", conv_to_rank_suit(two_pair_hand))
	elif pair_count == 1:
		print("You have a pair", conv_to_rank_suit(pair_hand))

















# Converts cards to a standard 3 char format:
# Eg 6H = 06,H   KC = 13,C
def convert_card(card_list):

	result = []

	for card_value in card_list:

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
			result.append((int(card_value[:2]), card_value[-1:]))
		else:
			result.append((int(card_value[:1]), card_value[-1:]))

	return result

def conv_to_rank_suit(card_list):
	result = []

	for card in card_list:

		if card[0] == 14:
			result.append('A' + card[1].lower())
		elif card[0] == 13:
			result.append('K' + card[1].lower())
		elif card[0] == 12:
			result.append('Q' + card[1].lower())
		elif card[0] == 11:
			result.append('J' + card[1].lower())
		elif card[0] == 10:
			result.append('T' + card[1].lower())
		else:
			result.append(str(card[0]) + card[1].lower())

	return result

def raise_value_error(message):
	try:
		raise ValueError(message)
	except Exception as error:
		print(repr(error))
	sys.exit()



#hand_value_check(('Ah', '2d'), 'Ad', 'Tc', 'As', 'Ac', '8d')
hand_value_check(('Ad', '2s'), '7h', '5h', 'Ac', '3d', '9d')
