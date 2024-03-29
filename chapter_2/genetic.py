import random
import statistics
import time
import sys

class Chromosome:
    Genes = None
    Fitness = None

    def __init__(self, genes, fitness) -> None:
        self.Genes = genes
        self.Fitness = fitness


def _generate_parent(length, geneSet, get_fitness)-> Chromosome:
    genes = []
    while len(genes) < length:
        sampleSize = min(length - len(genes), len(geneSet))
        genes.extend(random.sample(geneSet, sampleSize))
    fitness = get_fitness(genes)
    return Chromosome(genes, fitness)
    

def _mutate(parent, geneSet, get_fitness)-> Chromosome:
    index = random.randrange(0,len(parent.Genes))
    childGenes = parent.Genes[:]
    newGene, alternate = random.sample(geneSet, 2)
    childGenes[index] = alternate \
        if newGene == childGenes[index] \
        else newGene
    fitness = get_fitness(childGenes)
    return Chromosome(childGenes, fitness)

def _get_improvement(new_cihld, generate_parent):
    bestParent = generate_parent()
    yield bestParent
    while True:
        child = new_cihld(bestParent)
        if bestParent.Fitness > child.Fitness:
            continue
        if not child.Fitness > bestParent.Fitness:
            bestParent = child
            continue
        yield child
        bestParent = child

def _mutate_custom(parent, custom_mutate, get_fitness):
    childGenes = parent.Genes[:]
    custom_mutate(childGenes)
    fitness = get_fitness(childGenes)
    return Chromosome(childGenes,fitness)

def get_best(get_fitness, targetLen, optimalFitness, geneSet, display, custom_mutate=None, custom_create=None):
    random.seed()

    if custom_mutate is None:
        def fnMutate(parent):
            return _mutate(parent, geneSet, get_fitness)
    else:
        def fnMutate(parent):
            return _mutate_custom(parent, custom_mutate, get_fitness)

    if custom_create is None:
        def fnGenerateParent():
            return _generate_parent(targetLen, geneSet, get_fitness)
    else:
        def fnGenerateParent():
            genes = custom_create()
            return Chromosome(genes, get_fitness(genes))
        

    for improvement in _get_improvement(fnMutate, fnGenerateParent):
        display(improvement)
        if not optimalFitness > improvement.Fitness:
            return improvement

class Benchmark:
    @staticmethod
    def run(function):
        timings = []
        stdout = sys.stdout
        for i in range(100):
            sys.stdout = None
            startTime = time.time()
            function()
            seconds = time.time() - startTime
            sys.stdout = stdout
            timings.append(seconds)
            mean = statistics.mean(timings)
            if i < 10 or i %10 == 9:
                print("{0} {1:3.2f} {2:3.2f}"\
                .format(1 + i, mean, statistics.stdev(timings,mean) if i > 1 else 0))
        
