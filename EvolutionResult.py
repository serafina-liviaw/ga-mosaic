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
    
    def export_stats_to_file(self, filename):
        """Export statistik generasi ke file teks"""
        with open(filename, 'w') as f:
            f.write("Generation Statistics\n")
            f.write("="*80 + "\n")
            f.write(f"{'Gen':<6} {'Best Fitness':<15} {'Avg Fitness':<15} {'Worst Fitness':<15} {'Violation':<10}\n")
            f.write("-"*80 + "\n")
            
            for stat in self.generation_stats:
                f.write(f"{stat.generation:<6} {stat.best_fitness:<15.5f} {stat.avg_fitness:<15.5f} {stat.worst_fitness:<15.5f} {stat.best_violation:<10}\n")
