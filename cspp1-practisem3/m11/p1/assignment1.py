'''
Exercise: Assignment-1
The first step is to implement some code that allows us to calculate the score for a single word. The function get_word_score should accept as input a string of lowercase letters (a word) and return the integer score for that word, using the game's scoring rules.
'''

def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1,
    'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1,
    's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10}
    sum  = 0
    re_s = 0
    for letters in word:
        if letters in SCRABBLE_LETTER_VALUES:
            sum = sum + SCRABBLE_LETTER_VALUES[letters]
    re_s = sum * len(word)
    if n == len(word):
        return re_s + 50
    return re_s  


def main():
    '''
    Main function for the given problem
    '''
    data = input()
    data = data.split()
    print(get_word_score(data[0], int(data[1])))


if __name__ == "__main__":
    main()
