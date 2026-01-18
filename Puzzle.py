"""
Merepresentasikan papan puzzle mosaic sebagai sebuah object. 
"""

class Puzzle:
    def __init__(self, board, size):
        """
        Inisialisasi Puzzle.
        
        Parameter:
        board (list of list): Array 2D berisi clue puzzle
        size (int): Ukuran papan (size x size)
        """
        self.size = size
        self.board = board
