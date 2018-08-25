def Tic_Tac_Toe(matrix):
	winner = []
	for row in matrix:
		if row[0] == row[1] == row[2]:
			winner.append(row[0])
	for i in range(0,3):
		if matrix[0][i] == matrix[1][i] == matrix[2][i]:
			winner.append(matrix[0][i])
	if matrix[0][0] == matrix[1][1] == matrix[2][2]:
		winner.append(matrix[0][0])
	if matrix[2][0] == matrix[1][1] == matrix[0][2]:
		winner.append(matrix[0][2])
	if len(winner) == 0:
		print('draw')
		return None
	if len(winner) == 1:
		if winner[0] == 'x' or winner[0] == 'o':
			print(winner[0])
		else:
			print("invalid input")
		return winner[0]
	else:
		print("invalid game")
		return None
def main():
	matrix = []
	for _ in range(0, 3):
		col = input().split(' ')
		matrix.append(col)
	Tic_Tac_Toe(matrix)
if __name__ == '__main__':
   main()