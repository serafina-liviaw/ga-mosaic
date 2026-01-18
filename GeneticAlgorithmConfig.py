"""
GeneticAlgorithmConfig adalah kelas untuk menyimpan semua parameter GA dalam satu object
"""

from dataclasses import dataclass

@dataclass
class GeneticAlgorithmConfig:
    """Configuration untuk Genetic Algorithm"""
    population_size: int
    max_generations: int
    elitism_rate: float
    tournament_size: int
    crossover_rate: float
    mutation_rate: float
