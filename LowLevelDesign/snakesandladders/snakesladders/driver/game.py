import sys
sys.path.insert(0,'/Users/spoylios/Desktop/mc')

from snakesladders.services.snake_and_ladder_service import SnakeAndLadderService
from snakesladders.models.ladder import Ladder
from snakesladders.models.snake import Snake
from snakesladders.models.player import Player
#snakes
snakes = []
snakes.append(Snake(99,10))
snakes.append(Snake(84,65))
snakes.append(Snake(75,35))
snakes.append(Snake(66,23))
snakes.append(Snake(24,12))
snakes.append(Snake(18,3))
#ladders
ladders = []
ladders.append(Ladder(7,21))
ladders.append(Ladder(19,89))
ladders.append(Ladder(27,83))
ladders.append(Ladder(31,78))
ladders.append(Ladder(47,68))
ladders.append(Ladder(57,87))
ladders.append(Ladder(76,98))
#player
players = []
players.append(Player(1,'Pawan'))
players.append(Player(2,'Abhinav'))
players.append(Player(3,'Gyan'))
players.append(Player(4,'Divyank'))


obj = SnakeAndLadderService()
obj.setLadders(ladders)
obj.setPlayers(players)
obj.setSnakes(snakes)

obj.startGame()