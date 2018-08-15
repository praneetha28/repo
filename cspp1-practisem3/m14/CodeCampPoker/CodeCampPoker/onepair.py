'''global dictionary'''
card_values = {'T':10,'J':11,'Q':12,'K':13,'A':14,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
def one_pair(hand):
	'''one pair'''
	l3 = []
	for h in hand:
		l3.append(card_values[h[0]])
	l3.sort()
	for i in range(0,len(l3)-1):
		if(l3[i]) == (l3[i+1]):
			return True
	return False

def hand_rank(hand):
	'''
		You will code this function. The goal of the function is to
		return a value that max can use to identify the best hand.
		As this function is complex we will progressively develop it.
		The first version should identify if the given hand is a straight
		or a flush or a straight flush.
	'''

	# By now you should have seen the way a card is represented.
	# If you haven't then go the main or poker function and print the hands
	# Each card is coded as a 2 character string. Example Kind of Hearts is KH
	# First character for face value 2,3,4,5,6,7,8,9,T,J,Q,K,A
	# Second character for the suit S (Spade), H (Heart), D (Diamond), C (Clubs)
	# What would be the logic to determine if a hand is a straight or flush?
	# Let's not think about the logic in the hand_rank function
	# Instead break it down into two sub functions is_straight and is_flush

	# check for straight, flush and straight flush
	# best hand of these 3 would be a straight flush with the return value 3
	# the second best would be a flush with the return value 2
	# third would be a straight with the return value 1
	# any other hand would be the fourth best with the return value 0
	# max in poker function uses these return values to select the best hand
	if one_pair(hand):
		return 1
	return 0

def poker(hands):
	'''
		This function is completed for you. Read it to learn the code.

		Input: List of 2 or more poker hands
			   Each poker hand is represented as a list
			   Print the hands to see the hand representation

		Output: Return the winning poker hand
	'''


	# the line below may be new to you
	# max function is provided by python library
	# learn how it works, in particular the key argument, from the link
	# https://www.programiz.com/python-programming/methods/built-in/max
	# hand_rank is a function passed to max
	# hand_rank takes a hand and returns its rank
	# max uses the rank returned by hand_rank and returns the best hand
	return max(hands, key=hand_rank)

if __name__ == "__main__":
	# read the number of test cases
	COUNT = int(input())
	# iterate through the test cases to set up hands list
	HANDS = []
	for x in range(COUNT):
		line = input()
		ha = line.split(" ")
		HANDS.append(ha)
	# test the poker function to see how it works
	print(' '.join(poker(HANDS)))
