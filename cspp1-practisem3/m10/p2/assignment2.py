'''
Exercise : Assignment-2
implement the function hangman, which takes one parameter - the secretWord 
the user is to guess. This starts up an interactive game of Hangman between 
the user and the computer. Be sure you take advantage of the three helper functions, 
isWordGuessed, getGuessedWord, and getAvailableLetters, 
that you've defined in the previous part.
'''
import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
	"""
	Returns a list of valid words. Words are strings of lowercase letters.
	
	Depending on the size of the word list, this function may
	take a while to finish.
	"""
	print("Loading word list from file...")
	# inFile: file
	inFile = open(WORDLIST_FILENAME, 'r')
	# line: string
	line = inFile.readline()
	# wordlist: list of strings
	wordlist = line.split()
	print("  ", len(wordlist), "words loaded.")
	return wordlist

def chooseWord(wordlist):
	"""
	wordlist (list): list of words (strings)

	Returns a word from wordlist at random
	"""
	return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()
def isWordGuessed(secret_word, letters_guessed):
	'''
	secretWord: string, the word the user is guessing
	lettersGuessed: list, what letters have been guessed so far
	returns: boolean, True if all the letters of secretWord are in lettersGuessed;
	  False otherwise
	'''
	# FILL IN YOUR CODE HERE...
	count = 0
	for char in secret_word:
		if char in letters_guessed:
			count += 1
	if count == len(secret_word):
		return True
	return False

def getGuessedWord(secret_word, letters_guessed):
	'''
	secretWord: string, the word the user is guessing
	lettersGuessed: list, what letters have been guessed so far
	returns: string, comprised of letters and underscores that represents
	  what letters in secretWord have been guessed so far.
	'''
	# FILL IN YOUR CODE HERE...
	s_t = ''
	for char in secret_word:
		if char in letters_guessed:
			s_t = s_t + char
		else:
			s_t = s_t +'_'
	return s_t

def getAvailableLetters(letters_guessed):
	'''
	lettersGuessed: list, what letters have been guessed so far
	returns: string, comprised of letters that represents what letters have not
	  yet been guessed.
	'''
	# FILL IN YOUR CODE HERE...
	import string
	ALPHA = string.ascii_lowercase
	s_t = ''
	for char in ALPHA:
		if char not in letters_guessed:
			s_t = s_t + char
	return s_t

def hangman(secret_word):
	'''
	secretWord: string, the secret word to guess.

	Starts up an interactive game of Hangman.
	Follows the other limitations detailed in the problem write-up.
	'''
	
	intro = str(len(secret_word))
	letters_guessed = []
	guess = str
	mistakes = 8
	wordGuessed = False
	
	print('Welcome to the game, Hangman!')
	print ('I am thinking of a word that is ' + intro + ' letters long.')
	print ('------------')
	while mistakes > 0 and mistakes <= 8 and wordGuessed is False:
		print ('You have ' + str(mistakes) + ' guesses left.')
		print ('Available letters: ' + getAvailableLetters(letters_guessed))
		guess = input('Please guess a letter: ').lower()
		if guess in secret_word:
			if guess in letters_guessed:
				print ("oops! You've already guessed that letter: " + getGuessedWord(secret_word, letters_guessed))
				print ('------')
			else:
				letters_guessed.append(guess)
				print ('correct guess: ' + getGuessedWord(secret_word, letters_guessed))
				print ('------')
		else:
			if guess in letters_guessed:
				print ("oops! You've already guessed that letter: " + getGuessedWord(secret_word, letters_guessed))
				print ('------')
			else:
				letters_guessed.append(guess)
				mistakes -= 1
				print ('oops! That letter is not in my word: ' + getGuessedWord(secret_word, letters_guessed))
				print ('------')
		if secret_word == getGuessedWord(secret_word, letters_guessed):
			wordGuessed = True
	if wordGuessed == True:
		print('Congratulations, you won!')
	elif mistakes == 0:
		print ('Sorry, you ran out of guesses. The word was ' + secret_word)





def main():
	'''
	Main function for the given program
	'''
	#secret_word = chooseWord(wordlist).lower()
	secret_word = chooseWord(wordlist).lower()
	hangman(secret_word)


if __name__ == "__main__":
	main()
