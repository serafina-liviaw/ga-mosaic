from Individual import Individual

# Populatipn adalah kumpulan individual/kumpulan kandidat solusi
# @author  Nadhira Saffanah Zahra, Serafina Livia Wardhana
class Population:
    def __init__(self, popSize, board):
        # jumlah individu dalam satu populasi
        self.popSize = popSize

        # papan permainan yang berisi clue
        self.board = board

        # array individu-individu dalam suatu populasi
        self.individuals = []

        # variabel untuk menyimpan fitness terbaik
        self.bestFitness = -1

        # variabel untuk menyimpan rata-rata fitness
        self.avgFitness = 0

    def generate_population(self):
        for i in range(self.popSize):
            individual = Individual(self.board)
            individual.generate_chromosome_1stStrat()
            self.individuals.append(individual)

    # ======= FUNGSI EVALUATE GENERASI ========
    def evaluate_generation(self):
        # buat empat variabel untuk menyimpan total fitness, best fitness, avg fitness, dan jumlah violation
        totalFitness = 0
        self.bestFitness = -1
        self.avgFitness = 0

        # lakukan loop untuk tiap individu di populasi saat ini 
        for individual in self.individuals:
            # kalkulasi fitness menggunakan fungsi compute_fitness pada Individu
            # ketika memanggi compute_fitness, penalti dan jumlah violation juga akan dikalkulasi
            fitnessTemp =  individual.compute_fitness() 
            totalFitness += fitnessTemp

            #sekalian bandingin fitness mana yang terbaik dari tiap individu 
            self.bestFitness = max(fitnessTemp, self.bestFitness)

        self.avgFitness = totalFitness/self.popSize

    