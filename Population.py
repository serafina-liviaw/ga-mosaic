from Individual import Individual
import random

# Populatipn adalah kumpulan individual/kumpulan kandidat solusi
# @author  Nadhira Saffanah Zahra, Serafina Livia Wardhana
class Population:
    def __init__(self, popSize, elitismRate, mutationRate, board):
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

        # variabel untuk menyimpan probabilitas pemilihan individu terbaik
        self.elitismRate = elitismRate

        # variabel untuk m
        self.mutationRate = mutationRate

        # print("initialize pop...")

    # method untuk memulai generasi populasi awal
    def generate_population(self):
        print("generating pop...")
        for i in range(self.popSize):
            individual = Individual(self.board)
            individual.generate_chromosome_1stStrat()
            self.individuals.append(individual)

    # ======= FUNGSI EVALUATE GENERASI ========
    def evaluate_generation(self):
        print("\nevaluate pop...")
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

            # sekalian bandingin fitness mana yang terbaik dari tiap individu 
            self.bestFitness = max(fitnessTemp, self.bestFitness)

        self.avgFitness = totalFitness/self.popSize

        # urutkan individuals juga berdasarkan fitness
        self.individuals.sort(key=lambda x: x.fitness, reverse=True)

        for i, ind in enumerate(self.individuals):
            print(f"[{i}]: fitness={ind.fitness:.5f}")

    # method mengambil sekian persen individu terbaik dari populasi saat ini (sementara gini, nanti mungkin dimodif tea)
    # @param parentPop  populasi pada generasi sebelum
    def doElitism(self, parentPop):
        # print("pick elites...")
        nElite = int(len(parentPop.individuals) * parentPop.elitismRate) # jumlah individual elite
        self.individuals = parentPop.individuals[:nElite]
        
        print("\nelites:")
        for i, ind in enumerate(self.individuals):
            print(f"[{i}]: fitness={ind.fitness:.5f}")
       
    # method untuk melakukan terhadap individu yang belum terpilih elitism (exploration) untuk mengisi sisa slot next gen 
    # @param parentPop  populasi pada generasi sebelum
    def doCrossover(self, parentPop): # hasil cross langsung ditambahin ke self.inidividuals aja te
        print("\nstart crossover...")
        self.parentLog = []  # Track parent yang dipakai
        
        # while len(self.individuals) < self.popSize: <<nanti diganti ini yeaa
        for i in range(6): 
            parent1 = self.selectNonElite(parentPop)
            parent2 = self.selectNonElite(parentPop)
            
            # Track parent
            self.parentLog.append((parent1, parent2))
        

    # NANTI APUS vvv
    # ini ak bikin dua parent selection (mungkin bisa buat eksperimen)
    # pertimbangannya kalo seleksi dilakukan thd semua individu kaya di doc, ada kemungkinan dia inbreeding (local max?)
    # misal
    # waktu elitism individu a kepilih, trus dimasukin ke next gen
    # waktu crossover individu a kawin sm b, trus dimasukin ke next gen
    # di next gen ada kemungkinan individu a kawin sama anaknya sendiri
    # sebenernya tergantung crossRate, elitismRate, ukuran populasi juga si, sm mau lebih eksplor/eksploit
    # contoh inbreeding gapapa: kalo elitism rate kecil & ukuran populasi besar (& mutationRate gedean)


    # method untuk melakukan pemilihan individu dari suatu populasi (binary tournament select)
    # dilakukan terhadap **semua individu** pada populasi parent
    # @param parentPop  populasi pada generasi sebelum
    def select(self, parentPop):
        # print("select parent...")
        # ukuran tournament
        tournamentSize = parentPop.popSize

        # pilih angka random pertama
        currIdx = random.randint(0, parentPop.popSize-1)
        # print(f"individuals length: {len(self.individuals)}")
        # print(f"current idx: {currIdx}")

        currIndividual = parentPop.individuals[currIdx]
        # print(f"first candidate selected: {currIdx}")
        
        for i in range(tournamentSize):
            # pilih angka random kedua
            oppIdx = random.randint(0, parentPop.popSize-1)
            # ulang pemilihan sampai index yang terpilih berbeda
            while oppIdx == currIdx:
                oppIdx = random.randint(0, parentPop.popSize-1)
            oppIndividual = parentPop.individuals[oppIdx]

            # update currIndividual dengan oppIdx individual jika fitness oppIdx lebih besar
            if(currIndividual.fitness < oppIndividual.fitness):
                currIndividual = oppIndividual

        # print(f"second candidate selected: {oppIdx}")
        # print("return selected")
        return currIndividual
    
    # method untuk melakukan pemilihan individu dari suatu populasi (binary tournament select)
    # dilakukan terhadap **individu yang belum terpilih saat elitism** pada populasi parent
    # @param parentPop  populasi pada generasi sebelum
    def selectNonElite(self, parentPop):
        # jumlah elites
        # juga merupakan start index saat pemilihan angka random
        nElite = int(len(parentPop.individuals) * parentPop.elitismRate) 

        # ukuran tournament: ukurang populasi - jumlah elites
        tournamentSize = parentPop.popSize - nElite

        # pilih angka random pertama
        currIdx = random.randint(nElite, parentPop.popSize-1)
        currIndividual = parentPop.individuals[currIdx]

        for i in range(tournamentSize):
            # pilih angka random kedua
            oppIdx = random.randint(nElite, parentPop.popSize-1)
            # ulang pemilihan sampai index yang terpilih berbeda
            while oppIdx == currIdx:
                oppIdx = random.randint(nElite, parentPop.popSize-1)
            oppIndividual = parentPop.individuals[oppIdx]

            # update currIndividual dengan oppIdx individual jika fitness oppIdx lebih besar
            if(currIndividual.fitness < oppIndividual.fitness):
                currIndividual = oppIndividual

        # print("return selected parent")
        return currIndividual

