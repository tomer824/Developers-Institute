# import random
# from random import randint

# randBool = bool(random.getrandbits(1))
# randValue = randint(0, 1)

# class Gene:
#     def __init__(self, value, mutate):
#         self.value = value
#         self.mutate =  mutate

#     def mutation(self):
#         if self.mutate == True:
#             new_value = self.value
#             if new_value == 1:
#                 return new_value - 1
#             else:
#                 return new_value + 1
#         else:
#             return self.value

# class Chromosome:
#     def __init__(self, geneValue, geneMutate, geneMutation):
#         self.geneValue = geneValue
#         self.geneMutate = geneMutate
#         self.geneMutation = geneMutation
#         self.geneList = [self.geneValue, self.geneMutate, self.geneMutation]
#         print(self.geneList)

# class Gene_Mutation_Multiply(self):
#     def __init__(self):
#         self.gene_mutation_multiply = []
#         for i in range(10):
#             self.gene_mutation_multiple = gene.mutation()
#         print(gene_mutation_multiply)
#         return gene_mutation_multiply

# gene = Gene(randValue, randBool)
# print(gene.value)
# print(gene.mutate)
# print(gene.mutation())

# gene = Gene(randValue, randBool)
# print(gene.value)
# print(gene.mutate)
# print(gene.mutation())
# chrom = Chromosome(gene.value, gene.mutate, gene.mutation())

import random

class Gene():
    def __init__(self):
        self.value = random.choice([True, False])
    
    def mutate(self):
       self.value = not self.value
    
    def __repr__(self):
        return "1" if self.value else "0"
    
    def __str__(self):
        return f"I'm a gene with value {self.__repr__}"

class Chromosome():
    def __init__(self):
        self.value = [Gene() for i in range(10)]
    
    def mutate(self):
       for gene in self.value:
           if random.choice([True, False]):
               gene.mutate()
    
    def __repr__(self):
        return str(self.value)

class DNA():
    def __init__(self):
        self.value = [Chromosome() for i in range(10)]
    
    def mutate(self):
        for chromosome in self.value:
            if random.choice([True, False]):
                chromosome.mutate()

class Organism():
    def __init__(self, dna, probabilitiy_to_mutate):
        self.dna = dna
        self.probability_to_mutate = probability_to_mutate
    
    def mutate(self):
        mutate_number = random.random()
        if random.random() <= probability to mutate:
            self.dna.mutate()

    def __repr__(self):
        return str(self.dna)    

class Evolution():
    def __init__(self, num_of_organisms):
        self.population = [Organism(DNA(), 0.8) for i in range(num_of _organisms)]
        self.generations = 0
    
    def is_complete(self):
        for organism in self.population:
            for dna in organism:
                for chromosme in dna:
                    for gene in chromosome:
                        return all(gene.value)


    def big_bang(self):
        for organism in self.population:
            organism.mutate()
    
    def chromose_all_true(self, chromosome):
        return all(chromosome)

    def dna_all_true():
        for chromosome in dam:
            if not all(chromosome):
                return False
            else:
                return True



d1= DNA()
print(d1.value)
print("\n")
d1.mutate()
print(d1.value)