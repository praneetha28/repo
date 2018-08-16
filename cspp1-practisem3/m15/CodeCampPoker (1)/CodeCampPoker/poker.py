'''
    Write a program to evaluate poker hands and determine the winner
    Read about poker hands here.
    https://en.wikipedia.org/wiki/List_of_poker_hands
'''
CARD_VALUES = {'T':10, 'J':11, 'Q':12, 'K':13, 'A':14, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}

def is_straight(hand):
    '''
        How do we find out if the given hand is a straight?
        The hand has a list of cards represented as strings.
        There are multiple ways of checking if the hand is a straight.
        Do we need both the characters in the string? No.
        The first character is good enough to determine a straight
        Think of an algorithm: given the card face value how to check if it a straight
        Write the code for it and return True if it is a straight else return False
    '''
    list1 = []
    for i in hand:
        list1.append(CARD_VALUES[i[0]])
    list1.sort()
    for i in range(0, len(list1)-1):
        if list1[i+1] - list1[i] != 1:
            return False
    return True



def is_flush(hand):
    '''
        How do we find out if the given hand is a flush?
        The hand has a list of cards represented as strings.
        Do we need both the characters in the string? No.
        The second character is good enough to determine a flush
        Think of an algorithm: given the card suite how to check if it is a flush
        Write the code for it and return True if it is a flush else return False
    '''
    temp = hand[0]
    i = 0
    for i in hand:
        if temp[1] != i[1]:
            return False
    return True

def four_of_a_kind(hand):
    '''four of a kind'''
    l_i = []
    for i in hand:
        l_i.append(CARD_VALUES[i[0]])
    l_i.sort()
    for i in range(0, len(l_i)-3):
        if l_i[i] == l_i[i+1] == l_i[i+2] == l_i[i+3]:
            return True
    return False

def three_of_a_kind(hand):
    '''three of kind'''
    l_1 = []
    for i in hand:
        l_1.append(CARD_VALUES[i[0]])
    l_1.sort()
    for i in range(0, len(l_1)-2):
        if l_1[i] == l_1[i+1] == l_1[i+2]:
            return True
    return False

def two_pair(hand):
    '''two pairs'''
    l_2 = []
    for i in hand:
        l_2.append(CARD_VALUES[i[0]])
    l_2.sort()
    for i in range(0, len(l_2)-3):
        if l_2[i] == l_2[i+1] and l_2[i+2] == l_2[i+3]:
            return True
    return False

def one_pair(hand):
    '''one pair'''
    l_3 = []
    for i in hand:
        l_3.append(CARD_VALUES[i[0]])
    l_3.sort()
    for i in range(0, len(l_3)-1):
        if(l_3[i]) == (l_3[i+1]):
            return True
    return False
def full_house(hand):
    '''only one pair'''
    l_4 = []
    for i in hand:
        l_4.append(CARD_VALUES[i[0]])
    l_4.sort()
    for i in range(0, len(l_4)-1):
        if l_4[i] == l_4[i+1] == l_4[i+2] and l_4[i+3] == l_4[i+4]:
            return True
    return False

def high_card(hand):
    '''high card'''
    l_5 = []
    for i in hand:
        l_5.append(CARD_VALUES[i[0]])
    l = max(l_5)
    d[l] = hand
    return max(d.keys())


def hand_rank(hand):
    '''
        You will code this function. The goal of the function is to
        return a value that max can use to identify the best hand.
        As this function is complex we will progressively develop it.
        The first version should identify if the given hand is a straight
        or a flush or a straight flush.
    '''
    if is_straight(hand) and is_flush(hand):
        return 9
    elif four_of_a_kind(hand):
        return 8
    elif three_of_a_kind(hand) and one_pair(hand):
        return 7
    elif is_flush(hand):
        return 6
    elif is_straight(hand):
        return 5
    elif three_of_a_kind(hand):
        return 4
    elif two_pair(hand):
        return 3
    elif one_pair(hand):
        return 2
    elif hand_rank(hand):
        return 1
    else:
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
