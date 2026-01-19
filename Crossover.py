import random
import copy

# @author Tya Kanaya
# Sumber kode -> Dokumen Mosaic, LLM
class Crossover:

    # Inisialisasi operator crossover.
    def __init__(self, crossoverRate: float, block_size: int = 3, swap_prob: float = 0.5):
          
        self.crossoverRate = crossoverRate  # Probabilitas terjadinya crossover
        self.block_size = block_size        # Ukuran sisi blok yang akan dipertukarkan
        self.swap_prob = swap_prob          # Probabilitas pertukaran setiap blok

    # Melakukan crossover antara dua parent dengan metode pertukaran blok-uniform / region-based.
    # @param parent1: Grid parent pertama (matriks 2D)
    # @param parent2: Grid parent kedua (matriks 2D)
    def blokUniform(self, parent1, parent2): 

        n = len(parent1)  # Ukuran grid (n x n) 

        # Membuat salinan mendalam dari parent sebagai awal offspring
        # Deep copy diperlukan karena list 2d
        offspring1 = copy.deepcopy(parent1)
        offspring2 = copy.deepcopy(parent2)
        
        # Hitung jumlah blok pada setiap dimensi
        num_blocks = n // self.block_size

        # Iterasi melalui setiap blok pada grid
        for i in range(num_blocks):
            for j in range(num_blocks):
                # Putuskan secara acak apakah blok ini akan ditukar
                if random.random() < self.swap_prob:
                    # Swap the block
                    for bi in range(self.block_size):
                        for bj in range(self.block_size):
                            # Hitung koordinat sebenarnya pada grid
                            x = i * self.block_size + bi     # Baris pada grid
                            y = j * self.block_size + bj     # Kolom pada grid

                            # Tukar nilai antara kedua offspring
                            offspring1[x][y], offspring2[x][y] = offspring2[x][y], offspring1[x][y]
        
        return offspring1, offspring2