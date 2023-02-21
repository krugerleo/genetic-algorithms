import datetime
import genetic

def test_hello_world():
    target = "Hello World Jaguara"
    guess_password(target)

def guess_password(target):
    geneset = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!."
    startTime = datetime.datetime.now()

    def fnGetFitness(genes):
        return get_fitness(genes, target)

    def fnDisplay(genes):
        display(genes, target, startTime)
    
    optimalFitness = len(target)
    genetic.get_best(fnGetFitness, len(target), optimalFitness, geneset, fnDisplay)


def display(genes, target, startTime):
    timeDiff = datetime.datetime.now() - startTime
    fitness = get_fitness(genes, target)
    print("{0}\t{1}\t{2}".format(genes, fitness, str(timeDiff)))

def get_fitness(genes, target):
    return sum(1 for expeced,actual in zip(target,genes) if expeced == actual)

if __name__ == '__main__':
    test_hello_world()