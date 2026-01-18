"""
Kelas untuk menyimpan hasil evolusi + statistik setiap generasi. 
"""

from dataclasses import dataclass
from typing import List, Optional

@dataclass
class GenerationStats:
    """Statistik untuk satu generasi"""
    generation: int
    best_fitness: float
    avg_fitness: float
    worst_fitness: float
    best_violation: int


class EvolutionResult:
    """Container untuk hasil evolusi"""
    
    def __init__(self):
        self.best_individual = None
        self.best_fitness = -1
        self.generation_stats: List[GenerationStats] = []
        self.total_generations = 0
        self.execution_time = 0.0
        self.is_solved = False
