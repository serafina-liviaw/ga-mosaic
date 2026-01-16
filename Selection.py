# @author Tya Kanaya
# Sumber kode -> Dokumen Mosaic, https://www.baeldung.com/cs/elitism-evolutionary-algorithms, LLM
import random

class Selection:
    def __init__(self, elitismRate: float, elitism_count: int = 2, tournament_size: int = 3):
        """
        Inisialisasi operator seleksi.

        Parameter:
        elitismRate (float): Probabilitas atau proporsi penggunaan elitism (biasanya dari GeneticAlgorithm).
        elitism_count (int): Jumlah individu elit yang dipertahankan.
        tournament_size (int): Ukuran tournament untuk tournament selection.
        """
        self.elitismRate = elitismRate
        self.elitism_count = elitism_count
        self.tournament_size = tournament_size

    def elitism(self, population, fitness_func=None):
        """
        Melakukan seleksi dengan strategi elitism.

        Individu terbaik (fitness tertinggi) dari generasi n akan langsung
        disalin ke generasi n+1 tanpa melalui mutasi atau crossover.
        Penggunaan strategi ini memastikan bahwa kualitas solusi terbaik
        yang telah ditemukan tidak hilang antar generasi, sekaligus menjaga keragaman populasi.

        Parameter:
        population (list): List individu dalam populasi
        fitness_func (function | None): Fungsi untuk menghitung fitness individu. 
                                        Jika None, diasumsikan tiap individu
                                        memiliki atribut 'fitness'.

        Returns:
        list: Individu-individu terpilih untuk menjadi parent generasi berikutnya
        """ 

        # fungsi untuk mendapatkan fitness individu
        if fitness_func is None:
            fitness_func = lambda ind: ind.fitness

        # Hitung fitness untuk semua individu
        fitness_scores = [(individual, fitness_func(individual)) for individual in population]

        # Urutkan berdasarkan fitness (tertinggi ke terendah)
        fitness_scores.sort(key=lambda x: x[1], reverse=True)

        # Ambil individu terbaik sesuai elitism_count
        elites = [individual for individual, _ in fitness_scores[:self.elitism_count]]

        return elites

    def tournament_selection(self, population, fitness_func):
        """
        Melakukan seleksi parent menggunakan metode tournament selection.

        Parameter:
        population (list): List individu dalam populasi
        fitness_func (function): Fungsi untuk menghitung fitness individu.

        Returns:
        list: Individu-individu terpilih sebagai parent
        """

        selected = []
        for _ in range(len(population)):
            # Pilih kandidat secara acak untuk tournament
            tournament = random.sample(population, min(self.tournament_size, len(population)))
            # Pilih yang terbaik dari tournament
            best = max(tournament, key=fitness_func)
            selected.append(best)
        return selected