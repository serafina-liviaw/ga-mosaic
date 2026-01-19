from Population import Population
from Puzzle import Puzzle
from GeneticAlgorithmConfig import GeneticAlgorithmConfig
from EvolutionResult import EvolutionResult, GenerationStats

# GeneticAlgorithm adalah kode utama yang mengatur alur algoritma genetik dari inisialisasi populasi awal, parent selection, crossover, hingga pemilihan individu/solusi terbaik
# @author  Nadhira Saffanah Zahra, Serafina Livia Wardhana
# Sumber kode -> Dokumen Mosaic, LLM 
class GeneticAlgorithm: 
    def __init__(self, puzzle: Puzzle, config: GeneticAlgorithmConfig):
        """
        Initialize Genetic Algorithm.
        
        Parameter:
        puzzle (Puzzle): Puzzle object
        config (GeneticAlgorithmConfig): GA configuration
        """
        self.puzzle = puzzle
        self.board = puzzle.board
        self.config = config


    # method untuk mulai menyelesaikan puzzle
    def solve_mosaic(self):
        result = EvolutionResult()
        
        initPop = Population(self.config.population_size, self.config.elitism_rate, self.config.tournament_size, self.config.mutation_rate, self.board, self.config.crossover_rate)

        # generate populasi awal dan lakukan evaluasi fitness
        initPop.generate_population()
        initPop.evaluate_generation()
        
        # Track generation 0
        stat = GenerationStats(
            generation=0,
            best_fitness=initPop.bestFitness,
            avg_fitness=initPop.avgFitness,
            worst_fitness=min(ind.fitness for ind in initPop.individuals),
            best_violation=initPop.individuals[0].violation
        )
        result.generation_stats.append(stat)
        
        # lakukan iterasi sebanyak maxGenCount
        for i in range(self.config.max_generations):
            newPop = Population(self.config.population_size, self.config.elitism_rate, self.config.tournament_size, self.config.mutation_rate, self.board, self.config.crossover_rate)

            # ambil sekian persen individu terbaik untuk next generation
            newPop.doElitism(initPop)
        
            # lakukan crossover
            newPop.doCrossover(initPop)

            # evaluasi generasi baru
            newPop.evaluate_generation()
            
            # Track generation stats
            stat = GenerationStats(
                generation=i + 1,
                best_fitness=newPop.bestFitness,
                avg_fitness=newPop.avgFitness,
                worst_fitness=min(ind.fitness for ind in newPop.individuals),
                best_violation=newPop.individuals[0].violation
            )
            result.generation_stats.append(stat)
            
            initPop = newPop

        # Set result data
        bestIndividual = initPop.individuals[0]
        result.best_individual = bestIndividual
        result.best_fitness = bestIndividual.fitness
        result.is_solved = (bestIndividual.violation == 0)
        
        # Tampilkan best solution
        print("\n" + "="*50)
        print("BEST SOLUTION FOUND")
        print("="*50)
        print(f"Best Fitness: {bestIndividual.fitness:.5f}")
        print(f"Violations: {bestIndividual.violation}")
        print(f"\nBest Solution Grid:")
        self._print_chromosome(bestIndividual.chromosome)
        
        return result
    
    def _print_chromosome(self, chromosome):
        """Print the chromosome in a readable format"""
        for row in chromosome:
            print(''.join(['■' if cell == 1 else '□' for cell in row]))
