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

    def elitism(self, population, fitness_func=None, elitism_count=None):
        """
        Melakukan seleksi dengan strategi elitism.

        elitism_count individu terbaik (fitness tertinggi) dari generasi n akan langsung
        disalin ke generasi n+1 tanpa melalui mutasi atau crossover.
        Penggunaan strategi ini memastikan bahwa kualitas solusi terbaik
        yang telah ditemukan tidak hilang antar generasi, sekaligus menjaga keragaman populasi.

        Parameter:
        population (list): List individu dalam populasi
        fitness_func (function | None): Fungsi untuk menghitung fitness individu. 
                                        Jika None, diasumsikan tiap individu
                                        memiliki atribut 'fitness'.
        elitism_count (int | None): Jumlah individu elit yang dipertahankan.
                                    Jika None, memakai nilai default dari instance.

        Returns:
        list: Individu-individu terpilih untuk menjadi parent generasi berikutnya
        """ 

        # gunakan nilai default dari instance jika parameter tidak diberikan
        if elitism_count is None:
            elitism_count = self.elitism_count

        # fungsi untuk mendapatkan fitness individu
        if fitness_func is None:
            fitness_func = lambda ind: ind.fitness

        # Hitung fitness untuk semua individu
        fitness_scores = [(individual, fitness_func(individual)) for individual in population]

        # Urutkan berdasarkan fitness (tertinggi ke terendah)
        fitness_scores.sort(key=lambda x: x[1], reverse=True)

        # Ambil elitism_count individu terbaik
        elites = [individual for individual, _ in fitness_scores[:elitism_count]]

        return elites

    def tournament_selection(self, population, fitness_func, tournament_size=None):
        """
        Melakukan seleksi parent menggunakan metode tournament selection.

        Parameter:
        population (list): List individu dalam populasi
        fitness_func (function): Fungsi untuk menghitung fitness individu.
        tournament_size (int | None): Ukuran tournament.
                                      Jika None, memakai nilai default dari instance.

        Returns:
        list: Individu-individu terpilih sebagai parent
        """

        if tournament_size is None:
            tournament_size = self.tournament_size

        selected = []
        for _ in range(len(population)):
            # Pilih kandidat secara acak untuk tournament
            tournament = random.sample(population, min(tournament_size, len(population)))
            # Pilih yang terbaik dari tournament
            best = max(tournament, key=fitness_func)
            selected.append(best)
        return selected