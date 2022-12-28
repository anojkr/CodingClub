import random
class DiceService:
	def roll(self):
		#1 and 6 both included
		return random.randint(1,6)
