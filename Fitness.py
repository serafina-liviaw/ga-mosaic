import math

#Sumber kode -> Dokumen Mosaic, LLM 

# count black box : hitung jumlah kotak hitam sebenarnya pada papan individual 
def count_black_box(chromosome, x, y, size):
    count = 0
    
    #masih belom paham 
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < size and 0 <= ny < size:
                count += chromosome[nx][ny]
    return count

# fitness function: hitung penalti dari solusi individual   
def compute_fitness(individual, board):
    penalty = 0
    fitness = 0
    size = individual.size()

    # Lakukan loop untuk baris dan kolom individual 
    for i in range(size):
        for j in range(size): 
            # jika pada sel tidak ada clue, skip
            if board[i][j] == -1:
                continue

            # ambil nilai jumlah kotak hitam seharusnya 
            expected_black_box = board[i][j]

            # ambil jumlah kotak hitam sebenarnya pada papan individual
            actual_black_box = count_black_box(individual.chromosome, i, j, size)

            # hitung penalti berdasarkan selisih antara expected dan actual 
            penalty += abs(expected_black_box - actual_black_box)

    # hitung fitness 
    fitness = 1 / (1 + penalty)
    return fitness



