## UNFINISHED

import random
import unittest
import genetic
import datetime

class KnightsTests(unittest.TestCase):
    def test_3x4(self):
        width = 4
        height = 3
        # 1,0 2,0 3,0
        # 0,2 1,2 2,0
        # 2 N N N .
        # 1 . . . .
        # 0 . N N N
        # 0 1 2 3
        self.find_knight_positions(width, height, 6)
        
    
    def find_knight_positions(self,boardWidth, boardHeight, expectedKnights):
        startTime = datetime.datetime.now()

        def fnDisplay(candidate):
            display(candidate, startTime, boardWidth, boardHeight)

        def fnGetFitness(genes):
            return get_fitness(genes, boardWidth, boardHeight)

        def fnGetRandomPosition():
            return Position(random.randrange(0, boardWidth), random.randrange(0, boardHeight) )

        def fnMutate(genes):
            mutate(genes, fnGetRandomPosition)

        def fnCreate():
            return create(fnGetRandomPosition, expectedKnights)

        optimalFitness = boardWidth*boardHeight
        best = genetic.get_best(fnGetFitness, None,
            optimalFitness, None, fnDisplay,fnMutate,fnCreate)
        self.assertTrue(not optimalFitness > best.Fitness)
        

class Position:
    X = None
    Y = None

    def __init__(self, x, y) -> None:
        self.X = x
        self.Y = y

    def __str__(self) -> str:
        return "{0},{1}".format(self.X, self.Y)

    def __eq__(self, __o: object) -> bool:
        return self.X == __o.X and self.Y == __o.Y

    def __hash__(self) -> int:
        return self.X*1000+self.Y

def get_attacks(location, boardWidth, boardHeight):
    return [i for i in set(
        Position(x + location.X, y + location.Y)
        for x in [-2, -1, 1, 2] if 0 <= x + location.X < boardWidth
        for y in [-2, -1, 1, 2] if 0 <= y + location.Y < boardHeight
        and abs(y) != abs(x)
    )]


def create(fnGetRandomPosition, expectedKnights):
    genes = [fnGetRandomPosition() for _ in range(expectedKnights)]
    return genes


def mutate(genes, fnGetRandomPosition):
    index = random.randrange(0, len(genes))
    genes[index] = fnGetRandomPosition()


class Board:
    def __init__(self, positions, width, height):
        board = [['.'] * width for _ in range(height)]
        for index in range(len(positions)):
            knightPosition = positions[index]
            board[knightPosition.Y][knightPosition.X] = 'N'
        self._board = board
        self._width = width
        self._height = height


    def print(self):
    # 0,0 prints in bottom left corner
        for i in reversed(range(self._height)):
            print(i, "\t", ' '.join(self._board[i]))
        print(" \t", ' '.join(map(str, range(self._width))))

def display(candidate, startTime, boardWidth, boardHeight):
    timeDiff = datetime.datetime.now() - startTime
    board = Board(candidate.Genes, boardWidth, boardHeight)
    board.print()

    print("{0}\n\t{1}\t{2}".format(
        ' '.join(map(str, candidate.Genes)),
        candidate.Fitness,
        str(timeDiff)
    ))

def get_fitness(genes, boardWidth, boardHeight):
    attacked = set(pos
                for kn in genes
                for pos in get_attacks(kn,boardWidth,boardHeight))
    return len(attacked)