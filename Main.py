from GeneticAlgorithm import GeneticAlgorithm

# baca file txt dan parse board puzzle mosaic + parameter GA
def read_board_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    # baca ukuran papan dari baris pertama
    size = int(lines[0].strip())
    
    # baca board dari baris berikutnya
    board = []
    for i in range(1, size + 1):
        row = []
        elements = lines[i].strip().split()
        
        for elem in elements:
            if elem.lower() == 'x':
                # 'x' melambangkan sel kosong (tidak ada clue)
                row.append(-1)
            else:
                # angka melambangkan clue
                row.append(int(elem))
        
        board.append(row)
    
    # baca parameter GA dari baris setelah board
    ga_params_line = lines[size + 1].strip().split()
    popSize = int(ga_params_line[0])
    maxGenCount = int(ga_params_line[1])
    elitismRate = float(ga_params_line[2])
    crossoverRate = float(ga_params_line[3])
    mutationRate = float(ga_params_line[4])
    
    return size, board, popSize, maxGenCount, elitismRate, crossoverRate, mutationRate

# konversi kromosom jadi string untuk print menjadi output
def chromosome_to_string(chromosome, size):
    result = []
    for i in range(size):
        row = []
        for j in range(size):
            # 1 = sel hitam, 0 = sel putih
            row.append(str(chromosome[i][j]))
        result.append(' '.join(row))

    return '\n'.join(result)

# print papan permainan (belum diwarnai)
def print_board(board, size, label="board"):
    print(f"\n{label}:")
    for i in range(size):
        row = []
        for j in range(size):
            if board[i][j] == -1:
                row.append('x')
            else:
                row.append(str(board[i][j]))
        print(' '.join(row))

def main():
    # baca file input
    input_file = "puzzle.txt"
    
    try:
        size, board, popSize, maxGenCount, elitismRate, crossoverRate, mutationRate = read_board_from_file(input_file)
        print(f"ukuran papan: {size}x{size}")
        print_board(board, size, "puzzle input")

        # inisialisasi genetic algorithm dengan parameter
        algo = GeneticAlgorithm(board, popSize, maxGenCount, elitismRate, crossoverRate, mutationRate)
        
        print("======== START solver ============")
        algo.solve_mosaic()
        
    
    except FileNotFoundError:
        print(f"error: file '{input_file}' tidak ditemukan!")
        print("pastikan file 'puzzle.txt' ada di direktori yang sama dengan Main.py")
    except Exception as e:
        print(f"error: {e}")

if __name__ == "__main__":
    main()
