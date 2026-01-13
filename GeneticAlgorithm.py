class GeneticAlgorithm: 
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
    
    #fungsi untuk menghitung penalty pada setiap individu 
    def count_penalty(individual, board):
        penalty = 0 
        size = individual.size

        #lakukan loop untuk baris dan kolom individual 
        for i in range(size):
            for j in range(size): 
                #jika pada sel tidak ada clue, skip
                if board[i][j] == -1:
                    continue

                #ambil nilai jumlah kotak hitam seharusnya 
                expected_black_box = board[i][j]

                #ambil jumlah kotak hitam sebenarnya pada papan individual
                actual_black_box = GeneticAlgorithm.count_black_box(individual.chromosome, i, j, size)

                #hitung penalti berdasarkan selisih antara expected dan actual 
                penalty += abs(expected_black_box - actual_black_box)

        return penalty 


    #fitness function: hitung penalti dari solusi individual   
    def compute_fitness(individual, board):
        fitness = 0
        penalty = GeneticAlgorithm.count_penalty(individual, board)

        #hitung fitness 
        fitness = 1 / (1 + penalty)
        return fitness
    
    
    # ======= FUNGSI EVALUATE GENERASI ========
    def evaluate_generation(population, board):
        #buat empat variabel untuk menyimpan total fitness, best fitness, avg fitness, dan jumlah violation
        total_fitness = 0
        best_fitness = -1
        avg_fitness = 0
        violation_count = 0

        #lakukan loop untuk tiap individu di populasi saat ini 
        for individual in population:
            #tambahkan tiap fitness dari tiap individu
            fitness_temp =  GeneticAlgorithm.compute_fitness(individual, board) #pake fungsi fitness 
            total_fitness += fitness_temp

            #sekalian bandingin fitness mana yang terbaik dari tiap individu 
            best_fitness = max(fitness_temp, best_fitness)

            #hitung jumlah violation tiap individu 
            violation_count = GeneticAlgorithm.count_violation(individual, board)

        #hitung average fitness dari populasi 
        avg_fitness = total_fitness/len(population)

        return best_fitness, avg_fitness, violation_count

    # count_constraint: hitung pelanggaran terhadap sel yang masih belum terpenuhi 
    def count_violation(individual, board):
        #set variabel violation untuk menyimpan jumlah violation individu 
        violation = 0
        size = individual.size

        #lakukan looping untuk mengecek tiap kotak apakah melanggar atau tidak 
        for i in range(size):
            for j in range(size):
                #jika pada sel tidak ada clue, skip
                if board[i][j] == -1:
                    continue

                #ambil nilai jumlah kotak hitam seharusnya 
                expected_black_box = board[i][j]

                #ambil jumlah kotak hitam sebenarnya pada papan individual
                actual_black_box = GeneticAlgorithm.count_black_box(individual.chromosome, i, j, size)

                #cek apakah terjadi violasi -> untuk ngecek berapa banyak kesalahan yang ada pada indidual (agar tidak terjebak di local maximum)
                if expected_black_box != actual_black_box: 
                    violation += 1

        return violation
                

