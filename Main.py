from GeneticAlgorithm import GeneticAlgorithm
from Puzzle import Puzzle
from GeneticAlgorithmConfig import GeneticAlgorithmConfig
import time
import random

# baca file txt dan parse board puzzle mosaic + parameter GA
def read_board_from_file(filename):
    with open(filename, 'r') as file:
        lines = [line.strip() for line in file.readlines()]

    # Hapus empty lines tapi keep track index
    lines = [line for line in lines if line]

    i = 0

    # baca parameter
    ga_params = lines[i].split()
    popSize = int(ga_params[0])
    maxGenCount = int(ga_params[1])
    elitismRate = float(ga_params[2])
    tournamentSize = int(ga_params[3])
    crossoverRate = float(ga_params[4])
    mutationRate = float(ga_params[5])
    i += 1

    # baca size papan
    size = int(lines[i])
    i += 1

    # buat variabel untuk menyimpan tiap test case
    cases = []

    # lakukan loop sebanyak n papan
    while i < len(lines):
        # buat variabel untuk menyimpan tiap isi papan
        board = []

        # lakukan loop sebesar size papan
        for j in range(size):

            # cek apakah masih ada input
            if i >= len(lines):
                break
            elements = lines[i].split()
            i += 1

            row = []
            for elem in elements:
                if elem.lower() == 'x':
                    row.append(-1)
                else:
                    row.append(int(elem))
            board.append(row)

        # buat mastiin kalau board sesuai sama size papan di awal
        if len(board) == size:
            cases.append((size, board, popSize, maxGenCount, elitismRate, tournamentSize, crossoverRate, mutationRate))

    # return tiap test case
    return cases

# # konversi kromosom jadi string untuk print menjadi output
# def chromosome_to_string(chromosome, size):
#     result = []
#     for i in range(size):
#         row = []
#         for j in range(size):
#             # 1 = sel hitam, 0 = sel putih
#             row.append('■' if chromosome[i][j] == 1 else '□')
#         result.append(' '.join(row))

#     return '\n'.join(result)

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
    # tentukan seed yang digunakan
    # bisa diganti-ganti
    SEED = 1231
    random.seed(SEED)
    print("Seed yang digunakan:", SEED)

    # baca file input
    input_file = "puzzle.txt"
    cases = read_board_from_file(input_file)
    print(f"Total test case: {len(cases)}")

    # buat variabel untuk menyimpan papan yang berhasil ter-solve
    solved_count = 0
    times = []

    try:
        # lakukan looping untuk tiap test case yang diinput
        for idx, case in enumerate(cases):
            print(f"\n==============================")
            print(f"Test Case #{idx + 1}")
            print(f"==============================")

            size, board, popSize, maxGenCount, elitismRate, tournamentSize, crossoverRate, mutationRate = case

            # Create Puzzle dan Config objects
            puzzle = Puzzle(board, size)
            config = GeneticAlgorithmConfig(
                population_size=popSize,
                max_generations=maxGenCount,
                elitism_rate=elitismRate,
                tournament_size=tournamentSize,
                crossover_rate=crossoverRate,
                mutation_rate=mutationRate
            )
            
            # panggil fungsi genetic serta memasukkan parameter
            algo = GeneticAlgorithm(puzzle, config)

            # simpan untuk menghitung waktu run
            start = time.time()

            # simpan hasil akhir run
            evolution_result = algo.solve_mosaic()

            # simpan untuk menghitung waktu run
            end = time.time()

            # simpan waktu total run
            elapsed = end - start
            times.append(elapsed)
            evolution_result.execution_time = elapsed

            print(f"Time : {elapsed:.4f} detik")

            # Cek apakah solved berdasarkan best individual
            if evolution_result.is_solved:
                print("Status: SOLVED")
                solved_count += 1
            else:
                print(f"Status: FAILED")

        # print summary dari seluruh test case
        print(f"\n==============================")
        print(f"SUMMARY")
        print(f"==============================")
        print(f"Total case  : {len(cases)}")
        print(f"Solved      : {solved_count}")
        print(f"Success rate: {solved_count / len(cases) * 100:.2f}%")
        print(f"Total time  : {sum(times):.4f} detik")
        print(f"Avg time    : {sum(times) / len(times):.4f} detik")
        print(f"Min time    : {min(times):.4f} detik")
        print(f"Max time    : {max(times):.4f} detik")

    except FileNotFoundError:
        print(f"error: file '{input_file}' tidak ditemukan!")
        print("pastikan file ada di direktori yang sama dengan Main.py")

    except Exception as e:
        print(f"error: {e}")

if __name__ == "__main__":
    main()