import math

# Class ini digunakan untuk mengevaluasi fitness dari solusi individual
# @author  Nadhira Saffanah Zahra
#Sumber kode -> Dokumen Mosaic, LLM 
class Fitness:
    def __init__(self, board):
        # ukuran papan game mosaic
        self.size = len(board)

        # papan permainan yang berisi clue
        self.board = board


    # fungsi untuk menghitung penalti dari solusi individual
    def compute_fitness(self, individual):
        fitness = 0
        penalty, violation = self.count_penalty_violation(individual)

        # hitung fitness 
        fitness = 1 / (1 + penalty)
        return fitness, penalty, violation

    # fungsi untuk menghitung penalty pada setiap individu 
    def count_penalty_violation(self, individual):
        penalty = 0 
        violation = 0
        size = individual.size

        # lakukan loop untuk mengecek setiap kotak pada baris dan kolom individual 
        for i in range(size):
            for j in range(size): 
                # jika pada sel tidak ada clue, skip
                if self.board[i][j] == -1:
                    continue

                # ambil nilai jumlah kotak hitam seharusnya 
                expected_black_box = self.board[i][j]

                # ambil jumlah kotak hitam sebenarnya pada papan individual
                actual_black_box = self.count_black_box(individual.chromosome, i, j)

                # hitung penalti berdasarkan selisih antara expected dan actual 
                penalty += abs(expected_black_box - actual_black_box)

                # hitung jumlah pelanggaran terhadap aturan game pada tiap individu 
                if expected_black_box != actual_black_box: 
                    violation += 1
        return penalty, violation
    
    # count_black_box : hitung jumlah kotak hitam sebenarnya pada papan individual 
    def count_black_box(self, chromosome, x, y):
        count = 0

        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.size and 0 <= ny < self.size:
                    count += chromosome[nx][ny]
        return count


  
