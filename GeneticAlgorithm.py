from Population import Population

# GeneticAlgorithm adalah kode utama yang mengatur alur algoritma genetik dari inisialisasi populasi awal, parent selection, crossover, hingga pemilihan individu/solusi terbaik
# @author  Nadhira Saffanah Zahra, Serafina Livia Wardhana
# Sumber kode -> Dokumen Mosaic, LLM 
class GeneticAlgorithm: 
    def __init__(self, board, popSize, maxGenCount, elitismRate, crossoverRate, mutationRate):
        # array 2d berisi clue yang diperlukan untuk menyelesaikan puzzle mosaic
        self.board = board

        self.popSize = popSize

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
        initPop = Population(self.popSize, self.board)

        initPop.generate_population()
        initPop.evaluate_generation()

        return initPop
    



 
    
    



