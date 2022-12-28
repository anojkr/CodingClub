from snakesladders.models.board import Board
from snakesladders.services.diceservice import DiceService
class SnakeAndLadderService:
	#default board size 100 if not provided
	def __init__(self,size=100):
		self.board = Board(size)
		#board has following : snakeList[],ladderList[],playersCurrentPositions{}

	def setPlayers(self,players):		
		self.playerQueue = []		
		self.initialNumberOfPlayers = len(players)
		playerPositions = {}
		for player in players:
			#fifo queue of players
			self.playerQueue.append(player)
			#initially all players at 0
			playerPositions[player.getId()] = 0
		
		self.board.playersCurrentPositions = playerPositions

	def setSnakes(self,snakes):
		self.board.snakeList = snakes

	def setLadders(self,ladders):
		self.board.ladderList = ladders

	def getTotalValueAfterDiceRolls(self):
		return DiceService().roll()

	def getNewPositionAfterGoingThroughSnakesAndLadders(self,player,position):
		print ("Processing Position " + str(position) + " for " + player.getName())
		while 1:
			for ladder in self.board.ladderList:
				if ladder.getStart() == position:
					print (player.getName() + " Ladder Alert at:" + str(position) + " moved from " + str(position) + " to " + str(ladder.getEnd() ))
					position = ladder.getEnd()
					continue

			for snake in self.board.snakeList:
				if snake.getStart() == position:
					print (player.getName() + " Snake Alert at:" + str(position) + " moved from " + str(position) + " to " + str(snake.getEnd()))
					position = snake.getEnd()
					continue
			break
		return position

	def movePlayer(self,player,diceValue):
		oldPosition = self.board.playersCurrentPositions[player.getId()]
		newPosition = oldPosition + diceValue
		boardSize = self.board.getSize()
		if (newPosition > boardSize):
			newPosition = oldPosition
		else:
			newPosition = self.getNewPositionAfterGoingThroughSnakesAndLadders(player,newPosition)

		self.board.playersCurrentPositions[player.getId()] = newPosition

	def hasPlayerWon(self,player):
		return self.board.getPlayersCurrentPositions().get(player.getId()) == self.board.getSize()

	def isGameCompleted(self):
		# we pop player after he win from playerQueue		
		return self.initialNumberOfPlayers > len(self.playerQueue)

	def startGame(self):		
		while (self.isGameCompleted() == False):
			diceValue = self.getTotalValueAfterDiceRolls()
			player = self.playerQueue.pop(0) # fifo
			self.movePlayer(player,diceValue)
			if self.hasPlayerWon(player):
				print (player.getName() + " wins the game")
				self.board.getPlayersCurrentPositions().pop(player.getId())
			else:
				self.playerQueue.append(player) # append player for next turn



		