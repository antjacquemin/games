class MNKGame:

    def __init__(self, length, height, nbPieces):
        self.m = length
        self.n = height
        self.k = nbPieces

    def drawBoard(self):
        print(" ---" * self.m)
        for i in range(self.n):
            print("|", end="")
            print("   |" * self.m)
            print(" ---" * self.m)

class TicTacToe(MNKGame):
    
    def __init__(self):
        super().__init__(3, 3, 3)
        self.grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    # Implementation d'une liste de liste avant de faire sur grille
    def checkGrid(self):
        for i in range(3):
            row = set(self.grid[i])
            if len(row) == 1 and self.grid[i][0]:
                return self.grid[i][0]
        for i in range(0,3):
            column = set([self.grid[0][i], self.grid[1][i], self.grid[2][i]])
            if len(column) == 1 and self.grid[0][i]:
                return self.grid[0][i]
        diag1 = set([self.grid[0][0], self.grid[1][1], self.grid[2][2]])
        diag2 = set([self.grid[0][2], self.grid[1][1], self.grid[2][0]])
        if (len(diag1) == 1 or len(diag2) == 1) and self.grid[1][1]:
            return self.grid[1][1]
        return 0

tic = TicTacToe()
tic.drawBoard()

winner_is_2 = [[2, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]
winner_is_1 = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]

winner_is_also_1 = [[0, 1, 0],
	[2, 1, 0],
	[2, 1, 1]]

no_winner = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 2]]

also_no_winner = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 0]]

tic.grid = winner_is_2
print(tic.checkGrid())
tic.grid = winner_is_1
print(tic.checkGrid())
tic.grid = winner_is_also_1
print(tic.checkGrid())
tic.grid = no_winner
print(tic.checkGrid())
tic.grid = also_no_winner
print(tic.checkGrid())