import random

# @author Tya Kanaya
# Sumber kode -> Dokumen Mosaic, LLM
class Mutation:
    def __init__(self, mutationRate: float, base_mutation_rate: float = 0.01):
        """
        Inisialisasi operator mutasi.

        Parameter:
        mutationRate (float): Probabilitas mutasi global (biasanya dari GeneticAlgorithm).
        base_mutation_rate (float): Tingkat mutasi dasar untuk perhitungan adaptif.
        """
        self.mutationRate = mutationRate
        # base_mutation_rate digunakan sebagai dasar penghitungan tingkat mutasi adaptif
        self.base_mutation_rate = base_mutation_rate

    def adaptive(self, offspring, parent1, parent2):
        """
        Melakukan mutasi adaptif pada offspring berdasarkan kemiripan parent.
        
        Tingkat mutasi diadaptasi berdasarkan jarak Hamming antara kedua parent.
        Jika parent sangat berbeda, tingkat mutasi lebih rendah, dan sebaliknya.
        
        Parameter:
        offspring (list of list): Grid offspring yang akan dimutasi
        parent1 (list of list): Grid parent pertama
        parent2 (list of list): Grid parent kedua
        
        Returns:
        list of list: Offspring yang telah dimutasi
        """
        
        n = len(parent1)    # Ukuran grid
        distance = 0        # Jarak Hamming (jumlah perbedaan bit) antara parent
        total_bits = n * n  # Total bit pada grid
        
        # Hitung jarak Hamming antara parent1 dan parent2
        # Dengan membandingkan setiap elemen pada posisi yang sama
        for i in range(n):
            for j in range(n):
                if parent1[i][j] != parent2[i][j]:
                    distance += 1
        
        # Hitung tingkat mutasi adaptif
        # Rumus: mutation_rate = base_rate * (1 - distance/total_bits)
        # Semakin besar jarak (parent lebih berbeda) -> mutation_rate lebih kecil
        # Semakin kecil jarak (parent lebih mirip) -> mutation_rate lebih besar
        mutation_rate = self.base_mutation_rate * (1 - distance / total_bits)
        
        # Terapkan mutasi pada setiap bit di offspring
        for i in range(n):
            for j in range(n):
                # Putuskan secara acak apakah bit ini akan dimutasi
                if random.random() < mutation_rate * self.mutationRate:
                    # Lakukan flip bit (untuk nilai biner 0 atau 1)
                    # 0 menjadi 1, 1 menjadi 0
                    offspring[i][j] = 1 - offspring[i][j]
        
        return offspring