import datetime
import genetic
import unittest
import random

class GuessPasswordTests(unittest.TestCase):
    geneset = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!."

    def test_benchmark(self):
        genetic.Benchmark.run(self.test_Random)

    def For_I_am_fearfully_and_wonderfully_made(self):
        target = "For I am Fearfully and wonderfully mage."
        self.guess_password(target)

    def test_Random(self):
        length = 150
        target = ''.join(random.choice(self.geneset) for _ in range(length))
        self.guess_password(target)

    # def test_Hello_World(self):
    #     target = "Hello World Jaguara"
    #     self.guess_password(target)


    def guess_password(self, target):
        geneset = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!."
        startTime = datetime.datetime.now()

        def fnGetFitness(genes):
            return get_fitness(genes, target)

        def fnDisplay(candidate):
            display(candidate, startTime)
        
        optimalFitness = len(target)
        best = genetic.get_best(fnGetFitness, len(target), optimalFitness, geneset, fnDisplay)

        self.assertEqual(best.Genes, target)


def display(candidate, startTime):
    timeDiff = datetime.datetime.now() - startTime
    print("{0}\t{1}\t{2}".format(candidate.Genes, candidate.Fitness, str(timeDiff)))

def get_fitness(genes, target):
    return sum(1 for expeced,actual in zip(target,genes) if expeced == actual)

if __name__ == '__main__':
    unittest.main()