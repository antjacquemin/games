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

tic = TicTacToe()
tic.drawBoard()
