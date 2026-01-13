from Individual import Individual

# GeneticAlgorithm adalah kode utama yang mengatur alur algoritma genetik dari inisialisasi populasi awal, parent selection, crossover, hingga pemilihan individu/solusi terbaik
# @author  Nadhira Saffanah Zahra, Serafina Livia Wardhana
# Sumber kode -> Dokumen Mosaic, LLM 
class GeneticAlgorithm: 
    def __init__(self, board, popSize, maxGenCount, elitismRate, crossoverRate, mutationRate):
        # array 2d berisi clue yang diperlukan untuk menyelesaikan puzzle mosaic
        self.board = board

        # jumlah maksimal generasi yang dihasilkan crossover
        self.maxGenCount = maxGenCount

        # probabilitas terjadinya elitism 
        self.elitismRate = elitismRate

        # probabilitas terjadinya crossover
        self.crossoverRate = crossoverRate

        # probabilitas terjadinya mutasi
        self.mutationRate = mutationRate

    # method untuk mulai menyelesaikan puzzle
    def solve_mosaic(self):
        

        self.evaluate_generation(population)
        return solution
    
    # ======= FUNGSI FITNESS =======
    #count black box : hitung jumlah kotak hitam sebenarnya pada papan individual 
    def count_black_box(chromosome, x, y, size):
        count = 0
        
        #masih belom paham 
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < size and 0 <= ny < size:
                    count += chromosome[nx][ny]
        return count
    



 
    
    



