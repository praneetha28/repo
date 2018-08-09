#Exercise : how many
# write a procedure, called how_many, which returns the sum of the number of values associated with a dictionary.


def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    value_list = []
    total = 0
    for value in aDict:
    	value_list = aDict[value]
    	count = len(value_list)
    	total += count
    return total

def main():
	'''enter input'''
	n=input()
	aDict={}
	for i in range(int(n)):
		s=input()
		l=s.split()
		if l[0] not in aDict:
			aDict[l[0][0]]=[l[1]]
		else:
			aDict[l[0][0]].append(l[1])
	print(how_many(aDict))


if __name__== "__main__":
    main()