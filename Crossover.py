import random
import copy

# @author Tya Kanaya
# Sumber kode -> Dokumen Mosaic, LLM
class Crossover:

    def blokUniform(parent1, parent2, block_size=3, swap_prob=0.5):
        """
        Melakukan crossover antara dua parent dengan metode pertukaran blok-uniform / region-based.
        
        Fungsi ini membagi grid menjadi blok-blok berukuran tertentu, kemudian
        memutuskan secara acak apakah akan menukar setiap blok antara kedua parent.
        
        Parameter:
        parent1 (list of list): Grid parent pertama (matriks 2D)
        parent2 (list of list): Grid parent kedua (matriks 2D)
        block_size (int): Ukuran sisi blok yang akan dipertukarkan (default: 3)
        swap_prob (float): Probabilitas pertukaran setiap blok (0.0-1.0, default: 0.5)
        
        Returns:
        tuple: Dua offspring hasil crossover (offspring1, offspring2)
        """

        n = len(parent1) # Ukuran grid (n x n) 

        # Membuat salinan mendalam dari parent sebagai awal offspring
        # Deep copy diperlukan karena list 2d
        offspring1 = copy.deepcopy(parent1)
        offspring2 = copy.deepcopy(parent2)
        
        # Hitung jumlah blok pada setiap dimensi
        num_blocks = n // block_size

        # Iterasi melalui setiap blok pada grid
        for i in range(num_blocks):
            for j in range(num_blocks):
                # Putuskan secara acak apakah blok ini akan ditukar
                if random.random() < swap_prob:
                    # Swap the block
                    for bi in range(block_size):
                        for bj in range(block_size):
                            # Hitung koordinat sebenarnya pada grid
                            x = i * block_size + bi     # Baris pada grid
                            y = j * block_size + bj     # Kolom pada grid

                            # Tukar nilai antara kedua offspring
                            offspring1[x][y], offspring2[x][y] = offspring2[x][y], offspring1[x][y]
        
        return offspring1, offspring2