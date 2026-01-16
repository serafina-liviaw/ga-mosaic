from Population import Population

# GeneticAlgorithm adalah kode utama yang mengatur alur algoritma genetik dari inisialisasi populasi awal, parent selection, crossover, hingga pemilihan individu/solusi terbaik
# @author  Nadhira Saffanah Zahra, Serafina Livia Wardhana
# Sumber kode -> Dokumen Mosaic, LLM 
class GeneticAlgorithm: 
    def __init__(self, board, popSize, maxGenCount, elitismRate, tournamentSize, crossoverRate, mutationRate):
        # array 2d berisi clue yang diperlukan untuk menyelesaikan puzzle mosaic
        self.board = board

        self.popSize = popSize

        # jumlah maksimal generasi yang digenerate
        self.maxGenCount = maxGenCount

        # probabilitas terjadinya elitism 
        self.elitismRate = elitismRate

        # ukuran turnamen pada seleksi
        self.tournamentSize = tournamentSize

        # probabilitas terjadinya crossover
        self.crossoverRate = crossoverRate

        # probabilitas terjadinya mutasi
        self.mutationRate = mutationRate


    # method untuk mulai menyelesaikan puzzle
    def solve_mosaic(self):
        initPop = Population(self.popSize, self.elitismRate, self.tournamentSize, self.mutationRate, self.board, self.crossoverRate)

        # generate populasi awal dan lakukan evaluasi fitness
        initPop.generate_population()
        print(f"\n=== Generation 0 ===")
        initPop.evaluate_generation()
        print(f"\nBest Fitness: {initPop.bestFitness:.5f}")
        print(f"Avg Fitness: {initPop.avgFitness:.5f}")
        
        # lakukan iterasi sebanyak maxGenCount
        for i in range(self.maxGenCount):
            newPop = Population(self.popSize, self.elitismRate, self.tournamentSize, self.mutationRate, self.board, self.crossoverRate)

            # ambil sekian persen individu terbaik untuk next generation
            newPop.doElitism(initPop)
        
            # lakukan crossover
            newPop.doCrossover(initPop)

            # ringkasan crossover beberapa parent pertama
            print(f"\nParent Selection (first 3):")
            for j, (p1, p2) in enumerate(newPop.parentLog[:3]):
                print(f"  Crossover {j+1}: Parent1 fitness={p1.fitness:.5f}, Parent2 fitness={p2.fitness:.5f}")

            # evaluasi generasi baru
            print(f"\n=== Generation {i + 1} ===")
            newPop.evaluate_generation()
            print(f"Best Fitness: {newPop.bestFitness:.5f}")
            print(f"Avg Fitness: {newPop.avgFitness:.5f}")

            
            initPop = newPop

        # Tampilkan best solution
        print("\n" + "="*50)
        print("BEST SOLUTION FOUND")
        print("="*50)
        bestIndividual = initPop.individuals[0]
        print(f"Best Fitness: {bestIndividual.fitness:.5f}")
        print(f"Violations: {bestIndividual.violation}")
        print(f"\nBest Solution Grid:")
        self._print_chromosome(bestIndividual.chromosome)
        
        return initPop
    
    def _print_chromosome(self, chromosome):
        """Print the chromosome in a readable format"""
        for row in chromosome:
            print(''.join(['■' if cell == 1 else '□' for cell in row]))
    



 
    
    



