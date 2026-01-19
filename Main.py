from GeneticAlgorithm import GeneticAlgorithm
from Puzzle import Puzzle
from GeneticAlgorithmConfig import GeneticAlgorithmConfig
import time
import random
import sys
import io

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
    SEED = 42
    random.seed(SEED)
    print("Seed yang digunakan:", SEED)

    # baca file input - bisa diganti-ganti sesuai file yang ingin di-solve puzzlenya
    input_file = "easy10x10.txt"

    # set nama file output -> result_input file
    output_file = f"result_{input_file}"

    # Redirect output ke file dengan UTF-8 encoding
    original_stdout = sys.stdout
    original_stderr = sys.stderr

    # Redirect output ke file
    original_stdout = sys.stdout

    # masukkan hasil ke file output
    with open(output_file, 'w', encoding='utf-8') as f:
        # Set stdout dengan UTF-8 wrapper
        sys.stdout = io.TextIOWrapper(f.buffer, encoding='utf-8', line_buffering=True)
        sys.stderr = sys.stdout

        print("=" * 50)
        print("MOSAIC GA SOLVER - EXPERIMENT RESULTS")
        print("=" * 50)
        print(f"Input file: {input_file}")
        print(f"Seed: {SEED}")
        print("=" * 50)

        try:
            cases = read_board_from_file(input_file)
            print(f"Total test case: {len(cases)}")

            # Print parameter GA sekali aja di awal (sama untuk semua test case)
            if cases:
                _, _, popSize, maxGenCount, elitismRate, tournamentSize, crossoverRate, mutationRate = cases[0]
                print(f"\nGA Parameters:")
                print(f"  Population Size   : {popSize}")
                print(f"  Max Generations   : {maxGenCount}")
                print(f"  Elitism Rate      : {elitismRate}")
                print(f"  Tournament Size   : {tournamentSize}")
                print(f"  Crossover Rate    : {crossoverRate}")
                print(f"  Mutation Rate     : {mutationRate}")

            # buat variabel untuk menyimpan papan yang berhasil ter-solve
            solved_count = 0
            times = []

            # lakukan looping untuk tiap test case yang diinput
            for idx, case in enumerate(cases):
                print(f"\n{'='*50}")
                print(f"Test Case #{idx + 1}")
                print(f"{'='*50}")

            size, board, popSize, maxGenCount, elitismRate, tournamentSize, crossoverRate, mutationRate = case

            # panggil fungsi genetic serta memasukkan parameter
            algo = GeneticAlgorithm(board, popSize, maxGenCount, elitismRate, tournamentSize, crossoverRate, mutationRate)

            # simpan untuk menghitung waktu run
            start = time.time()

            # simpan hasil akhir run
            final_population = algo.solve_mosaic()

            # simpan untuk menghitung waktu run
            end = time.time()

            # simpan waktu total run
            elapsed = end - start
            times.append(elapsed)

            print(f"Time : {elapsed:.4f} detik")

            # Cek apakah solved berdasarkan best individual
            best_individual = final_population.individuals[0]
            if best_individual.violation == 0:
                print("Status: SOLVED")
                solved_count += 1
            else:
                print(f"Status: FAILED")

            # print summary dari seluruh test case
            print(f"\n{'=' * 50}")
            print("SUMMARY")
            print(f"{'=' * 50}")
            print(f"Total case  : {len(cases)}")
            print(f"Solved      : {solved_count}")
            print(f"Failed      : {len(cases) - solved_count}")
            print(f"Success rate: {solved_count / len(cases) * 100:.2f}%")
            print(f"Total time  : {sum(times):.4f} detik")
            print(f"Avg time    : {sum(times) / len(times):.4f} detik")
            print(f"Min time    : {min(times):.4f} detik")
            print(f"Max time    : {max(times):.4f} detik")
            print(f"{'=' * 50}")

        except FileNotFoundError:
            print(f"error: file '{input_file}' tidak ditemukan!")
            print("pastikan file ada di direktori yang sama dengan Main.py")

        except Exception as e:
            print(f"error: {e}")
            import traceback
            traceback.print_exc()

    # Restore stdout
    sys.stdout = original_stdout
    sys.stderr = original_stderr

    # Print ke console bahwa file sudah dibuat
    print(f"Results saved to: {output_file}")

if __name__ == "__main__":
    main()