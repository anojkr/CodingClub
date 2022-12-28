class Board:
	def __init__(self,size):
		self.size = size
		self.snakeList = []
		self.ladderList = []
		#assume n players can play 1 by 1 in FIFO
		self.playersCurrentPositions = {}

	def getSize(self):
		return self.size

	def setSize(self,size):
		self.size = size

	def getSnakeList(self):
		return self.snakeList

	def setSnakeList(self,snakeList):
		self.snakeList = snakeList

	def getLadderList(self):
		return self.ladderList

	def setLadderList(self,ladderList):
		self.ladderList = ladderList

	def getPlayersCurrentPositions(self):
		return self.playersCurrentPositions

	def setPlayersCurrentPositions(self,playersCurrentPositions):
		self.playersCurrentPositions = playersCurrentPositions



