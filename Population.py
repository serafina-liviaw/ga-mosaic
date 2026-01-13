from Individual import Individual

# Populatipn adalah kumpulan individual/kumpulan kandidat solusi
# @author  Nadhira Saffanah Zahra, Serafina Livia Wardhana
class Population:
    def __init__(self, size):
        # jumlah individu dalam satu populasi
        self.size = size

        # array individu-individu dalam suatu populasi
        self.individuals = []

    def generatePopulation(self, board):
        for i in range(self.size):
            self.individuals.add(Individual(len(board)).generate_chromosome(board))

    # ======= FUNGSI EVALUATE GENERASI ========
    def evaluate_generation(self):
        # buat empat variabel untuk menyimpan total fitness, best fitness, avg fitness, dan jumlah violation
        total_fitness = 0
        best_fitness = -1
        avg_fitness = 0
        # NOTE: violation_count = 0 dipindah ke individual

        # lakukan loop untuk tiap individu di populasi saat ini 
        for individual in self.individuals:
            # kalkulasi fitness menggunakan fungsi compute_fitness pada Individu
            # ketika memanggi compute_fitness, penalti dan jumlah violation juga akan dikalkulasi
            fitness_temp =  individual.compute_fitness() 
            total_fitness += fitness_temp

            #sekalian bandingin fitness mana yang terbaik dari tiap individu 
            best_fitness = max(fitness_temp, best_fitness)


        # hitung average fitness dari populasi 
        avg_fitness = total_fitness/self.size

        return best_fitness, avg_fitness

    