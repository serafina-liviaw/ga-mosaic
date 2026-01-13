# @author Tya Kanaya
# Sumber kode -> Dokumen Mosaic, https://www.baeldung.com/cs/elitism-evolutionary-algorithms, LLM
import random

class Selection:

    def elitism(population, fitness_func=None, elitism_count=2):
        """
        Melakukan seleksi dengan strategi elitism.

        2 dari individu terbaik (fitness tertinggi) dari generasi n akan langsung
        disalin ke generasi n+1 tanpa melalui mutasi atau crossover.
        Penggunaan strategi ini memastikan bahwa kualitas solusi terbaik
        yang telah ditemukan tidak hilang antar generasi, sekaligus menjaga keragaman populasi.

        Parameter:
        population (list): List individu dalam populasi
        fitness_func (function): Fungsi untuk menghitung fitness individu. 
        elitism_count (int): Jumlah individu elit yang dipertahankan (default: 2) 

        Returns:
        list: Individu-individu terpilih untuk menjadi parent generasi berikutnya
        """ 

        # Hitung fitness untuk semua individu
        fitness_scores = [(individual, fitness_func(individual)) for individual in population]

        # Urutkan berdasarkan fitness (tertinggi ke terendah)
        fitness_scores.sort(key=lambda x: x[1], reverse=True)

        # Ambil elitism_count individu terbaik
        elites = [individual for individual, _ in fitness_scores[:elitism_count]]

        return elites

    def tournament_selection(population, fitness_func, tournament_size=3):
        """
        Melakukan seleksi parent menggunakan metode tournament selection.

        Parameter:
        population (list): List individu dalam populasi
        fitness_func (function): Fungsi untuk menghitung fitness individu.
        tournament_size (int): Ukuran tournament (default: 3)

        Returns:
        list: Individu-individu terpilih sebagai parent
        """
        selected = []
        for _ in range(len(population)):
            # Pilih kandidat secara acak untuk tournament
            tournament = random.sample(population, min(tournament_size, len(population)))
            # Pilih yang terbaik dari tournament
            best = max(tournament, key=fitness_func)
            selected.append(best)
        return selected