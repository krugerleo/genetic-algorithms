# File: guessPassword.py
#    from chapter 1 of _Genetic Algorithms with Python_, an ebook
#    for sale at http://leanpub.com/genetic_algorithms_with_python
#
# Author: Leonardo Bueno Nogueira Kruger
import random
import datetime

geneSet = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!."
target = "paPaGaio"



# evaluate fitness
def get_fitness(guess):
    return sum (1 for expected,actual in zip(target,guess) if expected == actual)

# Generate first parent
def generate_parent(length):
    genes = []
    while len(genes)< length:
        sampleSize = min(length - len(genes), len(geneSet))
        genes.extend(random.sample(geneSet,sampleSize))
    return ''.join(genes)

def mutate_parent(parent):
    index = random.randrange(0, len(parent))
    childGenes = list(parent)
    newGene, alternate = random.sample(geneSet,2)
    childGenes[index] = alternate if newGene == childGenes[index] else newGene
    return ''.join(childGenes)

def display(guess):
    timeDiff = datetime.datetime.now() - startTime
    fitness = get_fitness(guess)
    print("{0}\t{1}\t{2}".format(guess, fitness, str(timeDiff)))

if __name__ == '__main__':
    random.seed()
    startTime = datetime.datetime.now()
    bestParent = generate_parent(len(target))
    bestFitness = get_fitness(bestParent)
    display(bestParent)
    while True:
        child = mutate_parent(bestParent)
        childFitness = get_fitness(child)
        if bestFitness >= childFitness:
            continue
        display(child)
        if childFitness >= len(bestParent):
            break
        bestFitness = childFitness
        bestParent = child

