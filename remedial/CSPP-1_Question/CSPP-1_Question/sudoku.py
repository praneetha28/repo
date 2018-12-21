def sudoku(list1):
	if isFull(list1):
		print("Given sudoku is solved")
	else:
		solveSudoku(list1)

def isFull(li):
		if li.count('.') == 0:
			return True
		else:
			return False

def main():
	input1 = input()
	if len(input1) != 81:
		print("Invalid input")
	# else:
		# matrix = list(Grid(input1))
		# grid = []
		# for i in range(len(matrix)):
		# 	grid.append(list(map(int, matrix[i])))
		# print(grid)
	sudoku(input1)

def Grid(list3):
	for i in range(0, len(list3), 9):
		yield list3[i:i + 9]
	return list3


if __name__ == '__main__':
    main()