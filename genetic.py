import numpy
import numpy as np
from numpy import random


class Genetic:
    def __init__(self, function, start, end, alpha=0.2, n_first_population=10, n_cross_over_rate=0.4,
                 n_mutation_rate=0.2, iteration=100, minima=True):
        self.function = function
        self.start = start
        self.end = end
        self.alpha = alpha
        self.number_of_first_population = n_first_population
        self.number_of_cross_over = int(n_first_population * n_cross_over_rate)
        self.number_of_mutation = int(n_first_population * n_mutation_rate)
        self.iteration = iteration
        self.minima = minima
        self.crossover_resource = []
        self.resource = []

    def generation(self):
        for _ in range(self.number_of_first_population):
            chromosome = tuple(random.uniform(self.start, self.end, 2))
            self.resource.append(chromosome)

    def cross_over(self):
        for _ in range(self.number_of_cross_over):
            index1 = random.randint(0, self.number_of_first_population)
            parent1 = self.resource[index1]
            index2 = random.randint(0, self.number_of_first_population)
            parent2 = self.resource[index2]

            child1 = (parent1[0] * self.alpha + parent2[0] * (1 - self.alpha),
                      parent1[1] * self.alpha + parent2[1] * (1 - self.alpha))
            child2 = (parent2[0] * self.alpha + parent1[0] * (1 - self.alpha),
                      parent2[1] * self.alpha + parent1[1] * (1 - self.alpha))

            self.crossover_resource.append(child1)
            self.crossover_resource.append(child2)

            self.resource.append(child1)
            self.resource.append(child2)

    def mutation(self):
        for _ in range(self.number_of_mutation):
            index = random.randint(0, len(self.crossover_resource))
            old_chromosome = list(self.crossover_resource[index])
            i = random.randint(0, 2)
            new_value = random.uniform(self.start, self.end)
            old_chromosome[i] = new_value
            new_chromosome = tuple(old_chromosome)

            self.resource.append(new_chromosome)

    def evaluation(self):
        result = {}
        for chromosome in self.resource:
            X1 = chromosome[0]
            X2 = chromosome[1]
            output = eval(self.function)
            result[output] = chromosome

        self.resource.clear()
        if self.minima:
            sorted_result = sorted(result.items())
        elif not self.minima:
            sorted_result = sorted(result.items(), reverse=True)
        for i in range(self.number_of_first_population):
            chromosome = sorted_result[i][1]
            self.resource.append(chromosome)

    def calculation(self):
        self.generation()
        for i in range(self.iteration):
            self.cross_over()
            self.mutation()
            self.evaluation()

        X1 = self.resource[0][0]
        X2 = self.resource[0][1]
        output = eval(self.function)

        return X1, X2, output


def calculate(function, start, end, n_first_population, n_cross_over_rate, n_mutation_rate, iteration, alpha, minima):
    gen = Genetic(function=function, start=int(start), end=int(end), minima=minima,
                  n_first_population=int(n_first_population), n_cross_over_rate=n_cross_over_rate,
                  n_mutation_rate=n_mutation_rate, iteration=int(iteration), alpha=alpha)
    X_1, X_2, y = gen.calculation()
    return X_1, X_2, y