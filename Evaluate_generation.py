#NOTE : Alur Kode
#1. Inisialisasi populasi awal
# 2. Hitung fitness semua individu -> done 
# 3. LOOP per generasi:
#    a. Ukur performa generasi sekarang  ← yg gua bikin di sini 
#    b. Seleksi parent
#    c. Crossover
#    d. Mutation
#    e. Bentuk populasi baru
#    f. Hitung fitness populasi baru
# 4. Cek stopping condition

#variabel yg dibutuhin -> populasi, fitness, penalty
# SUMBER OP: https://www.datacamp.com/tutorial/genetic-algorithm-python 

#pseudocode 
#function measurePerformance(population, generation):
    # bestFitness = -infinity
    # totalFitness = 0
    # violatedCount = 0

    # for each individual in population:
    #     totalFitness += individual.fitness

    #     if individual.fitness > bestFitness:
    #         bestFitness = individual.fitness

    #     if individual.penalty > 0:
    #         violatedCount += 1

    # averageFitness = totalFitness / population.size

    # simpan(bestFitness, averageFitness, violatedCount)


# evaluate_generation: hitung performa generasi baru beserta rata-rata kualiatas generasi 
#butuh elitism 
def evaluate_generation(population, board):
    #buat empat variabel untuk menyimpan total fitness, best fitness, avg fitness, dan jumlah violation
    total_fitness = 0
    best_fitness = -1
    avg_fitness = 0
    violation_count = 0

    #lakukan loop untuk tiap individu di populasi saat ini 
    for individual in population:
        #tambahkan tiap fitness dari tiap individu
        fitness_temp = compute_fitness(individual, board) #pake fungsi fitness 
        total_fitness += fitness_temp

        #sekalian bandingin fitness mana yang terbaik dari tiap individu 
        best_fitness = max(fitness_temp, best_fitness)

        #hitung jumlah violation tiap individu 


    #yang mesti diitung: 
    # Best fitness di generasi ini 
    # Avg fitness nya 
    # jumlah pelanggaran constraint  


# count_constraint: hitung pelanggaran terhadap sel yang masih belum terpenuhi 
def count_violation():



#conclusion -> bikin si best fitness pake fungsi def 
# si avg bikinin fungsi def 
#si violation bikin fungsi def juga 