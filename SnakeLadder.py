import enum
import random


class Snake(object):

    def __init__(self, id, start, end):
        self.id = id
        self.start = start
        self.end = end


class Ladder(object):

    def __init__(self, id, start, end):
        self.id = id
        self.start = start
        self.end = end


class Player(object):
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.score = 0

    def getPlayerId(self):
        return self.id


class Cell(object):

    def __init__(self, id):
        self.id = id


class Board(object):

    def __init__(self, size):
        self.size = size
        self.snakes = {}
        self.ladders = {}
        self.player = {}



class Dice(object):

    def __init__(self, range):
        self.range = range

    def rollDice(self):
        return random.randint(1, self.range)


class GameStatus(enum.Enum):
    GAME_NOT_STARTED = 1,
    GAME_IN_PROGRESS = 2,
    GAME_ENDED = 3



class Game(object):

    def __init__(self, board):
        self.board = board

    def setGameStatusInProgress(self):
        self.gameStatus = GameStatus.GAME_IN_PROGRESS
        return self

    def setSnake(self, cellId, snake):
        self.snakes[cellId] = snake

    def getSnake(self, cellId):
        return self.snakes.get(cellId)

    def setLadder(self, cellId, ladder):
        self.ladders[cellId] = ladder

    def getLadder(self, cellId):
        return self.ladders.get(cellId)

    def getPlayerPosition(self, playerId):
        return self.playersPosition[playerId]

    def setPlayerPosition(self, playerId, position):
        self.playersPosition[playerId] = position
        return self

    def initGame(self):
        self.players

    def startGame(self):
        while True:
            for eachPlayer in self.players:
                nextStep = self.dice.rollDice()
                currentPlayerPosition = self.getPlayerPosition(eachPlayer.getPlayerId())
                self.setPlayerNextPosition(currentPlayerPosition, nextStep)

    def setPlayerNextPosition(self, currPosition, nextStep):
        pass


if __name__ == '__main__':
    board = Board(5)
